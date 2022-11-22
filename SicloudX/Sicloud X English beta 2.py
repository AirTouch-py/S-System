import time
import random
import math
from tkinter import *
from tkinter import messagebox
import webbrowser
import sys
import datetime
import threading
import socket
import calendar
while True:
    time.sleep(0.5)
    cmd=input("cmd:")
    if cmd=="help":
        print("""System instructions:
    Help: View all system instructions: View the system version
    encryption machine: Silicon® Encryptor
    decryptor: Silicon® Decrypting machine
    rock-paper-scissors:Rock-paper-scissors Game
    stopwatch: Sicloud system's own stopwatch
    open website: Open Web Site
    clock: check the current time
    PS: Web page image editor
    minesweeping: minesweeping games
    tic-tac-toe: tic tac toe game
    c: see small comics
    calendar: View Calendar
    IP: View the IP address and name of the computer
    Python: web Python programming environment
    bilibili: Open the Bilibili website
    calculators: calculators
    shutdown: Shutdown

System version:
Sicloud X
Silicon ® Copyright Limited
              """)
    elif cmd=="PS":
        webbrowser.open("https://ps.gaoding.com/#/")
    elif cmd=="Python":
        webbrowser.open("https://www.json.cn/runcode/run_python3/")
    elif cmd=="bilibili":
        webbrowser.open("https://www.bilibili.com")
    elif cmd=="Calculators":
        root = Tk()
        root.resizable(width=False, height=False)
        '''hypeparameter'''
        # 是否按下了运算符
        IS_CALC = False
        # 存储数字
        STORAGE = []
        # 显示框最多显示多少个字符
        MAXSHOWLEN = 18
        # 当前显示的数字
        CurrentShow =StringVar()
        CurrentShow.set('0')

        '''按下数字键(0-9)'''


        def pressNumber(number):
            global IS_CALC
            if IS_CALC:
                CurrentShow.set('0')
                IS_CALC = False
            if CurrentShow.get() == '0':
                CurrentShow.set(number)
            else:
                if len(CurrentShow.get()) < MAXSHOWLEN:
                    CurrentShow.set(CurrentShow.get() + number)


        '''按下小数点'''


        def pressDP():
            global IS_CALC
            if IS_CALC:
                CurrentShow.set('0')
                IS_CALC = False
            if len(CurrentShow.get().split('.')) == 1:
                if len(CurrentShow.get()) < MAXSHOWLEN:
                    CurrentShow.set(CurrentShow.get() + '.')


        '''清零'''


        def clearAll():
            global STORAGE
            global IS_CALC
            STORAGE.clear()
            IS_CALC = False
            CurrentShow.set('0')


        '''清除当前显示框内所有数字'''


        def clearCurrent():
            CurrentShow.set('0')


        '''删除显示框内最后一个数字'''


        def delOne():
            global IS_CALC
            if IS_CALC:
                CurrentShow.set('0')
                IS_CALC = False
            if CurrentShow.get() != '0':
                if len(CurrentShow.get()) > 1:
                    CurrentShow.set(CurrentShow.get()[:-1])
                else:
                    CurrentShow.set('0')


        '''计算答案修正'''


        def modifyResult(result):
            result = str(result)
            if len(result) > MAXSHOWLEN:
                if len(result.split('.')[0]) > MAXSHOWLEN:
                    result = 'Overflow'
                else:
                    # 直接舍去不考虑四舍五入问题
                    result = result[:MAXSHOWLEN]
            return result


        '''按下运算符'''


        def pressOperator(operator):
            global STORAGE
            global IS_CALC
            if operator == '+/-':
                if CurrentShow.get().startswith('-'):
                    CurrentShow.set(CurrentShow.get()[1:])
                else:
                    CurrentShow.set('-' + CurrentShow.get())
            elif operator == '1/x':
                try:
                    result = 1 / float(CurrentShow.get())
                except:
                    result = 'illegal operation'
                result = modifyResult(result)
                CurrentShow.set(result)
                IS_CALC = True
            elif operator == 'sqrt':
                try:
                    result = math.sqrt(float(CurrentShow.get()))
                except:
                    result = 'illegal operation'
                result = modifyResult(result)
                CurrentShow.set(result)
                IS_CALC = True
            elif operator == 'MC':
                STORAGE.clear()
            elif operator == 'MR':
                if IS_CALC:
                    CurrentShow.set('0')
                STORAGE.append(CurrentShow.get())
                expression = ''.join(STORAGE)
                try:
                    result = eval(expression)
                except:
                    result = 'illegal operation'
                result = modifyResult(result)
                CurrentShow.set(result)
                IS_CALC = True
            elif operator == 'MS':
                STORAGE.clear()
                STORAGE.append(CurrentShow.get())
            elif operator == 'M+':
                STORAGE.append(CurrentShow.get())
            elif operator == 'M-':
                if CurrentShow.get().startswith('-'):
                    STORAGE.append(CurrentShow.get())
                else:
                    STORAGE.append('-' + CurrentShow.get())
            elif operator in ['+', '-', '*', '/', '%']:
                STORAGE.append(CurrentShow.get())
                STORAGE.append(operator)
                IS_CALC = True
            elif operator == '=':
                if IS_CALC:
                    CurrentShow.set('0')
                STORAGE.append(CurrentShow.get())
                expression = ''.join(STORAGE)
                try:
                    result = eval(expression)
                # 除以0的情况
                except:
                    result = 'illegal operation'
                result = modifyResult(result)
                CurrentShow.set(result)
                STORAGE.clear()
                IS_CALC = True


        '''Demo'''


        def Demo():
            root.minsize(320, 420)
            root.title('Calculator')
            # 布局
            # --文本框
            label = Label(root, textvariable=CurrentShow, bg='black', anchor='e', bd=5, fg='white',
                                  font=('楷体', 20))
            label.place(x=20, y=50, width=280, height=50)
            # --第一行
            # ----Memory clear
            button1_1 = Button(text='MC', bg='#666', bd=2, command=lambda: pressOperator('MC'))
            button1_1.place(x=20, y=110, width=50, height=35)
            # ----Memory read
            button1_2 = Button(text='MR', bg='#666', bd=2, command=lambda: pressOperator('MR'))
            button1_2.place(x=77.5, y=110, width=50, height=35)
            # ----Memory save
            button1_3 = Button(text='MS', bg='#666', bd=2, command=lambda: pressOperator('MS'))
            button1_3.place(x=135, y=110, width=50, height=35)
            # ----Memory +
            button1_4 = Button(text='M+', bg='#666', bd=2, command=lambda: pressOperator('M+'))
            button1_4.place(x=192.5, y=110, width=50, height=35)
            # ----Memory -
            button1_5 = Button(text='M-', bg='#666', bd=2, command=lambda: pressOperator('M-'))
            button1_5.place(x=250, y=110, width=50, height=35)
            # --第二行
            # ----删除单个数字
            button2_1 = Button(text='del', bg='#666', bd=2, command=lambda: delOne())
            button2_1.place(x=20, y=155, width=50, height=35)
            # ----清除当前显示框内所有数字
            button2_2 = Button(text='CE', bg='#666', bd=2, command=lambda: clearCurrent())
            button2_2.place(x=77.5, y=155, width=50, height=35)
            # ----清零(相当于重启)
            button2_3 = Button(text='C', bg='#666', bd=2, command=lambda: clearAll())
            button2_3.place(x=135, y=155, width=50, height=35)
            # ----取反
            button2_4 = Button(text='+/-', bg='#666', bd=2, command=lambda: pressOperator('+/-'))
            button2_4.place(x=192.5, y=155, width=50, height=35)
            # ----开根号
            button2_5 = Button(text='sqrt', bg='#666', bd=2, command=lambda: pressOperator('sqrt'))
            button2_5.place(x=250, y=155, width=50, height=35)
            # --第三行
            # ----7
            button3_1 = Button(text='7', bg='#bbbbbb', bd=2, command=lambda: pressNumber('7'))
            button3_1.place(x=20, y=200, width=50, height=35)
            # ----8
            button3_2 = Button(text='8', bg='#bbbbbb', bd=2, command=lambda: pressNumber('8'))
            button3_2.place(x=77.5, y=200, width=50, height=35)
            # ----9
            button3_3 = Button(text='9', bg='#bbbbbb', bd=2, command=lambda: pressNumber('9'))
            button3_3.place(x=135, y=200, width=50, height=35)
            # ----除
            button3_4 = Button(text='/', bg='#708069', bd=2, command=lambda: pressOperator('/'))
            button3_4.place(x=192.5, y=200, width=50, height=35)
            # ----取余
            button3_5 = Button(text='%', bg='#708069', bd=2, command=lambda: pressOperator('%'))
            button3_5.place(x=250, y=200, width=50, height=35)
            # --第四行
            # ----4
            button4_1 = Button(text='4', bg='#bbbbbb', bd=2, command=lambda: pressNumber('4'))
            button4_1.place(x=20, y=245, width=50, height=35)
            # ----5
            button4_2 = Button(text='5', bg='#bbbbbb', bd=2, command=lambda: pressNumber('5'))
            button4_2.place(x=77.5, y=245, width=50, height=35)
            # ----6
            button4_3 = Button(text='6', bg='#bbbbbb', bd=2, command=lambda: pressNumber('6'))
            button4_3.place(x=135, y=245, width=50, height=35)
            # ----乘
            button4_4 = Button(text='*', bg='#708069', bd=2, command=lambda: pressOperator('*'))
            button4_4.place(x=192.5, y=245, width=50, height=35)
            # ----取导数
            button4_5 = Button(text='1/x', bg='#708069', bd=2, command=lambda: pressOperator('1/x'))
            button4_5.place(x=250, y=245, width=50, height=35)
            # --第五行
            # ----1
            button5_1 = Button(text='1', bg='#bbbbbb', bd=2, command=lambda: pressNumber('1'))
            button5_1.place(x=20, y=290, width=50, height=35)
            # ----2
            button5_2 = Button(text='2', bg='#bbbbbb', bd=2, command=lambda: pressNumber('2'))
            button5_2.place(x=77.5, y=290, width=50, height=35)
            # ----3
            button5_3 = Button(text='3', bg='#bbbbbb', bd=2, command=lambda: pressNumber('3'))
            button5_3.place(x=135, y=290, width=50, height=35)
            # ----减
            button5_4 = Button(text='-', bg='#708069', bd=2, command=lambda: pressOperator('-'))
            button5_4.place(x=192.5, y=290, width=50, height=35)
            # ----等于
            button5_5 = Button(text='=', bg='#708069', bd=2, command=lambda: pressOperator('='))
            button5_5.place(x=250, y=290, width=50, height=80)
            # --第六行
            # ----0
            button6_1 = Button(text='0', bg='#bbbbbb', bd=2, command=lambda: pressNumber('0'))
            button6_1.place(x=20, y=335, width=107.5, height=35)
            # ----小数点
            button6_2 = Button(text='.', bg='#bbbbbb', bd=2, command=lambda: pressDP())
            button6_2.place(x=135, y=335, width=50, height=35)
            # ----加
            button6_3 = Button(text='+', bg='#708069', bd=2, command=lambda: pressOperator('+'))
            button6_3.place(x=192.5, y=335, width=50, height=35)
            root.mainloop()


        if __name__ == '__main__':
            Demo()

    elif cmd=="shutdown":
        sys.exit()
    elif cmd=="clock":
        nowtime=datetime.datetime.today()
        now=nowtime.strftime("%Y-%m-%d %H:%M:%S")
        print("time:"+now)
    elif cmd=="open website":
        html=input("website：")
        if "http://www." in html or "https://www." in html:
            webbrowser.open(html)
        elif "https://www." not in html:
            webbrowser.open("https://www."+html)
        elif "www." in html and "https://www." not in html:
            webbrowser.open("https://" + html)
    elif cmd=="stopwatch":
        # 创建窗口
        from1 = Tk()
        # 窗口标题
        from1.title('Sicloud Stopwatch')
        # 窗口大小
        from1.minsize(400, 400)

        isloop = False  # 初始化按钮False为停止 True为开始
        var = StringVar()
        stopid = None  # 定义一个空值

        '''********* 计时函数 *********'''


        def gettime():
            global isloop
            global stopid
            global star
            global fo

            elap = time.time() - star  # 获取时间差

            if isinstance(stopid, float):
                a = stopid
                elap = elap + a
            minutes = int(elap / 60)  # 分钟
            seconds = int(elap - minutes * 60.0)  # 秒
            hseconds = int((elap - minutes * 60.0 - seconds) * 1000)  # 毫秒
            var.set('%02d:%02d:%03d' % (minutes, seconds, hseconds))

            if isloop == False:
                but1['text'] = 'next'
                stopid = elap  # 把暂停时的时间差赋给 stopid (有记忆)
                fo.write('%02d:%02d:%03d' % (minutes, seconds, hseconds) + "\n")  # 记录时间
                fo.close()  # 关闭文件
                return

            from1.after(1, gettime)  # 每隔1ms调用函数自身获取时间


        '''********* 开始\暂停按钮函数 **********'''


        def newtask():
            global isloop
            global star
            global fo
            if but1['text'] == 'start' or but1['text'] == 'continue': # 根据按钮的文本来判断是否开启循环
                if but1['text'] == 'start':
                    fo = open("time.txt", "a+")  # 开始时清楚上一次记录的内容
                else:
                    fo = open("time.txt", "a+")  # 追加暂停时的时间
                but1['text'] = 'stop'
                isloop = True
                star = time.time()  # 获取当前时间
                # 建立线程
                t = threading.Thread(target=gettime)
                # 开启线程
                t.start()
            else:
                isloop = False


        '''******* 清零按钮函数 ********'''


        def clearing():
            global isloop
            global stopid
            isloop = False  # 初始化按钮为停止
            stopid = None  # 定义一个空值
            var.set('00:00:000')
            but1['text'] = '开始'


        # 开始\暂停 按钮
        but1 = Button(from1, text='开始', command=newtask)
        but1.place(x=95, y=280, width=80, height=50)  # 按钮位置和大小
        # 重置按钮
        but2 = Button(from1, text='清零', command=clearing)
        but2.place(x=225, y=280, width=80, height=50)
        # # 显示时间
        var.set('00:00:000')  # 初始化时间
        lab1 = Label(from1, textvariable=var, font=("Arial Bold", 30), foreground="skyblue")
        lab1.place(x=110, y=150)

        # from1.overrideredirect(1) # 隐藏标题栏 最大化最小化按钮

        # 显示窗体
        from1.mainloop()
        #计时器时间记忆.txt
        print("Stopwatch results have been stored in the time.txt")

    elif cmd=="encryption machine":
        last = []
        string = input("Enter the content you want to encrypt:")
        for i in string:
            last.append(chr(ord(i) + 10))
        time.sleep(1)
        print("Encryption succeeded")
        time.sleep(0.5)
        print("The encrypted content is:{}".format("".join(last)))
    elif cmd== "decrypting machine":
        last = []
        string = input("Enter the content you want to decrypt (using Silicon ® Encrypted by encryptor):")
        for i in string:
            last.append(chr(ord(i) - 10))
        time.sleep(1)
        print("Decryption succeeded")
        time.sleep(0.5)
        print("The decrypted content is::{}".format("".join(last)))
    elif cmd=="Rock-paper-scissors":
        choices = ["rock", "paper", "scissors"]
        computer = random.choice(choices)
        player = False
        cpu_score = 0
        player_score = 0
        while True:
            player = input("rock,paper or scissors (enter 'End' to end)").capitalize()
            # 判断游戏者和电脑的选择
            if player == computer:
                print("it ends in a draw!")
            elif player == "rock":
                if computer == "paper":
                    print("You lost!", computer, "covers", player)
                    cpu_score += 1
                else:
                    print("You win!", player, "smashes", computer)
                    player_score += 1
            elif player == "paper":
                if computer == "scissors":
                    print("You lost!", computer, "cut", player)
                    cpu_score += 1
                else:
                    print("You win!", player, "covers", computer)
                    player_score += 1
            elif player == "scissors":
                if computer == "rock":
                    print("You lost!", computer, "smashes", player)
                    cpu_score += 1
                else:
                    print("You win!", player, "cut", computer)
                    player_score += 1
            elif player == 'end':
                print("——————Final score——————")
                print(f"computer:{cpu_score}")
                print(f"player:{player_score}")
                break
            else:
                print("Input error, please check the input!!")
            computer = random.choice(choices)
    elif cmd=="IP":
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        print(f"Hostname: {hostname}")
        print(f"IP_Address: {ip_address}")
    elif cmd=="calendar":
        try:
            year = int(input("Enter Year:"))
        except Exception as e:
            print("error:{}".format(e))
        try:
            month = int(input("Enter Month:"))
        except Exception as e:
            print("error:{}".format(e))
        print(calendar.month(year, month))
    elif cmd=="tic-tac-toe":
        def drawBoard(board):
            # 打印棋盘

            # "board"是长度为10的列表，为了方便输入，忽略第一个元素board[0]

            print('\n\n\n\n')
            print('\t\t\t┌─┬─┬─┐')
            print('\t\t\t│' + board[7] + ' │' + board[8] + ' │' + board[9] + ' │')
            print('\t\t\t├─┼─┼─┤')
            print('\t\t\t│' + board[4] + ' │' + board[5] + ' │' + board[6] + ' │')
            print('\t\t\t├─┼─┼─┤')
            print('\t\t\t│' + board[1] + ' │' + board[2] + ' │' + board[3] + ' │')
            print('\t\t\t└─┴─┴─┘')


        def inputPlayerLetter():
            # 让玩家选择棋子
            # 返回一个列表，第一个是玩家的棋子，第二个是电脑的
            letter = ''
            while not (letter == 'X' or letter == 'O'):
                print('Do you want to be X or O?')
                letter = input().upper()

            if letter == 'X':
                return ['X', 'O']
            else:
                return ['O', 'X']


        def whoGoesFirst():
            # 随机产生谁先走
            if random.randint(0, 1) == 0:
                return 'computer'
            else:
                return 'player'


        def playAgain():
            # 再玩一次？输入yes或y返回True
            print('Do you want to play again? (yes or no)')
            return input().lower().startswith('y')


        def makeMove(board, letter, move):
            # 落子
            board[move] = letter


        def isWinner(bo, le):
            # 判断所给的棋子是否获胜
            # 参数为棋盘上的棋子（列表）和棋子符号
            # 以下是所有可能胜利的情况，共8种
            return ((bo[7] == le and bo[8] == le and bo[9] == le) or
                    (bo[4] == le and bo[5] == le and bo[6] == le) or
                    (bo[1] == le and bo[2] == le and bo[3] == le) or
                    (bo[7] == le and bo[4] == le and bo[1] == le) or
                    (bo[8] == le and bo[5] == le and bo[2] == le) or
                    (bo[9] == le and bo[6] == le and bo[3] == le) or
                    (bo[7] == le and bo[5] == le and bo[3] == le) or
                    (bo[9] == le and bo[5] == le and bo[1] == le))


        def getBoardCopy(board):
            # 复制一份棋盘，供电脑落子时使用
            dupeBoard = []

            for i in board:
                dupeBoard.append(i)

            return dupeBoard


        def isSpaceFree(board, move):
            # 判断这个位置是否有子，没子返回True
            return board[move] == ' '


        def getPlayerMove(board):
            # 玩家落子
            move = ' '
            while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
                print('What is your next move? (1-9)')
                move = input()
            return int(move)


        def chooseRandomMoveFromList(board, movesList):
            # 随机返回一个可以落子的坐标
            # 如果没有所给的movesList中没有可以落子的，返回None
            possibleMoves = []
            for i in movesList:
                if isSpaceFree(board, i):
                    possibleMoves.append(i)

            if len(possibleMoves) != 0:
                return random.choice(possibleMoves)
            else:
                return None


        def getComputerMove(board, computerLetter):
            # 确定电脑的落子位置
            if computerLetter == 'X':
                playerLetter = 'O'
            else:
                playerLetter = 'X'

            # Tic Tac Toe AI核心算法:
            # 首先判断电脑方能否通过一次落子直接获得游戏胜利
            for i in range(1, 10):
                copy = getBoardCopy(board)
                if isSpaceFree(copy, i):
                    makeMove(copy, computerLetter, i)
                    if isWinner(copy, computerLetter):
                        return i

            # 判断玩家下一次落子能否获得胜利，如果能，给它堵上
            for i in range(1, 10):
                copy = getBoardCopy(board)
                if isSpaceFree(copy, i):
                    makeMove(copy, playerLetter, i)
                    if isWinner(copy, playerLetter):
                        return i

            # 如果角上能落子的话，在角上落子
            move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
            if move != None:
                return move

            # 如果能在中心落子的话，在中心落子
            if isSpaceFree(board, 5):
                return 5

            # 在边上落子
            return chooseRandomMoveFromList(board, [2, 4, 6, 8])


        def isBoardFull(board):
            # 如果棋盘满了，返回True
            for i in range(1, 10):
                if isSpaceFree(board, i):
                    return False
            return True


        print('Welcome to Tic Tac Toe!')

        while True:
            # 更新棋盘
            theBoard = [' '] * 10
            playerLetter, computerLetter = inputPlayerLetter()
            turn = whoGoesFirst()
            print('The ' + turn + ' will go first.')
            gameIsPlaying = True

            while gameIsPlaying:
                if turn == 'player':
                    # 玩家回合
                    drawBoard(theBoard)
                    move = getPlayerMove(theBoard)
                    makeMove(theBoard, playerLetter, move)

                    if isWinner(theBoard, playerLetter):
                        drawBoard(theBoard)
                        print('Hooray! You have won the game!')
                        gameIsPlaying = False
                    else:
                        if isBoardFull(theBoard):
                            drawBoard(theBoard)
                            print('The game is a tie!')
                            break
                        else:
                            turn = 'computer'


                else:
                    # 电脑回合
                    move = getComputerMove(theBoard, computerLetter)
                    makeMove(theBoard, computerLetter, move)

                    if isWinner(theBoard, computerLetter):
                        drawBoard(theBoard)
                        print('The computer has beaten you! You lose.')
                        gameIsPlaying = False
                    else:
                        if isBoardFull(theBoard):
                            drawBoard(theBoard)
                            print('The game is a tie!')
                            break
                        else:
                            turn = 'player'

            if not playAgain():
                break
    elif cmd=="cartoon":
        import antigravity
    elif cmd=="minesweeper":
        # 定义五个二维数组，充当整个程序的数据
        control_list = [[0 for i in range(16)] for j in range(16)]  # 二维列表,呈现雷和数字的分布。
        show_list = [[0 for i in range(16)] for j in range(16)]  # 二维列表，控制遮住或显示雷和数字。(0--遮住，1--显示)
        button_list = [[0 for i in range(16)] for j in range(16)]  # 二维的按钮列表（显示在上层）
        label_list = [[0 for i in range(16)] for j in range(16)]  # 二维的标签列表（显示在下层）
        mark_list = [[0 for i in range(16)] for j in range(16)]  # 二维标记列表
        num_mine = 40  # 控制游戏结束
        counter = 0  # 计时
        T, t = 1, 0  # 游戏结束的判断


        def randomization(c_list):  # 随机初始化雷的分布即初始化列表control_list
            num = 0
            while num < 40:
                x = random.randint(0, 15)
                y = random.randint(0, 15)
                if (c_list[x][y] == 0):
                    num += 1
                    c_list[x][y] = -1
            for i in range(16):
                for j in range(16):
                    if (c_list[i][j] > -1):
                        if (i > 0 and c_list[i - 1][j] == -1):
                            c_list[i][j] += 1
                        if (i < 15 and c_list[i + 1][j] == -1):
                            c_list[i][j] += 1
                        if (j > 0 and c_list[i][j - 1] == -1):
                            c_list[i][j] += 1
                        if (j < 15 and c_list[i][j + 1] == -1):
                            c_list[i][j] += 1
                        if (i > 0 and j > 0 and c_list[i - 1][j - 1] == -1):
                            c_list[i][j] += 1
                        if (i < 15 and j < 15 and c_list[i + 1][j + 1] == -1):
                            c_list[i][j] += 1
                        if (i > 0 and j < 15 and c_list[i - 1][j + 1] == -1):
                            c_list[i][j] += 1
                        if (i < 15 and j > 0 and c_list[i + 1][j - 1] == -1):
                            c_list[i][j] += 1


        def game_core():
            randomization(control_list)
            for row in range(16):
                for col in range(16):
                    if (control_list[row][col] == -1):
                        label_list[row][col] = Label(root, text="☠", font=('arial', 15, 'bold'), fg="black",
                                                     bg="#AAAAAA", relief=RIDGE)
                        label_list[row][col].place(x=17 + col * 20, y=46 + row * 20, height=20, width=20)
                    elif (control_list[row][col] == 0):
                        label_list[row][col] = Label(root, text="", bg="#AAAAAA", relief=RIDGE)
                        label_list[row][col].place(x=17 + col * 20, y=46 + row * 20, height=20, width=20)
                    elif (control_list[row][col] == 1):
                        label_list[row][col] = Label(root, text="1", font=('arial', 15, 'bold'), fg="red", bg="#AAAAAA",
                                                     relief=RIDGE)
                        label_list[row][col].place(x=17 + col * 20, y=46 + row * 20, height=20, width=20)
                    elif (control_list[row][col] == 2):
                        label_list[row][col] = Label(root, text="2", font=('arial', 15, 'bold'), fg="blue",
                                                     bg="#AAAAAA", relief=RIDGE)
                        label_list[row][col].place(x=17 + col * 20, y=46 + row * 20, height=20, width=20)
                    elif (control_list[row][col] == 3):
                        label_list[row][col] = Label(root, text="3", font=('arial', 15, 'bold'), fg="green",
                                                     bg="#AAAAAA", relief=RIDGE)
                        label_list[row][col].place(x=17 + col * 20, y=46 + row * 20, height=20, width=20)
                    elif (control_list[row][col] == 4):
                        label_list[row][col] = Label(root, text="4", font=('arial', 15, 'bold'), fg="white",
                                                     bg="#AAAAAA", relief=RIDGE)
                        label_list[row][col].place(x=17 + col * 20, y=46 + row * 20, height=20, width=20)
                    elif (control_list[row][col] == 5):
                        label_list[row][col] = Label(root, text="5", font=('arial', 15, 'bold'), fg="red", bg="#AAAAAA",
                                                     relief=RIDGE)
                        label_list[row][col].place(x=17 + col * 20, y=46 + row * 20, height=20, width=20)
                    elif (control_list[row][col] == 6):
                        label_list[row][col] = Label(root, text="6", font=('arial', 15, 'bold'), fg="blue",
                                                     bg="#AAAAAA", relief=RIDGE)
                        label_list[row][col].place(x=17 + col * 20, y=46 + row * 20, height=20, width=20)
                    elif (control_list[row][col] == 7):
                        label_list[row][col] = Label(root, text="7", font=('arial', 15, 'bold'), fg="green",
                                                     bg="#AAAAAA", relief=RIDGE)
                        label_list[row][col].place(x=17 + col * 20, y=46 + row * 20, height=20, width=20)
                    elif (control_list[row][col] == 8):
                        label_list[row][col] = Label(root, text="8", font=('arial', 15, 'bold'), fg="white",
                                                     bg="#AAAAAA", relief=RIDGE)
                        label_list[row][col].place(x=17 + col * 20, y=46 + row * 20, height=20, width=20)
            for r in range(16):
                for c in range(16):
                    s = str((r) * 16 + c)
                    button_list[r][c] = Button(root, text=s, activeforeground="#AAAAAA", bg="#AAAAAA", fg="#AAAAAA")
                    button_list[r][c].place(x=17 + c * 20, y=46 + r * 20, height=20, width=20)
                    button_list[r][c].bind("<Button-1>", button_control_l)  # 鼠标左击绑定函数
                    button_list[r][c].bind("<Button-3>", button_control_r)


        def button_control_l(event):  # 扫雷控制函数.(开始函数直接用参数r和c，但是会产生问题)
            r = int(event.widget["text"]) // 16
            c = int(event.widget["text"]) % 16
            global t
            global T
            if (control_list[r][c] >= 1):
                button_list[r][c].place_forget()
                show_list[r][c] = 1
                t += 1
            elif (control_list[r][c] == 0):
                rec(r, c)
            elif (control_list[r][c] == -1 and T):
                button_list[r][c].place_forget()
                show_list[r][c] = 1
                T = 0
                for i in range(16):
                    for j in range(16):
                        if (control_list[i][j] == -1):
                            button_list[i][j].place_forget()
                            show_list[r][c] = 1
                button_restart["text"] = "again"
                messagebox.showwarning("NO", "YOU DIED!")
            if t == 216:
                T = 0
                messagebox.showwarning("YES", "YOU ARE BEST")


        def button_control_r(event):
            r = int(event.widget["text"]) // 16
            c = int(event.widget["text"]) % 16
            mark_list[r][c] = Button(root, text="？", font=('楷体', 14), activeforeground="#AAAAAA", bg="#AAAAAA",
                                     fg="yellow")
            mark_list[r][c].place(x=17 + c * 20, y=46 + r * 20, height=20, width=20)
            mark_list[r][c].bind("<Button-3>", button_control_r_change)


        def button_control_r_change(event):
            global num_mine
            if (event.widget["text"] == "？" and num_mine > 0):
                num_mine -= 1
                event.widget["text"] = "▲"
                cout_label["text"] = str(num_mine)
            elif (event.widget["text"] == "▲"):
                num_mine += 1
                cout_label["text"] = str(num_mine)
                event.widget.place_forget()
            elif (event.widget["text"] == "?" and num_mine == 0):
                event.widget.place_forget()


        def rec(r, c):  # 递归探测
            global t
            if control_list[r][c] > 0 and show_list[r][c] == 0:
                button_list[r][c].place_forget()
                show_list[r][c] = 1
                t += 1
                return 0
            elif control_list[r][c] == 0 and show_list[r][c] == 0:
                button_list[r][c].place_forget()
                show_list[r][c] = 1
                t += 1
                if r > 0 and c > 0:
                    rec(r - 1, c - 1)
                if r > 0:
                    rec(r - 1, c)
                if r > 0 and c < 15:
                    rec(r - 1, c + 1)
                if c < 15:
                    rec(r, c + 1)
                if r < 15 and c < 15:
                    rec(r + 1, c + 1)
                if r < 15:
                    rec(r + 1, c)
                if r < 15 and c > 0:
                    rec(r + 1, c - 1)
                if c > 0:
                    rec(r, c - 1)


        def time_counter(la):  # la是标签，计时函数
            def counting():
                global counter
                if T:
                    counter += 1
                la["text"] = str(counter)
                la.after(1000, counting)  # 在1000毫秒后执行counting()函数,即循环执行counting

            counting()


        def restart():  # 重新开始函数
            button_restart["text"] = "again"
            cout_label["text"] = "40"
            # 数据重置
            for i in range(16):
                for j in range(16):
                    control_list[i][j] = 0
                    show_list[i][j] = 0
                    button_list[i][j].place_forget()
                    button_list[i][j] = 0
                    label_list[i][j].place_forget()
                    label_list[i][j] = 0
                    if (mark_list[i][j] != 0):
                        mark_list[i][j].place_forget()
                    mark_list[i][j] = 0
            global num_mine
            global counter
            global T, t
            num_mine = 40
            counter = 0
            T, t = 1, 0
            game_core()


        if __name__ == "__main__":
            root = Tk()  # 根窗体
            root.title("minesweeper")
            root.geometry("360x410")  # 根窗体大小
            cv1 = Canvas(root, bd=15, bg="#FFFFFF", relief=RIDGE, cursor="cross", width=321, height=350)
            cv1.create_line(15, 45, 337, 45)
            cv1.place(x=0, y=0)
            w = Label(root, text="With every step, you can die!", font=("楷体", 12))
            w.place(x=60, y=385)
            button_restart = Button(root, text="new", font=('楷体', 15), bg="#AAAAAA", fg="blue", command=restart)
            button_restart.place(x=150, y=17, height=27, width=27)
            time_label = Label(root, bg="black", fg="red", text=str(counter), font=("LcdD", 15))  # 计时标签
            time_label.place(x=285, y=17, height=27, width=50)
            cout_label = Label(root, bg="black", fg="red", text="40", font=("LcdD", 20))  # 计数标签
            cout_label.place(x=18, y=17, height=27, width=27)
            game_core()
            time_counter(time_label)
            root.mainloop()  # 监控组件，组件发生变化或触发事件时，更新窗口
    else:
        print("Error does not have this directive")
        
    
        











