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

    try:
        if os.path.exists(archive_path):
            put(archive_path, remote="/tmp/", preserve_mode=True)
            filename = shlex.split(archive_path.replace('/', ' '))
            filename = shlex.split(name[1].replace('.', ' '))
            filename = name[0]
            release = "data/web_static/releases/"

            run('mkdir -p /{}{}/'.format(release, filename))
            run('tar -xzf /tmp/{}.tgz -C /{}'.format(filename, release))
            run('rm /tmp/{}.tgz'.format(filename))
            o = "/{}{}/web_static/*".format(release, filename)
            n = "/{}{}/".format(filename)
            run('mv {} {}'.format(o, n))
            run('rm -rf {}/web_static'.format(n))
            run('rm -rf /data/web_static/current')
            run('ln -s {} /data/web_static/current'.format(n))
            print("New version deployed!")
            return True
        else:
            return False
    except Exception:
        return False
