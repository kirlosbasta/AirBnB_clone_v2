#!/usr/bin/python3
'''Fabric script that distributes an archive to web servers,
using the function do_deploy'''
from datetime import datetime
from fabric.api import *
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
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        file = archive_path.split("/")[-1]
        file_noEx = file.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run("rm -rf {}{}".format(path, file_noEx))
        sudo('mkdir -p {}{}/'.format(path, file_noEx))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file, path, file_noEx))
        run('rm /tmp/{}'.format(file))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, file_noEx))
        run('rm -rf {}{}/web_static'.format(path, file_noEx))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, file_noEx))
        return True
    except Exception:
        return False
