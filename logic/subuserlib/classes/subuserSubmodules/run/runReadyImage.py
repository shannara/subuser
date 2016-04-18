# -*- coding: utf-8 -*-

"""
Contains code that prepairs a subuser's image to be run.
"""

#external imports
import os
#internal imports
from subuserlib.classes.userOwnedObject import UserOwnedObject

class RunReadyImage(UserOwnedObject):
  def __init__(self,user,subuser):
    self.__subuser = subuser
    self.__id = None
    UserOwnedObject.__init__(self,user)

  def setup(self):
    if not "run-ready-image-id" in self.getSubuser().getRuntimeCache():
      self.__id = self.build()
      self.getSubuser().getRuntimeCache()["run-ready-image-id"] = self.__id
      self.getSubuser().getRuntimeCache().save()

  def getSubuser(self):
    return self.__subuser

  def getId(self):
    if not self.__id:
      self.__id = self.getSubuser().getRuntimeCache()["run-ready-image-id"]
    return self.__id

  def generateImagePreparationDockerfile(self):
    """
    There is still some preparation that needs to be done before an image is ready to be run.  But this preparation requires run time information, so we cannot preform that preparation at build time.
    """
    dockerfileContents  = "FROM "+self.getSubuser().getImageId()+"\n"
    dockerfileContents += "RUN useradd --uid="+str(self.getUser().getEndUser().uid)+" "+self.getUser().getEndUser().name+" ;export exitstatus=$? ; if [ $exitstatus -eq 4 ] ; then echo uid exists ; elif [ $exitstatus -eq 9 ]; then echo username exists. ; else exit $exitstatus ; fi\n"
    dockerfileContents += "RUN test -d "+self.getUser().getEndUser().homeDir+" || mkdir "+self.getUser().getEndUser().homeDir+" && chown "+self.getUser().getEndUser().name+" "+self.getUser().getEndUser().homeDir+"\n"
    if self.getSubuser().getPermissions()["serial-devices"]:
      dockerfileContents += "RUN groupadd dialout; export exitstatus=$? ; if [ $exitstatus -eq 4 ] ; then echo gid exists ; elif [ $exitstatus -eq 9 ]; then echo groupname exists. ; else exit $exitstatus ; fi\n"
      dockerfileContents += "RUN groupadd uucp; export exitstatus=$? ; if [ $exitstatus -eq 4 ] ; then echo gid exists ; elif [ $exitstatus -eq 9 ]; then echo groupname exists. ; else exit $exitstatus ; fi\n"
      dockerfileContents += "RUN usermod -a -G dialout "+self.getUser().getEndUser().name+"\n"
      dockerfileContents += "RUN usermod -a -G uucp "+self.getUser().getEndUser().name+"\n"
    if self.getSubuser().getPermissions()["sudo"]:
      dockerfileContents += "RUN (umask 337; echo \""+self.getUser().getEndUser().name+" ALL=(ALL) NOPASSWD: ALL\" > /etc/sudoers.d/allowsudo )\n"
    return dockerfileContents

  def build(self):
    """
    Returns the Id of the Docker image to be run.
    """
    return self.getUser().getDockerDaemon().build(None,quietClient=True,useCache=True,forceRm=True,rm=True,dockerfile=self.generateImagePreparationDockerfile())
