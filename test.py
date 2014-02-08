# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import glob
import os
import sys
import shutil

screenshot_path = "glove_test/screenshots";

if len(sys.argv) != 2:
	print "[Glove-test] Incorrect argument"
	exit()

country = sys.argv[1]

device = MonkeyRunner.waitForConnection()
print "[Glove-test] start testing ("+country+")"
print "[Glove-test] connected device"
screen_width = int(device.getProperty("display.width"))
screen_height = int(device.getProperty("display.height"))
device_id = device.getSystemProperty("build.ID")
print "[Glove-test] device ID: " + str(device_id)
print "[Glove-test] screen resolution: " + str(screen_width) + " * " + str(screen_height)

# Installs the Android package. Notice that this method returns a boolean, so you can test
# to see if the installation worked.
device.installPackage('glove_test/glove'+country+'.apk')
print "[Glove-test] install package"
package = 'com.glove'
activity = 'com.glove.activity.RoutingActivity'
runComponent = package + '/' + activity

device.startActivity(component=runComponent)
MonkeyRunner.sleep(4)

# === Tutorial
def tutorial():
	result = device.takeSnapshot()
	result.writeToFile(screenshot_path+'/tut_0.png','png')
	print "[Screenshot] tut_0"
	MonkeyRunner.sleep(1)
	for num in range(1,6):
		device.drag(((screen_width)*2/3, screen_height/2),(screen_width/3,screen_height/2),0.15,5)
		print "[Action] swipe"
		MonkeyRunner.sleep(1)
		result = device.takeSnapshot()
		result.writeToFile(screenshot_path+'/tut_' + str(num) + '.png','png')
		print "[Screenshot] tut_" + str(num)
		MonkeyRunner.sleep(1)

# ===  Nap
def nap_email():
	device.touch(screen_width/2, screen_height-10, 'DOWN_AND_UP')
	print "[Action] click GET STARTED button"
	MonkeyRunner.sleep(2)
	device.press('KEYCODE_DPAD_RIGHT', MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(0.5)
	device.press('KEYCODE_DPAD_RIGHT', MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(0.5)
	device.press('KEYCODE_ENTER', MonkeyDevice.DOWN_AND_UP)
	print "[Action] click 'Accept'"
	MonkeyRunner.sleep(2)
	result = device.takeSnapshot()
	result.writeToFile(screenshot_path+'/nap_email_0.png','png')
	print "[Screenshot] nap_email_0"
	MonkeyRunner.sleep(2)
	device.type('yjlo123@qq.com')
	print "[Action] type email"
	MonkeyRunner.sleep(2)

	device.touch(screen_width/2, screen_height-10, 'DOWN_AND_UP')
	print "[Action] click button"
	MonkeyRunner.sleep(2)
	result = device.takeSnapshot()
	result.writeToFile(screenshot_path+'/nap_email_1.png','png')
	print "[Screenshot] nap_email_1"
	MonkeyRunner.sleep(2)

def nap_num():
	MonkeyRunner.sleep(2)
	result = device.takeSnapshot()
	result.writeToFile(screenshot_path+'/nap_num_0.png','png')
	print "[Screenshot] nap_num_0"

	MonkeyRunner.sleep(1)
	device.type('123123')
	print "[Action] type number"
	MonkeyRunner.sleep(2)
	device.touch(screen_width/2, screen_height-10, 'DOWN_AND_UP')
	print "[Action] click button"
	MonkeyRunner.sleep(2)
	result = device.takeSnapshot()
	result.writeToFile(screenshot_path+'/nap_num_1.png','png')
	print "[Screenshot] nap_num_1"

# === Result
def wait_for_result(time):
	while time != 0:
		print "[Action] waiting for result... " + str(time)
		MonkeyRunner.sleep(5)
		time -= 5

def result(number_of_results):
	result = device.takeSnapshot()
	result.writeToFile(screenshot_path+'/result_1.png','png')
	print "[Screenshot] result_1"

	for num in range(2,number_of_results+1):
		device.drag(((screen_width)*2/3, screen_height/2),((screen_width)/3,screen_height/2),0.15,5)
		print "[Action] swipe"
		MonkeyRunner.sleep(1)
		result = device.takeSnapshot()
		result.writeToFile(screenshot_path+'/result_' + str(num) + '.png','png')
		print "[Screenshot] result_" + str(num)
		MonkeyRunner.sleep(1)

# swipe back
def swipe_back(number):
	for n in range(0,number):
		device.drag((screen_width/3, screen_height/2),((screen_width)*2/3,screen_height/2),0.15,5)
		print "[Action] swipe"
		MonkeyRunner.sleep(1)

# ===how
def how():
	device.press('KEYCODE_MENU', MonkeyDevice.DOWN_AND_UP)
	device.press('KEYCODE_DPAD_UP', MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(0.5)
	device.press('KEYCODE_DPAD_UP', MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(0.5)
	device.press('KEYCODE_DPAD_DOWN', MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(0.5)
	device.press('KEYCODE_ENTER', MonkeyDevice.DOWN_AND_UP)
	print "[Action] click 'How it works?' button"
	MonkeyRunner.sleep(0.5)
	device.touch(screen_width/2, screen_height/2, 'DOWN_AND_UP')
	MonkeyRunner.sleep(0.5)
	result = device.takeSnapshot()
	result.writeToFile(screenshot_path+'/how.png','png')
	print "[Screenshot] how"
	MonkeyRunner.sleep(1)
	device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(0.5)
	device.touch(screen_width/2, screen_height-10, 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)

# ===click offer
def offer():
	device.touch(screen_width/2, screen_height-10, 'DOWN_AND_UP')
	print "[Action] click GET AN OFFER"
	MonkeyRunner.sleep(1)
	device.type('123123')
	device.press('KEYCODE_DPAD_DOWN', MonkeyDevice.DOWN_AND_UP)
	device.press('KEYCODE_DPAD_RIGHT', MonkeyDevice.DOWN_AND_UP)
	device.press('KEYCODE_ENTER', MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(5)
	result = device.takeSnapshot()
	result.writeToFile(screenshot_path+'/result_offer.png','png')
	print "[Screenshot] result_offer"
	MonkeyRunner.sleep(1)
	device.touch(screen_width/2, screen_height-10, 'DOWN_AND_UP')
	print "[Action] click REPRESENTATIVE button"
	MonkeyRunner.sleep(2)
	result = device.takeSnapshot()
	result.writeToFile(screenshot_path+'/result_offer_disabled.png','png')
	print "[Screenshot] result_offer_disabled"

# ===info & price
def left_btn(name):
	for num in range(1,5):
		device.press('KEYCODE_DPAD_RIGHT', MonkeyDevice.DOWN_AND_UP)
		MonkeyRunner.sleep(0.2)

	device.press('KEYCODE_DPAD_DOWN', MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(0.5)
	device.press('KEYCODE_DPAD_LEFT', MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(0.5)
	device.press('KEYCODE_ENTER', MonkeyDevice.DOWN_AND_UP)
	print "[Action] click "+name+" button"
	MonkeyRunner.sleep(0.5)
	device.touch(screen_width/2, screen_height/2, 'DOWN_AND_UP')
	MonkeyRunner.sleep(0.5)
	result = device.takeSnapshot()
	result.writeToFile(screenshot_path+'/'+name+'.png','png')
	print "[Screenshot] "+name
	MonkeyRunner.sleep(1)
	device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(0.5)

def right_btn(name):
	for num in range(1,5):
		device.press('KEYCODE_DPAD_RIGHT', MonkeyDevice.DOWN_AND_UP)
		MonkeyRunner.sleep(0.2)
	device.press('KEYCODE_DPAD_DOWN', MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(0.5)
	device.press('KEYCODE_ENTER', MonkeyDevice.DOWN_AND_UP)
	print "[Action] click "+name+" button"
	MonkeyRunner.sleep(0.5)
	device.touch(screen_width/2, screen_height/2, 'DOWN_AND_UP')
	MonkeyRunner.sleep(0.5)
	result = device.takeSnapshot()
	result.writeToFile(screenshot_path+'/'+name+'.png','png')
	print "[Screenshot] "+name
	MonkeyRunner.sleep(1)
	device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(1)

if country == "IL":
	tutorial()
	nap_email()
	nap_num()
	wait_for_result(30)
	result(5)
	swipe_back(2)
	how()
	offer()
	left_btn("info")
	right_btn("price")
elif country == "US":
	tutorial()
	nap_email()
	wait_for_result(35)
	result(4)
	swipe_back(2)
	how()
	right_btn("info")
else:
	print "[Glove-test] Invalid country"


# ===uninstall package
device.removePackage (package)
print "[Glove-test] remove package"

dst = screenshot_path+"/"+str(screen_width)+" "+str(screen_height)
os.makedirs(dst)

for pngfile in glob.iglob(os.path.join(screenshot_path, "*.png")):
    shutil.move(pngfile, dst)
data = open(dst+'/data.txt', 'w')
data.write("country="+country)
data.closed
print "[Glove-test] finished"
