#项目：“现在鼠标在哪里？”
import pyautogui
print('Press Ctrl-C to quit.')
x, y = pyautogui.position()
positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
print(positionStr, end='')
print('\b' * len(positionStr), end='', flush=True)
