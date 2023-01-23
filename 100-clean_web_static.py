#!/usr/bin/python3
""" Keep it clean! """
from fabric.api import *


env.hosts = ['54.237.120.163', '52.91.101.243']
env.user = "ubuntu"


def do_clean(number=0):
    """ Removes unnecessary versions """

    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
