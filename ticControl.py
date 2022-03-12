import subprocess
import yaml
import time
 
def ticcmd(*args):
  return subprocess.check_output(['ticcmd'] + list(args))
 
status = yaml.load(ticcmd('-s', '--full'))
 
position = status['Current position']
print("Current position is {}.".format(position))
 
new_target = -200 if position > 0 else 200
print("Setting target position to {}.".format(new_target))
ticcmd('--exit-safe-start', '--position', str(new_target))

def gotoHome():

def loadSettings():

def down(num):

def up(num):

def goto(pos):

def getPos():

def setHome():