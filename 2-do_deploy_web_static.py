#!/usr/bin/python3
""" Deploy archive to the both servers """
from datetime import datetime
import os
from fabric.api import *


env.hosts = ['54.237.120.163', '52.91.101.243']
env.user = "ubuntu"

def do_pack():
    """ fab function to create a tar file """
    try:
        if not os.path.exists("versions"):
            local('mkdir versions')
        t = datetime.now()
        f = "%Y%m%d%H%M%S"
        archived_file = 'versions/web_static_{}.tgz'.format(t.strftime(f))
        local('tar -cvzf {} web_static'.format(archived_file))
        return archived_file
    except Exception:
        return None

def do_deploy(archive_path):
    """ fab function to deploy archived file to the servers """
    
    try:
        if os.path.exists(archive_path):
            put(archive_path, remote="/tmp/", preserve_mode=True)
            path_name = run('export FILENAME={}'.format(archive_path))
            filename = run('echo $FILENAME | grep -o web_static_..............')
            run('mkdir -p /data/web_static/releases/{}/'.format(filename))
            run('tar -xzf /tmp/{}.tgz -C /data/web_static/releases/'.format(filename))
            run('rm /tmp/{}.tgz'.format(filename))
            o = "/data/web_static/releases/{}/web_static/*".format(filename)
            n = "/data/web_static/releases/{}/".format(filename)
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
