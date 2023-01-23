#!/usr/bin/python3
""" Compress before sending web_static folder """
from datetime import datetime
from fabric.api import local
import os


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
