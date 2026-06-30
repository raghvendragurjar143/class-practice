
# time.sleep(5)
# c=datetime.now().strftime("%A %d-%B-%y, %H:%M:%S")
# print(c)from datetime import datetime
# import time



# ##apne app curcer chlega jaha bhi rakhnge 
import pyautogui
import time
time.sleep(4)
pyautogui.typewrite("hello how are you",interval=0.05)
for i in range(10):
    
    print(pyautogui.typewrite("hello how are you",interval=0.05))