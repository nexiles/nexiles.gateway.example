# -*- coding: utf-8 -*-

import logging

from nexiles.tools.rest.services import service_base_url

from .blueprint import blueprint

from nexiles.gateway.example import version
from nexiles.gateway.example import license
from nexiles.gateway.example import example_api


__version__ = version.__version__
__build__   = version.__build__
__date__    = version.__date__

__license__ = license.LICENSE

logger = logging.getLogger("nexiles.gateway.example")


def register(app):
    """register(app) -> new app

    Register the data service.

    :returns: flask app
    """
    logger.info("register: app=%r" % app)

    app.register_blueprint(
        blueprint,
        url_prefix=service_base_url + "/example")

    return app
