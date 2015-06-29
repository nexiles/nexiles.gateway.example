# -*- coding: utf-8 -*-

import pkg_resources
from nexiles.tools.rest import returns_json
from .blueprint import blueprint


def version():
    dist = pkg_resources.get_distribution("nexiles.gateway.example")
    return dist.version

__version__ = version()
__build__ = 1
__date__ = '2015-04-27'


@blueprint.route("/version", methods=["GET"])
@returns_json
def apiversion():
    return {
        "version": __version__,
        "build": __build__,
        "date": __date__
    }
