Building
========

Abstract
--------

This documentation explains the build setup.

Assumptions
-----------

Because this is all about creating a server-side extension for `PTC Windchill`_,
we assume that you have some experience with Windchill.

We assume that your local development machine has access to a -- mounted or copied --
Windchill installation.

We also assume that your development machine has unix-like tools installed.  We use
`Apple Mac`_s as development machines.

Prerequisites
-------------

.. note:: Installing these is out of scope for this document.  If you need help,
   contact us_.

**JDK**
	:version: `1.7.x` (java 1.7)

	We need a JDK to do Windchill development.  We assume that the `JAVA_HOME` is correctly set and java binaries and tools ar in your `PATH`.

**Jython**
	:version: `2.7.0` or better

	We use Jython_ for development.  We assume the `JYTHON_HOME` environment variable is set correctly.

**Windchill**
	:version: `10.2` or better

	We need a *locally* available -- mounted or copied -- Windchill codebase directory to compile sources.  We assume that the `WT_HOME` environment
	variable points to the directory containing the `site.xconf` file.

	.. note: **nexiles.gateway** actually supports all Windchill versions starting from version 9.1.  However,
	   for new projects we recommend to use version `10.2` or better.

Build Requirements
------------------

.. note:: You can use your own build tools if you like -- there's nothing magical about gateway services.  They're just
   python (jython) eggs.

The build process uses Fabric_ to automate the build.  The build uses tasks from *nexiles.fabric.tasks**, for more information
on them see there_.

To install the build requirements, you **could** do::

	$ cd nexiles.gateway.example
	$ pip install -r requirements.txt

We suggest to create a virtualenv_ for development instead::

	$ cd nexiles.gateway.example
	$ virtualenv .
	$ . bin/activate
	(nexiles.gateway.example)$ pip install -r requirements.txt

In general, this documentation assumes that you have set up a virtualenv_.  You *can* use any other means to isolate
your development environment.

.. note:: Jython_ currently is not compatible with virtualenv_.  We recommend to create a dedicated
   Jython_ installation just for Windchill development.

Build Environment
-----------------

There's a sample build environment setup included in `setenv.sh`.  The example assumes the setup used at
nexiles for development.  To activate, *source* it into your development shell::

	$ cd nexiles.gateway.example
	$ . bin/activate
	(nexiles.gateway.example)$ . ./setenv.sh
	JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.7.0_60.jdk/Contents/Home
	JYTHON_HOME=/usr/local/opt/jython/libexec
	WT_HOME=/Users/seletz/develop/Windchill/WT_HOME_102
	IPYTHONDIR=/Users/seletz/develop/nexiles/nexiles.gateway.example/src/.ipython
	PYTHONUSERBASE=/Users/seletz/develop/nexiles/nexiles.gateway.example/src/local


Performing a build
------------------

:prerequisites: `build requirements`, `build environment`

To perform a full build, do::

	$ cd nexiles.gateway.example
	$ . bin/activate
	(nexiles.gateway.example)$ . ./setenv.sh
	...
	(nexiles.gateway.example)$ fab build
	Loading fabric env from fabric.json
	...
	Built eggs:
	   /Users/seletz/develop/nexiles/nexiles.gateway.example/build/nexiles.gateway.example-0.1.0-py2.7-nexiles.egg

	Done.

This will build the *nexiles.gateway.example** egg and this documentation.  The build artefacts are placed
in the `build/` directory.

.. _virtualenv: https://virtualenv.pypa.io/en/latest/
.. _there: https://skynet.nexiles.com/docs/nexiles.fabric.tasks/
.. _Fabric: http://www.fabfile.org/
.. _Jython: http://www.jython.org/
.. _Apple Mac: http://www.apple.com/mac/
.. _PTC Windchill: http://www.ptc-solutions.de/produkte/ptc-windchill/ptc-windchill-102.html
.. _us: mailto:info@nexiles.com?subject=nexiles.gateway%20request%20for%20information&cc=se@nexiles.de