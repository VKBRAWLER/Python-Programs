import pyautogui
 

# take screenshot using pyautogui
image = pyautogui.screenshot()
# this will return the image as PIL and
# store in `image`

# if you need to save the image as a
# file, pass the path of the file as
# an argument like this
image1 = pyautogui.screenshot("image2.jpg")