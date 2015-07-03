Deploying
=========

Abstract
--------

This documentation explains how to deploy the built module to a Windchill server, how
to verify it's version and how to use the API help.

Assumptions
-----------

To perform these steps, you need:

- A running Windchill server
- Filesystem access to the server
- Administrative access to the server
- Have nexiles.tools Version 1.5 or better installed and running on that
  server.

Deployment Steps
----------------

The deployment of a **nexiles.gateway** module consists of these steps:

- Copying the built egg file to the windchill server
- Configuring **nexiles.gateway** to load the new module (aka *plugin*)
- Restarting the Windchill Service
- Verifying that the module has been load and the version matches

Copying the egg file
--------------------

TBD

Configuring *nexiles.gateway* to load the module on startup
-----------------------------------------------------------

TBD

Restarting Windchill
--------------------

TBD

Verifying the Version
---------------------

To verify the version, simply point your browser to:

	https://www.example.com/Windchill/servlet/nexiles/tools/plugins/index.html

And verify that the module is listed and the version is correct.
