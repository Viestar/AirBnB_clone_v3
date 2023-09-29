#!/usr/bin/python3``
""" Fabric script that generates .tgz archive"""

from fabric.decorators import runs_once
from fabric.api import local
from datetime import datetime


@runs_once
def do_pack():
    """generates .tgz archive """
    local("mkdir -p versions")
    archive = ("versions/web_static_{}.tgz"
               .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))
    result = local("tar -cvzf {} web_static/".format(archive))

    if result.succeeded:
        return archive
    return None
