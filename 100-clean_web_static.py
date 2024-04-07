#!/usr/bin/python3
# del outdated.
import os
from fabric.api import *
env.hosts = ["35.174.209.127", "34.234.201.37"]


def do_clean(number=0):
    """archives

    Args:
        number (int): number of the archives

    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
