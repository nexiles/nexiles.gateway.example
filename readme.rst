nexiles.gateway.example
=======================

|build-status| |docs|

Abstract
--------

A example service module for nexiles.gateway.

What?
-----

This is a example service module to be used as template
for creating new services fo nexiles.gateway.

nexiles.gateway is a generic HTTP API for `PTC Windchill`_ which offers
a REST-Like, JSON based API to access, create, and manipulate Windchill
objects.

.. _PTC Windchill: http://www.ptc-solutions.de/produkte/ptc-windchill/ptc-windchill-102.html

Why?
----

Usually, `PTC Windchill`_ extensions (or *customizations*) are coded in
Java, and the UI is done by customizing the `PTC Windchill`_ UI directly.

While this is fine for one-off projects, we find that the mainenance cost
of this approach is too high.

Using nexiles.gateway, we separate UI (front-end) from business logic (back-end),
and thus free ourselves (and the customer) from the restrictions and maintenance
overhead imposed by the normal customization approach.

Additionally, using nexiles.gateway allows us to use the dynamic programming language
Python_, which allows to use a more agile and interactive development process.  This
gives us and our customers a great advantage wrt. time-to-market and development costs,
as well as very quick iteration cycles.

For more information, contact us_.

.. _Python: http://www.python.org
.. _us: mailto:info@nexiles.com?subject=nexiles.gateway%20request%20for%20information&cc=se@nexiles.de