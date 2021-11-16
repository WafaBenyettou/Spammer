import pyautogui, time
time.sleep(10)

pyautogui.click()

for word in range(20):
    pyautogui.write('hello its wafa')
    pyautogui.press('ENTER')
    time.sleep(0.3)

