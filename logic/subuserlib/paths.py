# -*- coding: utf-8 -*-

"""
Module used for determining non-user-configurable paths.
"""

#external imports
import os
import inspect
#internal imports
#import ...

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

def getSubuserDataFile(filename):
  dataFile = os.path.join(getSubuserDir(),"logic","subuserlib","data",filename)
  if os.path.exists(dataFile):
    return dataFile
  else:
    import pkg_resources
    dataFile = pkg_resources.resource_filename("subuserlib",os.path.join("data",filename))
    if not os.path.exists(dataFile):
      exit("Data file does not exist:"+str(dataFile))
    else:
      return dataFile

def getSubuserCommandsDir():
  """
  Return the path to the directory where the individual built-in subuser command executables are stored.
  """
  commandsDir = os.path.join(getSubuserDir(),"logic","subuserCommands")
  if os.path.exists(commandsDir):
    return commandsDir
  else:
    import pkg_resources
    commandsDir = pkg_resources.resource_filename("subuserlib",os.path.join("packagedCommands"))
    if not os.path.exists(commandsDir):
      exit("Commands dir does not exist: "+str(commandsDir))
    else:
      return commandsDir
