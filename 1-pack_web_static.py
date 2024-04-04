#!/usr/bin/python3
""" Fabric script that generates a .tgz"""
from datetime import datetime
from fabric.api import *


def do_pack():
    """ archive from the contents of the web_static"""
    time = datetime.now().strftime('%Y%m%d%H%M%S')
    name = "versions/web_static_{}.tgz".format(time)
    try:
        local("mkdir -p ./versions")
        local("tar --create --verbose -z --file={} ./web_static"
              .format(name))
        return name
    except NotADirectoryError:
        return None
