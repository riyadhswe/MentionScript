import pyautogui, time
time.sleep(5)
f = open("script", 'r')
for word in f:
    pyautogui.press('@')
    pyautogui.typewrite(word)
    pyautogui.press("enter")
