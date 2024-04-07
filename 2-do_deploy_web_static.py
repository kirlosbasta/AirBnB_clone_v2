#!/usr/bin/python3
'''Fabric script that distributes an archive to web servers,
using the function do_deploy'''
from fabric.api import *
from os.path import isdir, exists


env.hosts = ['100.25.19.62', '100.26.174.180']


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
        run('mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/'.format(filename_wex, filename_wex))
        run('rm -rf /tmp/{}'.format(filename))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(
            filename_wex))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.
            format(filename_wex))
        return True
    except Exception:
        return False
