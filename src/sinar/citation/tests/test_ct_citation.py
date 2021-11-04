# -*- coding: utf-8 -*-
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles, TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from sinar.citation.content.citation import ICitation  # NOQA E501
from sinar.citation.testing import SINAR_CITATION_INTEGRATION_TESTING  # noqa
from zope.component import createObject, queryUtility

import unittest


class CitationIntegrationTest(unittest.TestCase):

    layer = SINAR_CITATION_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_citation_schema(self):
        fti = queryUtility(IDexterityFTI, name='Citation')
        schema = fti.lookupSchema()
        self.assertEqual(ICitation, schema)

    def test_ct_citation_fti(self):
        fti = queryUtility(IDexterityFTI, name='Citation')
        self.assertTrue(fti)

    def test_ct_citation_factory(self):
        fti = queryUtility(IDexterityFTI, name='Citation')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            ICitation.providedBy(obj),
            u'ICitation not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_citation_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Citation',
            id='citation',
        )

        self.assertTrue(
            ICitation.providedBy(obj),
            u'ICitation not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('citation', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('citation', parent.objectIds())

    def test_ct_citation_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Citation')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_citation_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Citation')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'citation_id',
            title='Citation container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
