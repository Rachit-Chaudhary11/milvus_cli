from Connection import MilvusConnection
from Database import MilvusDatabase
from pymilvus import __version__
from Types import ParameterException

def getPackageVersion():
    import pkg_resources  # part of setuptools
    try:
        version = pkg_resources.require("milvus_cli")[0].version
    except Exception as e:
        raise ParameterException(
            "Could not get version under single executable file mode.")
    return version

class MilvusCli(object):
  connection = MilvusConnection()
  database = MilvusDatabase()


