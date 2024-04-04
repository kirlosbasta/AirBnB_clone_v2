#!/usr/bin/python3
'''Fabric script that generates a .tgz archive from the contents
of the web_static folder of AirBnB Clone repo'''
from fabric.api import *
from datetime import datetime
from os.path import abspath


def do_pack():
    '''generates a .tgz archive from the contents of the web_static folder'''
    now = datetime.now().strftime('%Y%m%d%H%M%S')
    local('mkdir versions')
    local(f'tar -cfavz ./versions/web_static_{now}.tgz web_static')
    return abspath('versions/web_static_{now}.tgz')
