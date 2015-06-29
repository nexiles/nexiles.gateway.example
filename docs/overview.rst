Overview
========

Abstract
--------

Here we give an overview of the example code.

Overview
--------

Nexiles gateway services are *plug-ins* to *nexiles.gateway* which implement a JSON HTTP API using
multiple *routes*.  All routes of a service have a common base URL.

The API the modules implement may use the *nexiles.gateway* core API, other service's public API and
the Windchill API.

We recommend that the *business logic* to be grouped in logical modules, and to provide the *glue*
to the HTTP and JSON formatting in API modules.  This way, the business logic will be usable by other
modules directly, and the API and the logic are nicely separated.

Flask Web Framework
-------------------

The **nexiles.gateway** core uses the Flask_ web feb framework to provide it's services.  It uses
custom code to hook into the Tomcat_ servlet_ engine which is used by Windchill.

This example code uses `Flask Blueprints`_ to define API endpoints.  This is a **requirement** for
all service modules.

.. _Flask: http://flask.pocoo.org/docs/0.10
.. _Tomcat: http://tomcat.apache.org/
.. _servlet: https://en.wikipedia.org/wiki/Java_servlet
.. _Flask Blueprints: http://flask.pocoo.org/docs/0.10/blueprints/

Implemented functionality
-------------------------

The example service is very simple and provides two API endpoints.

URL Format
~~~~~~~~~~

Generally, URLs to gateway modules consist of these parts:

- The Windchill Web App URL
- The **nexiles.gateway** service entry point
- The module base name
- The route part.

For example, in the URL `https://www.example.com/Windchill/servlet/nexiles/tools/services/example/version` the parts
are:

- `https://www.example.com/Windchill`
- `/servlet/nexiles/tools/services`
- `example/`
- `version`

Below, we obmit the Windchill Web App URL and the **nexiles.gateway** service entry point.

Please note that we recommend to have **version numbers** in API endpoints.  This way, API upgrades can be made
without breaking existing consumers by simply creating new entry points.

API: example_get
~~~~~~~~~~~~~~~~
:endpoint: `example/1.0/example`
:http method: `GET`
:request parameter: `limit`, optional number
:example: `https://www.example.com/Windchill/servlet/nexiles/tools/services/example/1.0/example?limit=10`

This API endpoint performs a simple, limited query and formats the results as JSON data.  The API module
calls into the business logic module to do the actual query.

To use test the API from the CLI, do something like::

	$ curl -q --user wtadmin:wtadmin -H "Conent-Type: application/json" -X GET \
		'https://www.example.com/Windchill/servlet/nexiles/tools/services/example/1.0/example?limit=10'
	{
		"count": 42,
		"items": [
			{
				"url": "....",
				"details": "....",
				"OID": "wt.epm.EPMDocument:42",
				"name:" "example.prt"
			},
			...
		]
	}


API: example_post
~~~~~~~~~~~~~~~~~
:endpoint: `example/1.0/example`
:http method: `POST`

This api call does nothing but echo back the JSON body.  To test this route, you need to issue a HTTP POST, e.g.
something like::

	$ curl -q --user wtadmin:wtadmin -H "Conent-Type: application/json" -X POST -d '{hello: "world"}' \
		https://www.example.com/Windchill/servlet/nexiles/tools/services/example/1.0/example
	{
		"body": {
			"hello": "world"
		}
	}


Module Overview
---------------

Module: example.py
~~~~~~~~~~~~~~~~~~

This module defines functions which implement the business logic.  Because this is an example, the business logic
is very simple and consists only of one function wich does a very simple query.

Please note, that:-

- The business logic module has full access to all the Windchill APIs,
- has full access to all *nexiles.gateway* modules installed,
- has full access to the *nexiles.gateway* core API.

Business modules by conventions deal with native **Windchill Objects**.  It's the callee's responsibility to format
these to other formats -- for example, the API module needs to produce JSON.

Module: example_api.py
~~~~~~~~~~~~~~~~~~~~~~

This module defines the HTTP JSON API of the example module.  By convention, the module is named like the business
logic module with an `_api` postfix.

The API module's responsibility is to:-

- Define API routes, i.e. mappings of URL endpoints to functions and HTTP verbs,
- define these route functions,
- handle request parameters and request payloads if neccessary,
- call into the business logic to using decoded parameters to perform the task at hand, and finally
- to format the results to JSON.
