# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
)
from plone.testing import z2

import sinar.citation


class SinarCitationLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=sinar.citation)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'sinar.citation:default')


SINAR_CITATION_FIXTURE = SinarCitationLayer()


SINAR_CITATION_INTEGRATION_TESTING = IntegrationTesting(
    bases=(SINAR_CITATION_FIXTURE,),
    name='SinarCitationLayer:IntegrationTesting',
)


SINAR_CITATION_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(SINAR_CITATION_FIXTURE,),
    name='SinarCitationLayer:FunctionalTesting',
)


SINAR_CITATION_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        SINAR_CITATION_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='SinarCitationLayer:AcceptanceTesting',
)
