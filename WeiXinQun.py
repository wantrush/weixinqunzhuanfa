import pyautogui
import time

# time.sleep(10)
old_screen = pyautogui.screenshot('old_screen.png',region=(320,85, 500, 300))
new_screen = pyautogui.screenshot('new_screen.png',region=(320,85, 200, 300))
i = 1
while True:
    if old_screen != new_screen:
        
        while True:
            file_pos = pyautogui.locateOnScreen('1.png', confidence=0.9)
            
            # print(file_pos)
            if file_pos == None:
                
                # print("未找到匹配区域"+str(i)+"次,继续搜索")
                # i += 1
                continue

            else:
                goto_pos = pyautogui.center(file_pos)
                # print(goto_pos)
                print("取得区域，并成功赋值"+str(i))
                i += 1
                break
        pyautogui.moveTo(goto_pos,duration=0.2)
        pyautogui.moveRel(0,-20,duration=0.2)
        # pyautogui.moveTo(388,345,duration=0.2)
        pyautogui.rightClick()
        # pyautogui.moveRel(40,120,duration=0.2)
        file4_pos = pyautogui.locateOnScreen('4.png', confidence=0.9)
        if file4_pos == None:
            pyautogui.moveRel(0,200,duration=0.2)
            pyautogui.leftClick()
            new_screen = pyautogui.screenshot('new_screen.png',region=(320,85, 200, 300))
            old_screen = pyautogui.screenshot('old_screen.png',region=(320,85, 200, 300))
            continue
        else:
            goto4_pos = pyautogui.center(file4_pos)
            pyautogui.moveTo(goto4_pos,duration=0.2)
            pyautogui.leftClick()
            # pyautogui.moveRel(125,-30,duration=0.2)
            file5_pos = pyautogui.locateOnScreen('5.png', confidence=0.9)
            if file5_pos == None:
                continue
            else:
                goto5_pos = pyautogui.center(file5_pos)
                pyautogui.moveTo(goto5_pos,duration=0.2)
                pyautogui.leftClick()
                file6_pos = pyautogui.locateOnScreen('6.png', confidence=0.9)
                if file6_pos != None:
                    goto6_pos = pyautogui.center(file6_pos)
                    pyautogui.moveTo(goto6_pos,duration=0.2)
                    pyautogui.leftClick()
                    pyautogui.moveTo(943,391,duration=0.2)
                    pyautogui.leftClick()
                    # time.sleep(10)
                    continue
                else:

                    file2_pos = pyautogui.locateOnScreen('2.png', confidence=0.9)
                    goto2_pos = pyautogui.center(file2_pos)
                    pyautogui.moveTo(goto2_pos,duration=0.2)
                    pyautogui.leftClick()
                    file3_pos = pyautogui.locateOnScreen('3.png', confidence=0.9)
                    goto3_pos = pyautogui.center(file3_pos)
                    pyautogui.moveTo(goto3_pos,duration=0.2)
                    pyautogui.leftClick()

                    new_screen = pyautogui.screenshot('new_screen.png',region=(320,85, 200, 300))
                    old_screen = pyautogui.screenshot('old_screen.png',region=(320,85, 200, 300))
    else:
        new_screen = pyautogui.screenshot('new_screen.png',region=(320,85, 200, 300))
        continue