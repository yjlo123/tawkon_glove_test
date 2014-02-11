from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import os
import glob
import shutil

package = 'com.glove'
screenshot_path = "glove_test/screenshots"

print "[Glove-test] cleaning..."
'''
shutil.rmtree('glove_test/screenshots')
if not os.path.exists("glove_test/screenshots"):
    os.makedirs("glove_test/screenshots")
'''
for pngfile in glob.iglob(os.path.join(screenshot_path, "*.png")):
    os.remove(pngfile)

print "[Glove-test] deleted screenshots"

print "[Glove-test] waiting for device..."
device = MonkeyRunner.waitForConnection()
print "[Glove-test] connected device"
device.removePackage (package)
print "[Glove-test] remove package"

print "[Glove-test] finished"