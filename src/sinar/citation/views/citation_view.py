# -*- coding: utf-8 -*-

from plone.dexterity.browser.view import DefaultView
from sinar.citation import _


# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class CitationView(DefaultView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('citation_view.pt')

    def __call__(self):
        # Implement your own actions:
        return super(CitationView, self).__call__()
