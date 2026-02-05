# -*- coding: utf-8 -*-

"""
Module used for determining non-user-configurable paths.
"""

#external imports
import os
import inspect
try:
    import importlib.resources as importlib_resources
except ImportError:
    # For compatibility with older Python versions (< 3.7)
    import importlib_resources
#internal imports
import subuserlib.executablePath as executablePath

home = os.path.expanduser("~")

def upNDirsInPath(path,n):
  if n > 0:
    return os.path.dirname(upNDirsInPath(path,n-1))
  else:
    return path

def getSubuserDir():
  """
  Get the toplevel directory for subuser.
  """
  pathToThisSourceFile = os.path.abspath(inspect.getfile(inspect.currentframe()))
  return upNDirsInPath(pathToThisSourceFile,3)

def getSubuserExecutable():
  executable = os.path.join(getSubuserDir(),"logic","subuser")
  if not os.path.exists(executable):
    executable = executablePath.which("subuser")
  return executable

def getSubuserDataFile(filename):
  dataFile = os.path.join(getSubuserDir(),"logic","subuserlib","data",filename)
  if os.path.exists(dataFile):
    return dataFile
  else:
    ref = importlib_resources.files("subuserlib").joinpath("data", filename)
    if not ref.is_file():
      exit("Data file does not exist:"+str(dataFile))
    else:
      return str(ref)
