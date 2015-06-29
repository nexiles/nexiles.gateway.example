# -*- coding: utf-8 -*-
#
# Copyright (c) nexiles GmbH
from __future__ import with_statement

import os
import flask
import logging
import datetime

from nexiles.tools.rest import APIError
from nexiles.tools.rest import handle_api_error
from nexiles.tools.rest import returns_json
from nexiles.tools.rest import inject_runtime

from nexiles.tools import utils, get_wrapped, principal

""" implementation of the nexiles|gateway example service
"""

__all__ = ["blueprint"]

logger = logging.getLogger("nexiles.gateway.example")

blueprint = flask.Blueprint("example", __name__,
                            template_folder="templates",
                            static_folder="static")


def get_template_path(template):
    """get_template_path(p) -> path

    Build template path by prepending the template base directory.

    :returns: string
    """
    return "bom/" + template


def get_api():
    return [{"name": "version",
             "description": "get plugin version",
             "url": flask.url_for(".version", _external=True)},
            {"name": "api",
             "description": "api documentation",
             "url": flask.url_for(".api", _external=True)},
            {"name": "example_post",
             "description": "example POST route",
             "url": flask.url_for(".example_open",
                                  _external=True)},
            {"name": "example_get",
             "description": "example GET route",
             "url": flask.url_for(".example_get",
                                  limit="max results",
                                  _external=True)},
            ]

@blueprint.route("/1.0", endpoint="api", methods=["GET"])
@blueprint.route("/1.0/api.json", endpoint="api", methods=["GET"])
@handle_api_error
@returns_json
@inject_runtime
def api():
    """api() -> JSON

    cargotec erp service api description.

    :returns: JSON data
    """
    logger.debug("api()")
    return {
        "api": get_api()
        }

# vim: set ft=python ts=4 sw=4 expandtab :
