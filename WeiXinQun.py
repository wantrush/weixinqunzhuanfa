import pyautogui
import time

time.sleep(10)
#休眠10秒 方便摆放窗口位置 微信程序靠在窗口左上角 打开需要转发的聊天窗口

old_screen = pyautogui.screenshot('old_screen.png',region=(320,85, 300, 50))
new_screen = pyautogui.screenshot('new_screen.png',region=(320,85, 300, 50))
#分别截取两次屏幕 针对聊天窗口区域 便于后期侦测聊天窗口内容变化

i = 1
#赋值i 为的是执行LOG里面的计数器

#整体循环
while True:
    if old_screen != new_screen:
        #当两次截图不一致时 运行转发点击
        while True:
            file_pos = pyautogui.locateOnScreen('1.png', confidence=0.9)
            #"1.png"文件为鼠标点击位置获取截图      
            # print(file_pos)
            if file_pos == None:
                #如果未找到截图位置 则继续查找 以免程序后面赋值出错
                continue
            else:
                #如果找到截图位置 则将位置中心点赋值 并输出LOG
                goto_pos = pyautogui.center(file_pos)
                # print(goto_pos)
                print("取得区域，并成功赋值"+str(i))
                i += 1
                break
        #鼠标移动到截图位置中心点 并相对移动到文字框中 点击右键
        pyautogui.moveTo(goto_pos,duration=0.2)
        pyautogui.moveRel(0,-20,duration=0.2)
        # pyautogui.moveTo(388,345,duration=0.2)
        pyautogui.rightClick()
        # pyautogui.moveRel(40,120,duration=0.2)
        #"4.png"为多选截图
        file4_pos = pyautogui.locateOnScreen('4.png', confidence=0.9)
        if file4_pos == None:
            #某些文件在下载过程中 右键点击是不会出现“多选”选项的 这里需要做出判断 如果没有 则重新查找
            pyautogui.moveRel(0,200,duration=0.2)
            pyautogui.leftClick()
            new_screen = pyautogui.screenshot('new_screen.png',region=(320,85, 300, 50))
            old_screen = pyautogui.screenshot('old_screen.png',region=(320,85, 300, 50))
            continue#这里会跳转到哪里我自己也看不懂 但它能工作
        else:
            goto4_pos = pyautogui.center(file4_pos)#找到“多选”选项，并将中心点位置 赋值
            pyautogui.moveTo(goto4_pos,duration=0.2)
            pyautogui.leftClick()#点击中心点位置
            # pyautogui.moveRel(125,-30,duration=0.2)
            file5_pos = pyautogui.locateOnScreen('5.png', confidence=0.9)#"5.png"截图为合并发送选项
            if file5_pos == None:#判断是否找到
                continue
            else:
                goto5_pos = pyautogui.center(file5_pos)#赋值并左击合并发送选项
                pyautogui.moveTo(goto5_pos,duration=0.2)
                pyautogui.leftClick()
                file6_pos = pyautogui.locateOnScreen('6.png', confidence=0.9)#"6.png"为某些情况下会出现的错误提示 确认按钮
                if file6_pos != None:#如果出现了报错确认按钮 则点击它 并重置循环
                    goto6_pos = pyautogui.center(file6_pos)
                    pyautogui.moveTo(goto6_pos,duration=0.2)
                    pyautogui.leftClick()
                    pyautogui.moveTo(943,391,duration=0.2)
                    pyautogui.leftClick()
                    # time.sleep(10)
                    continue
                else:
                    file2_pos = pyautogui.locateOnScreen('2.png', confidence=0.9)#"2.png"为转发的目标群截图
                    goto2_pos = pyautogui.center(file2_pos)
                    pyautogui.moveTo(goto2_pos,duration=0.2)
                    pyautogui.leftClick()
                    file3_pos = pyautogui.locateOnScreen('3.png', confidence=0.9)#"3.png"为发送按钮 结束程序
                    goto3_pos = pyautogui.center(file3_pos)
                    pyautogui.moveTo(goto3_pos,duration=0.2)
                    pyautogui.leftClick()

                    new_screen = pyautogui.screenshot('new_screen.png',region=(320,85, 300, 50))
                    old_screen = pyautogui.screenshot('old_screen.png',region=(320,85, 300, 50))
    else:
        new_screen = pyautogui.screenshot('new_screen.png',region=(320,85, 300, 50))
        continue