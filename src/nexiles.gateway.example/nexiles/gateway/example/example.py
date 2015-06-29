import logging

from nexiles.tools import query

logger = logging.getLogger("nexiles.gateway.example")

__all__ = ["example_query"]


def example_query(limit=25):
    """
    example_query(limit) -> sequence of WT objects

    Run a example query.

    :param limit:   optional limit

    :returns: A sequence of windchill objects
    """

    # We just use the nexiles.gateway core API to query for all
    # parts.
    #
    # Note: This is just an example.
    return query.find("wt.epm.EPMDocument", name="*.prt", limit=limit)


# vim: set ft=python ts=4 sw=4 expandtab :

