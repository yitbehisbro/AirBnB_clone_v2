#!/usr/bin/python3
""" Deploy archive to the both servers """
from datetime import datetime
import os
import shlex
from fabric.api import *


env.hosts = ['54.237.120.163', '52.91.101.243']
env.user = "ubuntu"

def do_deploy(archive_path):
    """ fab function to deploy archived file to the servers """
    if not os.path.exists(archive_path):
        return False
    try:
        filename1 = archive_path.replace('/', ' ')
        filename1 = shlex.split(filename1)
        filename1 = filename1[-1]

        filename2 = shlex.split(archive_path.replace('/', ' '))
        filename2 = shlex.split(filename2[1].replace('.', ' '))
        filename2 = filename2[0]

        releases_path = "/data/web_static/releases/{}/".format(filename2)
        tmp_path = "/tmp/{}".format(filename1)

        put(archive_path, "/tmp/", preserve_mode=True)
        run("mkdir -p {}".format(releases_path))
        run("tar -xzf {} -C {}".format(tmp_path, releases_path))
        run("rm {}".format(tmp_path))
        run("mv {}web_static/* {}".format(releases_path, releases_path))
        run("rm -rf {}web_static".format(releases_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(releases_path))
        print("New version deployed!")
        return True
    except Exception:
        return False
