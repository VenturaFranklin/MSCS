import subprocess
import yaml
import time
import atexit

manualFlag = True

settingFilePath = "/home/pi/MSCS/" # where the settings are located, this still needs to be checked
debugFlag = True
calibratePos = 27000 # temporary calibration position, substitute for a homeing switch
calibrateFlag = False
homePos = 23000 # position of slide right above rollers, in front of camera
upPos = 27000 # top most position of slide
downPos = 15000 # bottom most position of slide
calStepSize = 1000 # step size for manual calibration / homing
LAsettings = {
  "currentpos": 27000,
  "homepos": 23000,
  "uppos": 27000,
  "downpos": 15000,
} # dictionary for variable storage to file

def start():
  atexit.register(exit_handler)
  log("starting linear actuator")
  loadSettings()
  ticcmd("--exit-safe-start")
  ticcmd('--halt-and-set-position', str(LAsettings["currentpos"]))

def log(msg):
  if debugFlag:
    print(msg)

def ticcmd(*args):
  return subprocess.check_output(['ticcmd'] + list(args))

def gotoHome():
  goto(homePos)

def loadSettings():
  log("loading LA settings from file")
  ticcmd('--settings', settingFilePath + "tic_settings.txt")
  lasettings = settingFilePath + "LASettings.yaml"
  with open(lasettings, "r") as file:
      LAsettings = yaml.load(file, Loader=yaml.FullLoader)

def exit_handler():
  LAsettings["currentpos"] = pos
  lasettings = settingFilePath + "LASettings.yaml"
  with open(lasettings, "w") as file:
      LAsettings = yaml.dump(file, Loader=yaml.FullLoader)

# manually lowers the slide by a set step size, used to manually home the LA
def down():
  goto(getPos() - calStepSize) # this is addition because LA is mounted upside down

# manually raises the slide by a set step size, used to manually home the LA
def up():
  goto(getPos() + calStepSize) # this is subtraction because LA is mounted upside down

# goes to input position on the linear actuator, pos is int, returns when position is achieved
def goto(pos):
  ticcmd('--exit-safe-start', '--position', str(pos)) # execute ticcmd to goto
  LAsettings["currentpos"] = pos
  if manualFlag:
      time.sleep(3)
      ticcmd('--halt-and-set-position', str(pos))
      return
      
  while True: # wait loop to return only when the target position is achieved
    currentPosition = getPos()
    log("going to " + str(pos) + "currently at " + str(currentPosition))
    if currentPosition == pos:
      return
    time.sleep(0.1)

def getPos():
  if manualFlag:
      position = LAsettings["currentpos"]
  else:
      log("not manual")
      print(ticcmd('-s', '--full'))
      status = yaml.load(ticcmd('-s', '--full'))
      position = status['Current position']
  log("getPos " + str(position))
  return position
  
def oscClean():
    for i in range(4):
        goto(LAsettings["homepos"])
        goto(LAsettings["downpos"])
        goto(LAsettings["homepos"])
        
def oscDry():
    for i in range(1):
        goto(LAsettings["homepos"])
        goto(LAsettings["uppos"])
        goto(LAsettings["homepos"])

def gotoHome():
    goto(LAsettings["homepos"])

def gotoTop():
    goto(LAsettings["uppos"])
    
def calibrate():
  calibrateFlag = True
  LAsettings["currentpos"] = calibratePos
  ticcmd('--halt-and-set-position', str(calibratePos))



