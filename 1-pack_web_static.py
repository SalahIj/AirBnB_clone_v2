#!/usr/bin/python3
""" Fabric script  """
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """ The function def  """
    try:
        local("mkdir -p versions")
        now = datetime.now()
        date_time = now.strftime("%Y%m%d%H%M%S")
        archive_name = "web_static_{}.tgz".format(date_time)
        local("tar -cvzf versions/{} web_static".format(archive_name))
        archive_path = "versions/{}".format(archive_name)
        if os.path.exists(archive_path):
            return archive_path
        else:
            return None

    except Exception as e:
        return None
