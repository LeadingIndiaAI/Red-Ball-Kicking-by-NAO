# Project Title

Tracking and Kicking of a Ball by Nao Robot

## Introduction

In this project we are programming Nao, a humanoid robot to kick a ball to a goal post. The robot first detects the ball using its camera then walk towards it, adjusts itself and finally kicks the ball.

### Prerequisites

Set of tools deployed
OS: Windows 10
Softwares: Choregraphe, Python, Pynaoqi-SDK, JRE, Eclipse (or any Python Development IDE)
Python Libraries: Opencv, Numpy, Pillow
For eclipse to run we need to have Windows, JRE and Eclipse trio in either x86 or x64 version.


### Installing

1) Softwares
 a) Choregraphe: A tool to control and monitor Nao and Pepper Robot. We have used Choregraphe 2.8.5.10 which can be downloaded from Softbanks Robotics website.
 b) Python: We need to install python x86 version as Pynaoqi-SDK is available in x86 version for Windows platform. While installinf pyhton we have to check the option     to use python as environment variable
 c) Pynaoqi-SDK: A python library used for programming Nao. Its x86 version can be downloaded from Softbank website.
 d) JRE: JRE is Java Runtime Environment which is a prerequisite for Eclipse and is not needed for python IDEs. We have used jre-8u211-windows-x64 can downloaded from 	    Oracle websites
 e) Eclipse: For configuring Eclipse to use python we need to download eclipse-committers-neon-R-win32-x86_64. For configuring it we followed the instructions on          https://www.ics.uci.edu/~pattis/common/handouts/pythoneclipsejava/eclipsepython%20neon.html	
2) Libraries
 All requied python libraries can be installed using Command Prompt using the command without inverted commas "PYTHON_PATH\Scripts\pip.exe install opencv-python"  (Where PYTHON_PATH is the  path to the Python installation directory, for example C:\Python27 )

## Description of the files

adjust_left: 
ball:
config: 
connection:
find_ball:
find_goal:
goal:
kick:
kick_left:
kick_right:
kick-alt:
main:
take_postion:
vision_definitions:
vision_getandsaveimage:


## Running the tests

Explain how to run the automated tests for this system

## Deployment

Add additional notes about how to deploy this on a live system

## Acknowledgments

We thank Dr. Tapas Badal for floating this project. And Bennett University and leadingindia.ai for this opportunity.
Lovish and Rahul, Penalty Shootout by Aldebran NAO https://cse.iitk.ac.in/users/cs365/2013/submissions/~lovishc/cs365/project/index.html