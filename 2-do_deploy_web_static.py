#!/usr/bin/python3
'''Fabric script that distributes an archive to web servers,
using the function do_deploy'''
from fabric.api import *
from os.path import exists


env.hosts = ['100.25.19.62', '100.26.174.180']


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    compressedFile = archive_path.split("/")[-1]
    fileName = compressedFile.split(".")[0]
    upload_path = "/tmp/{}".format(compressedFile)
    if put(archive_path, upload_path).failed:
        return False
    current_release = '/data/web_static/releases/{}'.format(fileName)
    if run("rm -rf {}".format(current_release)).failed:
        return False
    if run("mkdir -p {}".format(current_release)).failed:
        return False
    uncompress = "tar -xzf /tmp/{} -C {}".format(
        compressedFile, current_release
    )
    if run(uncompress).failed:
        return False
    delete_archive = "rm -f /tmp/{}".format(compressedFile)
    if run(delete_archive).failed:
        return False
    if run("rm -rf /data/web_static/current").failed:
        return False
    relink = "ln -s {} /data/web_static/current".format(current_release)
    if run(relink).failed:
        return False
    return True
