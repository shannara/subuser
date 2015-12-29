#!/usr/bin/python3
# -*- coding: utf-8 -*-

try:
  import pathConfig
except ImportError:
  pass
#external imports
import sys
import optparse
#internal imports
from subuserlib.classes.user import User
import subuserlib.verify
import subuserlib.commandLineArguments
import subuserlib.profile
from subuserlib.classes.permissionsAccepters.acceptPermissionsAtCLI import AcceptPermissionsAtCLI

####################################################
def parseCliArgs(realArgs):
  usage = "usage: subuser repair [options]"
  description = """
Repair your subuser installation.

This is usefull when migrating from one machine to another.  You can copy your ~/.subuser folder to the new machine and run repair, and things should just work.
"""
  parser = optparse.OptionParser(usage=usage,description=description,formatter=subuserlib.commandLineArguments.HelpFormatterThatDoesntReformatDescription())
  parser.add_option("--accept",dest="accept",action="store_true",default=False,help="Acceppt permissions without asking.")
  parser.add_option("--prompt",dest="prompt",action="store_true",default=False,help="Prompt before installing new images.")
  return parser.parse_args(args=realArgs)

@subuserlib.profile.do_cprofile
def verify(realArgs):
  options,arguments=parseCliArgs(realArgs)
  user = User()
  permissionsAccepter = AcceptPermissionsAtCLI(user,alwaysAccept = options.accept)
  with user.getRegistry().getLock() as LockFileHandle:
    subuserNames = list(user.getRegistry().getSubusers().keys())
    subuserNames.sort()
    subuserlib.verify.verify(user,subuserNames=subuserNames,permissionsAccepter=permissionsAccepter,prompt=options.prompt)
    user.getRegistry().commit()

if __name__ == "__main__":
  verify(sys.argv[1:])
