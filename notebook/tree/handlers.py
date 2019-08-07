"""Tornado handlers for the tree view."""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

from tornado import web
import os
from ..base.handlers import IPythonHandler, path_regex
from ..utils import url_path_join, url_escape


class TreeHandler(IPythonHandler):
    """Render the tree view, listing notebooks, etc."""

    def generate_breadcrumbs(self, path):
        breadcrumbs = [(url_path_join(self.base_url, 'tree'), '')]
        parts = path.split('/')
        for i in range(len(parts)):
            if parts[i]:
                link = url_path_join(self.base_url, 'tree',
                    url_escape(url_path_join(*parts[:i+1])),
                )
                breadcrumbs.append((link, parts[i]))
        return breadcrumbs

    def generate_page_title(self, path):
        comps = path.split('/')
        if len(comps) > 3:
            for i in range(len(comps)-2):
                comps.pop(0)
        page_title = url_path_join(*comps)
        if page_title:
            return page_title+'/'
        else:
            return 'Home'

    @web.authenticated
    def get(self, path=''):
        raise web.HTTPError(404)


#-----------------------------------------------------------------------------
# URL to handler mappings
#-----------------------------------------------------------------------------


default_handlers = [
    (r"/tree%s" % path_regex, TreeHandler),
    (r"/tree", TreeHandler),
    ]
