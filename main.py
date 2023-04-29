import os
import sys
import random
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import pygame
import os
import te
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *


class DesktopPet(QWidget):
    def __init__(self, parent=None, **kwargs):
        super(DesktopPet, self).__init__(parent)
        # 窗体初始化
        self.init()
        # 托盘化初始
        self.initPall()
        # 宠物静态gif图加载
        self.initPetImage()
        # 宠物正常待机，实现随机切换动作
        self.petNormalAction()

    # 窗体初始化
    def init(self):
        # 初始化
        # 设置窗口属性:窗口无标题栏且固定在最前面
        # FrameWindowHint:无边框窗口
        # WindowStaysOnTopHint: 窗口总显示在最上面
        # SubWindow: 新窗口部件是一个子窗口，而无论窗口部件是否有父窗口部件
        # https://blog.csdn.net/kaida1234/article/details/79863146
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.SubWindow)
        # setAutoFillBackground(True)表示的是自动填充背景,False为透明背景
        self.setAutoFillBackground(False)
        # 窗口透明，窗体空间不透明
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.any = 0

        # 重绘组件、刷新
        self.repaint()
        # self.child_window = window()

    # 托盘化设置初始化
    def initPall(self):
        # 导入准备在托盘化显示上使用的图标
        icons = os.path.join('klee/1.jpg')
        # 设置右键显示最小化的菜单项
        # 菜单项退出，点击后调用quit函数
        quit_action = QAction('退出', self, triggered=self.quit)
        # 设置这个点击选项的图片
        quit_action.setIcon(QIcon(icons))
        # 菜单项显示，点击后调用showing函数
        showing = QAction(u'显示', self, triggered=self.showwin)
        vo = QAction(u'可莉语音包', self, triggered=self.showChi)
        img = QAction(u'截屏', self, triggered=self.jie)
        pycharm = QAction(u'打开pycharm', self, triggered=self.pycharm)
        # 新建一个菜单项控件
        self.tray_icon_menu = QMenu(self)
        # 在菜单栏添加一个无子菜单的菜单项‘退出’
        self.tray_icon_menu.addAction(quit_action)
        # 在菜单栏添加一个无子菜单的菜单项‘显示’
        self.tray_icon_menu.addAction(showing)
        self.tray_icon_menu.addAction(vo)
        self.tray_icon_menu.addAction(img)
        self.tray_icon_menu.addAction(pycharm)
        # QSystemTrayIcon类为应用程序在系统托盘中提供一个图标
        self.tray_icon = QSystemTrayIcon(self)
        # 设置托盘化图标
        self.tray_icon.setIcon(QIcon(icons))
        # 设置托盘化菜单项
        self.tray_icon.setContextMenu(self.tray_icon_menu)

        # 展示
        self.tray_icon.show()

    def pycharm(self):
        self.openfile(r'D:\PyCharm 2020.3\bin\pycharm64.exe')


    # 宠物静态gif图加载
    def initPetImage(self):
        # 对话框定义
        self.talkLabel = QLabel(self)
        # 对话框样式设计
        self.talkLabel.setStyleSheet("font:15pt '楷体';border-width: 1px;color:blue;")
        # 定义显示图片部分
        self.image = QLabel(self)
        # QMovie是一个可以存放动态视频的类，一般是配合QLabel使用的,可以用来存放GIF动态图
        self.movie = QMovie("dudu.png")
        # 设置标签大小
        self.movie.setScaledSize(QSize(300, 300))
        # 将Qmovie在定义的image中显示
        self.image.setMovie(self.movie)
        self.movie.start()
        self.resize(1024, 1024)
        # 调用自定义的randomPosition，会使得宠物出现位置随机
        self.randomPosition()
        # 展示
        self.show()
        # https://new.qq.com/rain/a/20211014a002rs00
        # 将宠物正常待机状态的动图放入pet1中
        self.pet1 = ['dudu.png']
        # for i in os.listdir("klee/normal"):
        #     self.pet1.append("klee/normal/" + i)
        # 将宠物正常待机状态的对话放入pet2中
        self.dialog = []
        # 读取目录下dialog文件
        with open("dialog.txt", "r",encoding='utf8') as f:
            text = f.read()
            # 以\n 即换行符为分隔符，分割放进dialog中
            self.dialog = text.split("\n")

    # 宠物正常待机动作
    def petNormalAction(self):
        # 每隔一段时间做个动作
        # 定时器设置
        self.timer = QTimer()
        # 时间到了自动执行
        self.timer.timeout.connect(self.randomAct)
        # 动作时间切换设置
        self.timer.start(3000)
        # 宠物状态设置为正常
        self.condition = 0
        # 每隔一段时间切换对话
        self.talkTimer = QTimer()
        self.talkTimer.timeout.connect(self.talk)
        self.talkTimer.start(3000)
        # 对话状态设置为常态
        self.talk_condition = 0
        # 宠物对话框
        self.talk()

    # 随机动作切换
    def randomAct(self):

        if not self.any:

        # condition记录宠物状态，宠物状态为0时，代表正常待机
            if not self.condition:
                # 随机选择装载在pet1里面的gif图进行展示，实现随机切换
                self.movie = QMovie(random.choice(self.pet1))
                # 宠物大小
                self.movie.setScaledSize(QSize(200, 200))
                # 将动画添加到label中
                self.image.setMovie(self.movie)
                # 开始播放动画
                self.movie.start()
            # condition不为0，转为切换特有的动作，实现宠物的点击反馈
            # 这里可以通过else-if语句往下拓展做更多的交互功能
            else:
                # 读取特殊状态图片路径
                self.movie = QMovie("./klee/2.gif")
                # 宠物大小
                self.movie.setScaledSize(QSize(200, 200))
                # 将动画添加到label中
                self.image.setMovie(self.movie)
                # 开始播放动画
                self.movie.start()
                # 宠物状态设置为正常待机
                self.condition = 0
                self.talk_condition = 0
        else:
            self.change()


    #切换阿尼亚
    def change(self):
        self.any = 1
        self.movie = QMovie("./any/img.png")
        # 宠物大小
        self.movie.setScaledSize(QSize(200, 200))
        # 将动画添加到label中
        self.image.setMovie(self.movie)
        # 开始播放动画
        self.movie.start()
        # # 宠物状态设置为正常待机
        # self.condition = 0
        # self.talk_condition = 0


    #键盘监听
    def keyPressEvent(self, event) -> None:
        if event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_Q:
            #Control+q被按下
            self.jie()
        if event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_P:
            #Control+p被按下
            self.pycharm()
    # 宠物对话框行为处理
    def talk(self):

        if not self.any:


            if not self.talk_condition:
                # talk_condition为0则选取加载在dialog中的语句
                self.talkLabel.setText(random.choice(self.dialog))
                # 设置样式
                self.talkLabel.setStyleSheet(
                    "font: bold;"
                    "font:25pt '楷体';"
                    "color:black;"
                    "background-color: black"
                    "url(:/)"
                )
                # 根据内容自适应大小
                self.talkLabel.adjustSize()
            else:
                # talk_condition为1显示为别点我，这里同样可以通过if-else-if来拓展对应的行为
                self.talkLabel.setText("嘿嘿嘿，小可莉好喜欢你呀")
                self.talkLabel.setStyleSheet(
                    "font: bold;"
                    "font:25pt '楷体';"
                    "color:black;"
                    "background-color: black"
                    "url(:/)"
                )
                self.talkLabel.adjustSize()
                # 设置为正常状态
                self.talk_condition = 0
        else:
            self.talkLabel.setText("嘿嘿嘿，阿尼亚好喜欢嘟嘟呀")
            self.talkLabel.setStyleSheet(
                "font: bold;"
                "font:25pt '楷体';"
                "color:black;"
                "background-color: black"
                "url(:/)"
            )
            self.talkLabel.adjustSize()
            # 设置为正常状态
            self.talk_condition = 0

    # 退出操作，关闭程序
    def quit(self):
        self.close()
        sys.exit()

    # 显示宠物
    def showwin(self):
        # setWindowOpacity（）设置窗体的透明度，通过调整窗体透明度实现宠物的展示和隐藏
        self.setWindowOpacity(1)

    # 宠物随机位置
    def randomPosition(self):
        screen_geo = QDesktopWidget().screenGeometry()
        pet_geo = self.geometry()
        width = (screen_geo.width() - pet_geo.width()) * random.random()
        height = (screen_geo.height() - pet_geo.height()) * random.random()
        self.move(width, height)
    #打开文件
    def openfile(self,path):
        os.startfile(path)

    #klee
    def klee_chan(self):
        self.any = 0


    def round(self):

        if not self.any:

            pygame.init()
            pygame.mixer.init()
            pygame.mixer.music.load("voices/toknow-1.ogg")
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.play()


    def jie(self):
        path = os.getcwd()
        os.chdir(path)
        os.system('python te.py')

        # import tkinter as tk
        #
        # import py_tool
        # import screenshot
        #
        # scale = py_tool.get_screen_scale_rate()
        # py_tool.eliminate_scaling_interference()
        # top = tk.Tk()
        #
        # screenshot.Screenshot(top, scale)
        #
        # top.mainloop()

    # 鼠标左键按下时, 宠物将和鼠标位置绑定
    def mousePressEvent(self, event):
        # 更改宠物状态为点击
        self.condition = 1
        # 更改宠物对话状态
        self.talk_condition = 1
        #切换阿尼亚


        # 即可调用对话状态改变
        self.talk()
        self.round()
        # 即刻加载宠物点击动画
        self.randomAct()
        if event.button() == Qt.LeftButton:
            self.is_follow_mouse = True
        # globalPos() 事件触发点相对于桌面的位置
        # pos() 程序相对于桌面左上角的位置，实际是窗口的左上角坐标
        self.mouse_drag_pos = event.globalPos() - self.pos()
        event.accept()
        # 拖动时鼠标图形的设置
        self.setCursor(QCursor(Qt.OpenHandCursor))

    # 鼠标移动时调用，实现宠物随鼠标移动
    def mouseMoveEvent(self, event):
        # 如果鼠标左键按下，且处于绑定状态
        if Qt.LeftButton and self.is_follow_mouse:
            # 宠物随鼠标进行移动
            self.move(event.globalPos() - self.mouse_drag_pos)
        event.accept()

    # 鼠标释放调用，取消绑定
    def mouseReleaseEvent(self, event):
        self.is_follow_mouse = False
        # 鼠标图形设置为箭头
        self.setCursor(QCursor(Qt.ArrowCursor))

    # 鼠标移进时调用
    def enterEvent(self, event):
        # 设置鼠标形状 Qt.ClosedHandCursor   非指向手
        self.setCursor(Qt.ClosedHandCursor)

    # 宠物右键点击交互
    def contextMenuEvent(self, event):
        # 定义菜单
        menu = QMenu(self)
        # 定义菜单项
        quitAction = menu.addAction("退出")
        hide = menu.addAction("隐藏")
        voice = menu.addAction('可莉语音')
        img = menu.addAction('截屏')
        pycharm = menu.addAction('打开pycharm')
        note = menu.addAction('打开记事本')
        llq = menu.addAction('打开浏览器')

        chan = menu.addAction('阿尼亚')
        klee = menu.addAction('可莉')
        # 使用exec_()方法显示菜单。从鼠标右键事件对象中获得当前坐标。mapToGlobal()方法把当前组件的相对坐标转换为窗口（window）的绝对坐标。
        action = menu.exec_(self.mapToGlobal(event.pos()))
        # 点击事件为退出
        if action == quitAction:
            qApp.quit()
        # 点击事件为隐藏
        if action == hide:
            # 通过设置透明度方式隐藏宠物
            self.setWindowOpacity(0)

        if action == voice:
            self.showChi()

        if action == img:
            self.jie()

        if action == pycharm:
            self.openfile(r'D:\PyCharm 2020.3\bin\pycharm64.exe')
        if action == note:
            os.system('notepad')
            # self.openfile('notepad')
        if action == llq:
            self.openfile('')
        if action == chan:
            self.change()
        if action == klee:
            self.klee_chan()

    def showChi(self):
        self.tea_register = window(self)
        self.tea_register.show()



class window(QDialog):
    def __init__(self, parent = None):
        super(window, self).__init__(parent)
        self.resize(500,550)
        self.setWindowTitle("可莉语音包")
        # quit = QPushButton('Close', self)  # button 对象
        # quit.clicked.connect(self.close)  # 点击按钮之后关闭窗口
        #self.vc = DesktopPet()
        # self.label = QLabel(self)
        # self.label.setText("Hello World")
        # font = QFont()
        # font.setFamily("Arial")
        # font.setPointSize(16)
        # self.label.setFont(font)
        # self.label.move(50,20)


        self.vo_di1 = {'first-meet.ogg':'初次见面',
                      'good-morning.ogg':'早上好',
                      'good-noon.ogg': '中午好',
                      'good-evening.ogg': '晚上好',
                      'good-night.ogg': '晚安',
                      'chatting-adventure.ogg': '闲聊·冒险',
                      'about-herself-compensation.ogg': '关于可莉自己·赔偿',
                      'about-us-knight.ogg': '关于我们·骑士',
                      'toknow-1.ogg': '你好！你是来找可莉玩的吗？',
                      'likes.ogg': '可莉的爱好',
                      'dadada.ogg':'冲刺_哒哒哒',
                      'lalala.ogg':'冲刺_啦啦啦'

                      }

        self.vo_di2 = {'chatting-harvest.ogg': '闲聊·收获',
                       'chatting-law.ogg': '闲聊·守则',
                       'raining.ogg': '下雨的时候',
                       'thundering.ogg': '打雷的时候',
                       'winding.ogg': '刮大风了',
                       'about-us-playmate.ogg': '关于我们·玩伴',
                       'about-eye-of-god.ogg': '关于「神之眼」',
                       'share.ogg': '有什么想要分享',
                       'about-reze.ogg': '关于雷泽',
                       'about-parents.ogg': '关于父母',
                       'about-kea.ogg': '关于凯亚',
                       'about-amber.ogg ': '关于安伯'
                       }

        self.vo_di3 = {
                    'about-jean.ogg': '关于琴',
                    'about-lisa.ogg': '关于丽莎',
                    'about-bennett.ogg': '关于班尼特',
                    'about-diona.ogg': '关于迪奥娜',
                    'about-mona.ogg': '关于莫娜',
                    'about-sugar.ogg': '关于砂糖',
                    'toknow-2.ogg': '想要了解可莉·其二',
                    'toknow-3.ogg': '想要了解可莉·其三',
                    '想要了解可莉·其三': '想要了解可莉·其四',
                    'toknow-5.ogg': '想要了解可莉·其五',
                    'troubles.ogg': '可莉的烦恼',
                    'like-food.ogg': '喜欢的食物',
                    'hate-food.ogg': '讨厌的食物',


                       }



        self.vo_di4 = {
                    'breakthrough-1.ogg': '突破的感受·起',
                    'breakthrough-2.ogg': '突破的感受·承',
                    'breakthrough-3.ogg': '突破的感受·转',

                       }
        x = 0
        y = 0
        inde = 40

        self.button1 = []
        for k in self.vo_di1:
            self.button1.append(k)


        i = 0
        # l = [1,2,3,4,5]
        for k in self.vo_di1:
            self.button1[i] = QPushButton(self)
            self.button1[i].setText(self.vo_di1[k])
            self.button1[i].move(x, y+inde)
            self.button1[i].clicked.connect(self.clickButton)
            inde = inde+40



        x = 170
        y = 0
        inde = 40
        self.button2 = []
        for k in self.vo_di2:
            self.button2.append(k)

        i = 0
        # l = [1,2,3,4,5]
        for k in self.vo_di2:
            self.button2[i] = QPushButton(self)
            self.button2[i].setText(self.vo_di2[k])
            self.button2[i].move(x, y + inde)
            self.button2[i].clicked.connect(self.clickButton)
            inde = inde + 40

        x = 340
        y = 0
        inde = 40
        self.button3 = []
        for k in self.vo_di3:
            self.button3.append(k)

        i = 0
        # l = [1,2,3,4,5]
        for k in self.vo_di3:
            self.button3[i] = QPushButton(self)
            self.button3[i].setText(self.vo_di3[k])
            self.button3[i].move(x, y + inde)
            self.button3[i].clicked.connect(self.clickButton)
            inde = inde + 40

        x = 510
        y = 0
        inde = 40
        self.button4 = []
        for k in self.vo_di4:
            self.button4.append(k)

        i = 0
        # l = [1,2,3,4,5]
        for k in self.vo_di4:
            self.button4[i] = QPushButton(self)
            self.button4[i].setText(self.vo_di4[k])
            self.button4[i].move(x, y + inde)
            self.button4[i].clicked.connect(self.clickButton)
            inde = inde + 40

        # self.button1 = QPushButton(self)
        # self.button1.setText(self.vo_di['good-morning.ogg'])
        # self.button1.move(x,y)
        # self.button1.clicked.connect(self.clickButton)
        #
        # self.button2 = QPushButton(self)
        # self.button2.setText(self.vo_di['first-meet.ogg'])
        # self.button2.move(x, y+40)
        # self.button2.clicked.connect(self.clickButton)
        #
        # self.button3 = QPushButton(self)
        # self.button3.setText(self.vo_di['toknow-1.ogg'])
        # self.button3.move(x, y + 80)
        # self.button3.clicked.connect(self.clickButton)
        #
        # # self.button4 = QPushButton(self)
        # # self.button4.setText(self.vo_di['good-noon.ogg'])
        # # self.button4.move(x, y + 120)
        # # self.button4.clicked.connect(self.clickButton)
        # #
        # # self.button5 = QPushButton(self)
        # # self.button5.setText(self.vo_di['good-evening.ogg'])
        # # self.button5.move(x, y + 160)
        # # self.button5.clicked.connect(self.clickButton)
        #
        # self.button6 = QPushButton(self)
        # self.button6.setText(self.vo_di['chatting-adventure.ogg'])
        # self.button6.move(x, y + 120)
        # self.button6.clicked.connect(self.clickButton)
        #
        # # self.button7 = QPushButton(self)
        # # self.button7.setText(self.vo_di['about-herself-compensation.ogg'])
        # # self.button7.move(x, y + 240)
        # # self.button7.clicked.connect(self.clickButton)
        # #
        # # self.button8 = QPushButton(self)
        # # self.button8.setT8xt(self.vo_di['about-us-knight.ogg'])
        # # self.button8.move(x, y + 280)
        # # self.button8.clicked.connect(self.clickButton)
        #
        # # self.button9 = QPushButton(self)
        # # self.button9.setText(self.vo_di['likes.ogg'])
        # # self.button9.move(x, y + 320)
        # # self.button9.clicked.connect(self.clickButton)
        #
        # self.button10 = QPushButton(self)
        # self.button10.setText(self.vo_di['dadada.ogg'])
        # self.button10.move(x, y + 160)
        # self.button10.clicked.connect(self.clickButton)
        #
        # self.button11 = QPushButton(self)
        # self.button11.setText(self.vo_di['lalala.ogg'])
        # self.button11.move(x, y + 200)
        # self.button11.clicked.connect(self.clickButton)


    def clickButton(self):
        sender = self.sender()
        vodi = {
            'first-meet.ogg': '初次见面',
            'good-morning.ogg': '早上好',
            'good-noon.ogg': '中午好',
            'good-evening.ogg': '晚上好',
            'good-night.ogg': '晚安',
            'chatting-adventure.ogg': '闲聊·冒险',
            'about-herself-compensation.ogg': '关于可莉自己·赔偿',
            'about-us-knight.ogg': '关于我们·骑士',
            'toknow-1.ogg': '你好！你是来找可莉玩的吗？',
            'likes.ogg': '可莉的爱好',
            'dadada.ogg': '冲刺_哒哒哒',
            'lalala.ogg': '冲刺_啦啦啦',
            'chatting-harvest.ogg': '闲聊·收获',
            'chatting-law.ogg': '闲聊·守则',
            'raining.ogg': '下雨的时候',
            'thundering.ogg': '打雷的时候',
            'winding.ogg': '刮大风了',
            'about-us-playmate.ogg': '关于我们·玩伴',
            'about-eye-of-god.ogg': '关于「神之眼」',
            'share.ogg': '有什么想要分享',
            'about-reze.ogg': '关于雷泽',
            'about-parents.ogg': '关于父母',
            'about-kea.ogg': '关于凯亚',
            'about-amber.ogg ': '关于安伯',
            'about-jean.ogg': '关于琴',
            'about-lisa.ogg': '关于丽莎',
            'about-bennett.ogg': '关于班尼特',
            'about-diona.ogg': '关于迪奥娜',
            'about-mona.ogg': '关于莫娜',
            'about-sugar.ogg': '关于砂糖',
            'toknow-2.ogg': '想要了解可莉·其二',
            'toknow-3.ogg': '想要了解可莉·其三',
            'toknow-4.ogg': '想要了解可莉·其四',
            'toknow-5.ogg': '想要了解可莉·其五',
            'troubles.ogg': '可莉的烦恼',
            'like-food.ogg': '喜欢的食物',
            'hate-food.ogg': '讨厌的食物',
            'breakthrough-1.ogg': '突破的感受·起',
            'breakthrough-2.ogg': '突破的感受·承',
            'breakthrough-3.ogg': '突破的感受·转',


        }
        # print(sender.text() + '被点击')

        key = self.get_key(vodi,sender.text())
        self.playMusic(key)


    def get_key(self,dict1, value):
        return [k for k, v in dict1.items() if v == value]



    def playMusic(self,path):
        base_path = 'voices'
        path = base_path+'/'+path[0]
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(path)
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play()

    def closeEvent(self, event):
        self.reject()


if __name__ == '__main__':
    # 创建了一个QApplication对象，对象名为app，带两个参数argc,argv
    # 所有的PyQt5应用必须创建一个应用（Application）对象。sys.argv参数是一个来自命令行的参数列表。
    app = QApplication(sys.argv)
    # 窗口组件初始化
    pet = DesktopPet()
    # 1. 进入时间循环；
    # 2. wait，直到响应app可能的输入；
    # 3. QT接收和处理用户及系统交代的事件（消息），并传递到各个窗口；
    # 4. 程序遇到exit()退出时，机会返回exec()的值。
    sys.exit(app.exec_())