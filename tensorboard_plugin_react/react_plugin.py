"""Example of a TensorBoard dynamic plugin."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import mimetypes
import os

from tensorboard.plugins import base_plugin
from werkzeug import wrappers


class ReactPlugin(base_plugin.TBPlugin):
  """WebpackReact Plugin for TensorBoard."""

  plugin_name = 'react'

  def __init__(self, context):
    """Instantiates WebpackReact via TensorBoard core.

    Args:
      context: A base_plugin.TBContext instance.
    """

  def get_plugin_apps(self):
    return {
        '/static/js/index.js': self.serve_static,
        '/static/js/main.js': self.serve_static,
        '/static/js/main.js.map': self.serve_static,
        '/static/media/logo.svg': self.serve_static,
    }

  def is_active(self):
    return True

  def _send_file(self, file_path):
    with open(file_path, 'rb') as file_obj:
      mimetype = mimetypes.guess_type(file_path)[0]
      return wrappers.Response(
          file_obj.read(), content_type=mimetype)

  @wrappers.Request.application
  def serve_static(self, request):
    path_frags = request.path.rsplit('/', 3)[-3:]
    if path_frags[0] != u'static':
      return

    build = os.path.join(os.path.dirname(__file__), 'frontend/build/')
    return self._send_file(os.path.join(build, *path_frags))

  def frontend_metadata(self):
    return super(ReactPlugin, self).frontend_metadata()._replace(
        tab_name='React Demo',
        es_module_path='/static/js/index.js',
    )


class ReactPluginLoader(base_plugin.TBLoader):
  """Loads React Plugin dynamically. Allows dynamic imorts."""

  def load(self, context):
    return ReactPlugin(context)


