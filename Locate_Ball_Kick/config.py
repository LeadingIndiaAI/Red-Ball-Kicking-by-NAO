import os
import sys
import motion
from naoqi import *
import almath
IP = "192.168.43.11"
PORT = 9559
if (IP == ""):
  print "IP address not defined, aborting"
  print "Please define it in " + __file__
  exit(1)
def loadProxy(pName):
  print "---------------------"
  print "Loading proxy"
  print "---------------------"
  proxy = ALProxy(pName, IP, PORT)
  print "---------------------"
  print "Starting " + pName + " Tests"
  print "---------------------"
  return proxy
def StiffnessOn(proxy):
  pNames = "Body"
  pStiffnessLists = 1.0
  pTimeLists = 1.0
  proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)
def StiffnessOff(proxy):
  pNames = "Body"
  pStiffnessLists = 0.0
  pTimeLists = 1.0
  proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)
def PoseInit(proxy, pMaxSpeedFraction = 0.2):
  HeadYawAngle       = 0
  HeadPitchAngle     = 0
  ShoulderPitchAngle = 80
  ShoulderRollAngle  = 20
  ElbowYawAngle      = -80
  ElbowRollAngle     = -60
  WristYawAngle      = 0
  HandAngle          = 0
  HipYawPitchAngle   = 0
  HipRollAngle       = 0
  HipPitchAngle      = -20
  KneePitchAngle     = 40
  AnklePitchAngle    = -20
  AnkleRollAngle     = 0
  robotConfig = proxy.getRobotConfig()
  robotName = ""
  for i in range(len(robotConfig[0])):
    if (robotConfig[0][i] == "Model Type"):
      robotName = robotConfig[1][i]
  if (robotName == "naoH25") or\
     (robotName == "naoAcademics"):
      Head     = [HeadYawAngle, HeadPitchAngle]
      LeftArm  = [ShoulderPitchAngle, +ShoulderRollAngle, +ElbowYawAngle, +ElbowRollAngle, WristYawAngle, HandAngle]
      RightArm = [ShoulderPitchAngle, -ShoulderRollAngle, -ElbowYawAngle, -ElbowRollAngle, WristYawAngle, HandAngle]
      LeftLeg  = [HipYawPitchAngle, +HipRollAngle, HipPitchAngle, KneePitchAngle, AnklePitchAngle, +AnkleRollAngle]
      RightLeg = [HipYawPitchAngle, -HipRollAngle, HipPitchAngle, KneePitchAngle, AnklePitchAngle, -AnkleRollAngle]
  elif (robotName == "naoH21") or\
       (robotName == "naoRobocup"):
      Head     = [HeadYawAngle, HeadPitchAngle]
      LeftArm  = [ShoulderPitchAngle, +ShoulderRollAngle, +ElbowYawAngle, +ElbowRollAngle]
      RightArm = [ShoulderPitchAngle, -ShoulderRollAngle, -ElbowYawAngle, -ElbowRollAngle]
      LeftLeg  = [HipYawPitchAngle, +HipRollAngle, HipPitchAngle, KneePitchAngle, AnklePitchAngle, +AnkleRollAngle]
      RightLeg = [HipYawPitchAngle, -HipRollAngle, HipPitchAngle, KneePitchAngle, AnklePitchAngle, -AnkleRollAngle]
  elif (robotName == "naoT14"):
      Head     = [HeadYawAngle, HeadPitchAngle]
      LeftArm  = [ShoulderPitchAngle, +ShoulderRollAngle, +ElbowYawAngle, +ElbowRollAngle, WristYawAngle, HandAngle]
      RightArm = [ShoulderPitchAngle, -ShoulderRollAngle, -ElbowYawAngle, -ElbowRollAngle, WristYawAngle, HandAngle]
      LeftLeg  = []
      RightLeg = []
  elif (robotName == "naoT2"):
      Head     = [HeadYawAngle, HeadPitchAngle]
      LeftArm  = []
      RightArm = []
      LeftLeg  = []
      RightLeg = []
  pTargetAngles = Head + LeftArm + LeftLeg + RightLeg + RightArm
  pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
  pNames = "Body"
  proxy.angleInterpolationWithSpeed(pNames, pTargetAngles, pMaxSpeedFraction)
def poseZero(proxy):
  pNames = "Body"
  numBodies = len(proxy.getJointNames(pNames))
  pTargetAngles = [0.0] * numBodies
  pMaxSpeedFraction = 0.3
  proxy.angleInterpolationWithSpeed(pNames, pTargetAngles, pMaxSpeedFraction)
