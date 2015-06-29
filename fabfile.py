import os
import sys

from fabric.api import env
from fabric.api import task
from fabric.api import local
from fabric.api import execute

from nexiles.fabric.tasks import log

log.setup_logging()

if not "WT_HOME" in os.environ:
    log.error("WT_HOME not set: Please read the documentation on build "
              "requisites and set-up.")
    sys.exit(10)

from nexiles.fabric.tasks import docs
from nexiles.fabric.tasks import utils
from nexiles.fabric.tasks import release
from nexiles.fabric.tasks import gateway
from nexiles.fabric.tasks import environment

env.nexiles.initialize()


@task
def version():
    """Print package version"""
    log.info("{} {}".format(env.nexiles.package_name, env.nexiles.version))


@task
def build():
    execute(docs.build)
    execute(docs.package)
    execute(gateway.build_eggs)


@task
def dist():
    execute(gateway.dist_eggs)
    execute(docs.dist)


@task
def full_monty():
    execute(build)
    execute(dist)
    # execute(release.github)

# EOF
