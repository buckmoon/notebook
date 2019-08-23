"""Tornado handlers for the live notebook view."""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import os
import json
from tornado import web
HTTPError = web.HTTPError

from ..base.handlers import (
    IPythonHandler, FilesRedirectHandler, path_regex,
)
from ..utils import url_escape


class NotebookHandler(IPythonHandler):

    @web.authenticated
    def get(self, path):
        """get renders the notebook template if a name is given, or
        redirects to the '/files/' handler if the name is not given."""
        path = path.strip('/')
        cm = self.contents_manager
        miw_dict = json.loads(self.miw_dict_json)
        # print("#---------------------")
        # print(self.ml_project_id)
        # print(miw_dict['ml_project_id'])
        # print("#---------------------")
        # will raise 404 on not found
        try:
            if cm.file_exists(path):
                model = cm.get(path, content=False)
            else:
                model = {}
                model['type'] = 'directory'
                path_dir = '/'.join(path.split('/')[:-1])
                cm.new(model, path_dir)
                model = {}
                model['type'] = 'notebook'
                # path = 'miw/Node.ipynb'
                cm.new(model, path)
                model = cm.get(path, content=False)
        except web.HTTPError as e:
            if e.status_code == 404 and 'files' in path.split('/'):
                # 404, but '/files/' in URL, let FilesRedirect take care of it
                return FilesRedirectHandler.redirect_to_files(self, path)
            else:
                raise
        if model['type'] != 'notebook':
            # not a notebook, redirect to files
            return FilesRedirectHandler.redirect_to_files(self, path)
        name = path.rsplit('/', 1)[-1]
        self.write(self.render_template('notebook.html',
            notebook_path=path,
            notebook_name=name,
            kill_kernel=False,
            mathjax_url=self.mathjax_url,
            mathjax_config=self.mathjax_config,
            ml_project_id=self.ml_project_id,
            miw=miw_dict
            )
        )


#-----------------------------------------------------------------------------
# URL to handler mappings
#-----------------------------------------------------------------------------


default_handlers = [
    (r"/notebooks%s" % path_regex, NotebookHandler),
]
