#!/usr/bin/python3
"""distributes an archive to your web servers"""

from fabric.operations import run, sudo, put
import os
from fabric.api import *
env.hosts = ['35.174.209.127', '34.234.201.37']


def do_deploy(archive_path):
    """distribute archive"""
    if os.path.isfile(archive_path) is False:
        return False
    try:
        zip = archive_path.split("/")[-1]
        path = "/data/web_static/releases"
        put("{}".format(archive_path), "/tmp/{}".format(zip))
        folder = zip.split(".")
        run("mkdir -p {}/{}/".format(path, folder[0]))
        new_archive = '.'.join(folder)
        run("tar -xzf /tmp/{} -C {}/{}/"
            .format(new_archive, path, folder[0]))
        run("rm /tmp/{}".format(zip))
        run("mv {}/{}/web_static/* {}/{}/"
            .format(path, folder[0], path, folder[0]))
        run("rm -rf {}/{}/web_static".format(path, folder[0]))
        run("rm -rf /data/web_static/current")
        run("ln -sf {}/{} /data/web_static/current"
            .format(path, folder[0]))
        return True
    except OSError:
        return False
