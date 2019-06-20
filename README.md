# Final code for Redball Kicking By Humanoid Robot Nao 
# Project Title

Tracking and Kicking of a Ball by Nao Robot

## Introduction

In this project we are programming Nao, a humanoid robot to kick a ball to a goal post. The robot first detects the ball using its camera then walk towards it, adjusts itself and finally kicks the ball.

### Prerequisites

Set of tools deployed
1) For Windows 
  OS: Windows 10
  Softwares: Choregraphe, Python, Pynaoqi-SDK, JRE, Eclipse (or any Python Development IDE)
  Python Libraries: Opencv, Numpy, Pillow
2) For Ubuntu
  OS: Ubuntu 16.04 versions (no other version of Ubuntu works for Choregraphe for linux)
  Software: Choregraphe, Pynaoqi-SDK
  Pyhthon Libraries: Opencv, Numpy, Pillow
  
### Installing
1) For Windows
  A) Softwares
   a) Choregraphe: A tool to control and monitor Nao and Pepper Robot. We have used Choregraphe 2.8.5.10 which can be downloaded from Softbanks Robotics website.
   b) Python: We need to install python x86 version as Pynaoqi-SDK is available in x86 version for Windows platform. While installing pyhton we have to check the option to use python as environment variable.
   c) Pynaoqi-SDK: A python library used for programming Nao. Its x86 version can be downloaded from Softbank website.
   d) JRE: JRE is Java Runtime Environment which is a prerequisite for Eclipse and is not needed for python IDEs. We have used jre-8u211-windows-x64 can downloaded from Oracle websites
   e) Eclipse: For configuring Eclipse to use python we need to download eclipse-committers-neon-R-win32-x86_64. For configuring it we followed the instructions on https://www.ics.uci.edu/~pattis/common/handouts/pythoneclipsejava/eclipsepython%20neon.html	
  B) All requied python libraries can be installed using Command Prompt using the command without inverted commas "PYTHON_PATH\Scripts\pip.exe install opencv-python". (Where PYTHON_PATH is the  path to the Python installation directory, for example C:\Python27 )
2) For Ubuntu 16.04
  A) Softwares
     a) Choregraphe.run file is available from Softbank's site. Just change the permission of this file in properties to "run the file as executable file" and intall it just double clicking like any other normal software.
     b) Pynaoqi can be downloaded from Softbank Robotics Website either x86 or x64 according to your needs and extracted to a known location. Later we have to give its path as environment variable in bashsrc file. Type in terminal without inverted commas "sudo gedit ~/.bashrc" and add this line without inverted commas " export PYTHONPATH=${PYTHONPATH}:address". (Where address is the path to the location where you have extracted pynaoqi, for exaample /home/Downloads/pynaoqi-python-2.7-naoqi-2.1.4-linux64)
  B) All requires All requied python libraries can be installed using termianl using these two commands one by one 1) sudo apt-get install python-pip 2) sudo pip install opencv-python

## Description of the files

Locate_Ball_Kick: Codes for making NAO kick redball present anywhere (maximum distace of 1.5 m) in frontal hemispherical plane of NAO.
Penalty_Kick: Codes for making NAO kick redball kick redball kept in front to the goal post, all in line (maximum distance inbetween NAO and goal canot be more than 2 m)

## Addition Deployment Notes
1) Windows
  a) For eclipse to run we need to have Windows, JRE and Eclipse trio in either x86 or x64 version
  b) We need to manually add two file given in this link -- https://www.robotlab.com/support/choregraphe-bin.exe-system-error-fix
2) Ubuntu
  In our case adding address of pynaoqi didn't work because of some error So, we linked used Choregraphe's naoqi. We logged in to ubuntu as root user (very risky, if want to do it do it at your own risk) and went to opt folder renamed the folder Softbank Robotics to Softbank. And the further entered in and changed the name of Choregraphe 2.8.5.10 to Choregraphe. Finally, add the address of site-pachages folder as path as we did above for pynaoqi. In this case address would be similar to /opt/Softbank/Choregraphe/Lib/python2.7/site-packages. 

## Acknowledgments

We thank Dr. Tapas Badal for floating this project and Bennett University and leadingindia.ai for providing us all the necessary resources, suitable place and time for doing the project. Last and but the least Lovish and Rahul for the source code reference https://cse.iitk.ac.in/users/cs365/2013/submissions/~lovishc/cs365/project/index.html


