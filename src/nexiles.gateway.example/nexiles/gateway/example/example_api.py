# -*- coding: utf-8 -*-
#
# File: example_api.py
#
# Copyright (c) nexiles GmbH

from __future__ import with_statement

import flask
import logging

from wt.util import WTException
from wt.admin import AdministrativeDomainHelper

from nexiles.tools.utils import OBJ, OID
from nexiles.tools.rest.api import ApiBase

from nexiles.tools.rest import APIError
from nexiles.tools.rest import handle_api_error
from nexiles.tools.rest import returns_json
from nexiles.tools.rest import inject_runtime

from nexiles.tools.utils import get_info_page_url

from .blueprint import blueprint

# This module implements the "business logic"
from .example import example_query

logger = logging.getLogger("nexiles.gateway.example")

if 0:
    logger.setLevel(logging.DEBUG)


def format_object(obj):
    """format_object(obj) -> mapping

    This function maps Windchill Object Attributes to JSON.
    """
    d = {}

    # Add the OID and teh name of this object.
    d["OID"] = OID(obj)
    d["name"] = obj.getName()

    # The URL will point to the nexiles.gateway URL for this object
    d["url"] = ApiBase.url(d["oid"])

    # This will be the Windchill Details Page for that object
    d["details"] = get_info_page_url(obj)

    return d


######################################################################
# API routes

@blueprint.route("/1.0/example", endpoint="example_post", methods=["POST"])
@handle_api_error
@returns_json
@inject_runtime
def example():
    logger.debug("example_post")

    logger.debug("JSON Body: %r", flask.request.json)
    json_body = flask.request.json
    if not json_body:
        raise APIError(400, "illegal request", "need a json body.")

    # This example does nothing but echo the JSON body back to the
    # client.

    return {
        "body": json_body
    }


@blueprint.route("/1.0/example/<int:session_id>", endpoint="example_get", methods=["GET"])
@handle_api_error
@returns_json
@inject_runtime
def example_get_page(session_id):
    limit = flask.request.args.get("limit", 25, type=int)
    logger.debug("example_get: limit=%d", limit)

    # Call the example code form the business logic.  This is a hypothetic
    # query with some limit.  The query returns Windchill Objects.
    results = example_query(limit=limit)

    # Format the Windchill Objects to suitable JSON.
    items = []
    for obj in results:
        items.append(format_object(obj))

    return {
        "count": len(items),
        "items": items
    }


# vim: set ft=python ts=4 sw=4 expandtab :
