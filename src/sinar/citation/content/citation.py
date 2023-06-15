# -*- coding: utf-8 -*-
# from plone.app.textfield import RichText
# from plone.autoform import directives
from plone.dexterity.content import Container
# from plone.namedfile import field as namedfile
from plone.supermodel import model
from sinar.citation import _
# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from plone.app.dexterity import textindexer
from zope import schema
from zope.interface import implementer


class ICitation(model.Schema):
    """ Marker interface and Dexterity Python Schema for Citation
    """
    # If you want, you can load a xml model created TTW here
    # and customize it in Python:

    # model.load('citation.xml')

    # directives.widget(level=RadioFieldWidget)
    # level = schema.Choice(
    #     title=_(u'Sponsoring Level'),
    #     vocabulary=LevelVocabulary,
    #     required=True
    # )

    # text = RichText(
    #     title=_(u'Text'),
    #     required=False
    # )

    textindexer.searchable('author')
    author = schema.TextLine(
        title=_(u'Author or Website Name'),
        required=False,
        )

    url = schema.URI(
        title=_(u'Link'),
        description=_(u'URL to citation. eg https://example.org/report'),
        required=False
    )

    # fieldset('Images', fields=['logo', 'advertisement'])
    # logo = namedfile.NamedBlobImage(
    #     title=_(u'Logo'),
    #     required=False,
    # )

    # advertisement = namedfile.NamedBlobImage(
    #     title=_(u'Advertisement (Gold-sponsors and above)'),
    #     required=False,
    # )

    # directives.read_permission(notes='cmf.ManagePortal')
    # directives.write_permission(notes='cmf.ManagePortal')
    # notes = RichText(
    #     title=_(u'Secret Notes (only for site-admins)'),
    #     required=False
    # )


@implementer(ICitation)
class Citation(Container):
    """
    """
