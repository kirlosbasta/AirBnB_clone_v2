#!/usr/bin/python3
'''Fabric script that distributes an archive to web servers,
using the function do_deploy'''
from datetime import datetime
from fabric.api import local
from os.path import isdir, exists


env.hosts = ['100.25.19.62', '100.26.174.180']


def do_pack():
    """archive from the contents of the web_static folder of
    AirBnB Clone repo"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception:
        return None


def do_deploy(archive_path):
    '''deploy an archive to web server'''
    if exists(archive_path) is False:
        return False
    filename = archive_path.split('/')[-1]
    filename_wex = filename.partition('.')[0]
    try:
        put(archive_path, '/tmp/')
        run('mkdir -p /data/web_static/releases/{}'.format(
            filename_wex
        ))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(
            filename, filename_wex))
        run('rm -rf /tmp/{}'.format(filename))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.
            format(filename_wex))
        return True
    except Exception:
        return False
