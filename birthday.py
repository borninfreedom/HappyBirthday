#coding=utf-8
import turtle
import random
import time
from turtle import *
from random import *
import sys
import pygame
#from moviepy.editor import *
import os

APP_FOLDER=os.path.dirname(os.path.realpath(sys.argv[0]))
os.chdir(APP_FOLDER)

def make_cake(turtle,x=0,y=0):
    tina=turtle
    tina.penup()
    tina.color('white')
    tina.goto(x,y)
    tina.pendown()
    tina.begin_fill()
    tina.goto(x+20,y)
    tina.goto(x+20,y+20)
    tina.goto(x-20,y+20)
    tina.goto(x-20,y)
    tina.goto(x,y)
    tina.end_fill()
    tina.goto(x,y+20)
    tina.color('blue')
    tina.goto(x,y+35)
    tina.goto(x,y+30)
    tina.color('black')
    tina.goto(x,y+20)
    tina.penup()
    tina.goto(x,y+10)

#file='media/wuchuanfang.wav'
pygame.mixer.init()
track=pygame.mixer.music.load('media/wuchuanfang.wav')
pygame.mixer.music.play()

bg=turtle.Screen()
#bg.bgcolor("black")
bg.bgpic('media/zzy.png')
tommy=turtle.Turtle()
tommy.shape("turtle")
tommy.speed(1)

x=80
y=300
interval=35

tommy.color("red")

tommy.penup()
tommy.goto(x,y)  #每次减25
time.sleep(1)
tommy.write("  我从不会轻易许下任何诺言",font=('微软雅黑', 12, 'bold'))
time.sleep(4)

tommy.color("orange")
tommy.penup()
tommy.goto(x,y-interval)
tommy.write("  也从不会为一个人如此心碎",font=('微软雅黑',12,'bold'))
time.sleep(4)

tommy.color("yellow")
tommy.penup()
tommy.goto(x,y-interval*2)
tommy.write("  而现在我可以敞开我的心扉",font=('微软雅黑', 12, 'bold'))
time.sleep(4)

tommy.color("lime green")
tommy.penup()
tommy.goto(x,y-interval*3)  #每次减25
tommy.write("  你是我唯一真心爱过的姑娘",font=('微软雅黑', 12, 'bold'))
time.sleep(4)

tommy.color("blue")
tommy.penup()
tommy.goto(x,y-interval*4)  #每次减25
tommy.write("  愿上苍为你指引平坦的道路",font=('微软雅黑', 12, 'bold'))
time.sleep(4)

tommy.color("cyan")
tommy.penup()
tommy.goto(x,y-interval*5)  #每次减25
tommy.write("  愿命运让你遇见善良的人们",font=('微软雅黑', 12, 'bold'))
time.sleep(4)

tommy.color("medium slate blue")
tommy.penup()
tommy.goto(x,y-interval*6)  #每次减25
tommy.write("  愿远方的阳光和璀璨的灯火",font=('微软雅黑', 12, 'bold'))
time.sleep(4)

tommy.color("red")
tommy.penup()
tommy.goto(x,y-interval*7)  #每次减25
tommy.write("  为你照亮每一片未来的天空",font=('微软雅黑', 12, 'bold'))
time.sleep(4)

tommy.color("orange")
tommy.penup()
tommy.goto(x,y-interval*8)  #每次减25
tommy.write("  时光就像一条奔腾的河流",font=('微软雅黑', 12, 'bold'))
time.sleep(4)

tommy.color("yellow")
tommy.penup()
tommy.goto(x,y-interval*9)  #每次减25
tommy.write("  将生命中的一切悄悄带走",font=('微软雅黑', 12, 'bold'))
time.sleep(4)

tommy.color("lime green")
tommy.penup()
tommy.goto(x,y-interval*10)  #每次减25
tommy.write("  而我的心就像那翻涌的浪花",font=('微软雅黑', 12, 'bold'))
time.sleep(4)

tommy.color("blue")
tommy.penup()
tommy.goto(x,y-interval*11)  #每次减25
tommy.write("  永远陪着你哪怕是海角天涯",font=('微软雅黑', 12, 'bold'))
time.sleep(4)

tommy.color("cyan")
tommy.penup()
tommy.goto(x,y-interval*12)  #每次减25
tommy.write("  从此希望你明白",font=('微软雅黑', 12, 'bold'))
time.sleep(4)

tommy.color("medium slate blue")
tommy.penup()
tommy.goto(x,y-interval*13)  #每次减25
tommy.write("  我就在你身旁",font=('微软雅黑', 12, 'bold'))
time.sleep(4)

tommy.color("red")
tommy.penup()
tommy.goto(x,y-interval*14)  #每次减25
tommy.write("  无论你在多远的地方",font=('微软雅黑', 12, 'bold'))
time.sleep(4)

tommy.color("orange")
tommy.penup()
tommy.goto(x,y-interval*15)  #每次减25
tommy.write("  即使你变了模样",font=('微软雅黑', 12, 'bold'))
time.sleep(4)

tommy.color("yellow")
tommy.penup()
tommy.goto(x,y-interval*16)  #每次减25
tommy.write("  即使你把我遗忘",font=('微软雅黑', 12, 'bold'))
time.sleep(4)

tommy.color("lime green")
tommy.penup()
tommy.goto(x,y-interval*17)  #每次减25
tommy.write("  你永远都是我心爱的姑娘",font=('微软雅黑', 12, 'bold'))
time.sleep(4)

time.sleep(1)

pygame.mixer.music.stop()

file='media/Happy.mp3'
pygame.mixer.music.load(file)
pygame.mixer.music.play()
time.sleep(4)

tommy.clear()
bg.bgpic("nopic")
tommy.pensize(6)

#draw lines
tommy.penup()
tommy.goto(-190,-180)
tommy.color("yellow")
tommy.pensize(6)
tommy.pendown()
tommy.goto(190,-180)
tommy.penup()

tommy.penup()
tommy.goto(-160, -150)
tommy.color("purple")
tommy.pensize(6)
tommy.pendown()
tommy.goto(160,-150)
tommy.penup()

tommy.penup()
tommy.goto(-130, -120)
tommy.color("teal")
tommy.pensize(6)
tommy.pendown()
tommy.goto(130,-120)
tommy.penup()

# draw cake
tommy.goto(-74,-110)   #这个是画蛋糕
tommy.begin_fill()
tommy.pendown()
tommy.color("white")
tommy.goto(50,-110)
tommy.left(90)
tommy.forward(60)
tommy.left(90)
tommy.forward(125)
tommy.left(90)
tommy.forward(60)
tommy.end_fill()
tommy.penup()


tommy.goto(-74,-110)   #这个是画蛋糕，到这个坐标去,这个是黄色那层
tommy.begin_fill()
tommy.pendown()   #放下画笔
tommy.color("yellow")
tommy.goto(50,-110)
tommy.left(90)

tommy.left(90)
tommy.forward(45)  #这个是一层的厚度
tommy.left(90)  #这个是根据角度来转方像
tommy.forward(125)
tommy.left(90)  #这个是根据角度来转方像
tommy.forward(45)
tommy.end_fill()
tommy.penup()

tommy.goto(-74,-110)   #这个是画蛋糕，到这个坐标去,这个是黄色那层
tommy.begin_fill()
tommy.pendown()   #放下画笔
tommy.color("#40E0D0")
tommy.goto(50,-110)
tommy.left(90)

tommy.left(90)
tommy.forward(30)  #这个是一层的厚度
tommy.left(90)  #这个是根据角度来转方像
tommy.forward(125)
tommy.left(90)  #这个是根据角度来转方像
tommy.forward(30)
tommy.end_fill()
tommy.penup()


tommy.goto(-74,-110)   #这个是画蛋糕，到这个坐标去,最下面那层
tommy.begin_fill()
tommy.pendown()   #放下画笔
tommy.color("#BA55D3")
tommy.goto(50,-110)
tommy.left(90)
tommy.left(90)
tommy.forward(15)  #这个是一层的厚度
tommy.left(90)  #这个是根据角度来转方像
tommy.forward(125)
tommy.left(90)  #这个是根据角度来转方像
tommy.forward(15)
tommy.end_fill()
tommy.penup()

#draw candles
tommy.goto(-60, -40)
tommy.color("aquamarine")
tommy.pendown()
tommy.pensize(3)
tommy.goto(-60, -20)
tommy.penup()

tommy.goto(-40, -40)
tommy.color("yellow")
tommy.pendown()
tommy.pensize(3)
tommy.goto(-40, -20)
tommy.penup()

tommy.goto(-20, -40)
tommy.color("green")
tommy.pendown()
tommy.pensize(3)
tommy.goto(-20, -20)
tommy.penup()

tommy.goto(0, -40)
tommy.color("red")
tommy.pendown()
tommy.pensize(3)
tommy.goto(0, -20)
tommy.penup()

tommy.goto(20, -40)
tommy.color("blue")
tommy.pendown()
tommy.pensize(3)
tommy.goto(20, -20)
tommy.penup()


tommy.goto(40, -40)
tommy.color("#556B2F")
tommy.pendown()
tommy.pensize(3)
tommy.goto(40, -20)
tommy.penup()


bg.bgcolor("pink")


def snow():
    tommy.hideturtle()
    tommy.speed(100)
    tommy.pensize(2)
    for i in range(100):
        r=random()
        g=random()
        b=random()
        tommy.pencolor(r,g,b)
        tommy.penup()
        tommy.setx(randint(-350,350))
        tommy.sety(randint(1,270))
        tommy.pendown()
        dens=randint(8,12)
        snowsize=randint(10,14)
        for j in range(dens):
            tommy.forward(snowsize)
            tommy.backward(snowsize)
            tommy.right(360/dens)


time.sleep(0.5)
snow()

tommy.penup()
tommy.goto(-320, 300)
tommy.color("orange")
tommy.pendown()
tommy.write( "漫天 ｡･ﾟ･(ﾉД`)ヽ(ﾟДﾟ ) 烟花送给你~",font=('微软雅黑', 24, 'normal'))

pygame.mixer.music.stop()
file='media/sweet.mp3'

track = pygame.mixer.music.load(file)
pygame.mixer.music.play()

time.sleep(4)


tommy.penup()
tommy.goto(-380,-250)
tommy.write("祝你生日快乐，我的大女票 ο(=•ω＜=)p⌒☆!",font=('微软雅黑', 24, 'normal'))

time.sleep(5)



# send the turtle to the corner


tommy.penup()
tommy.goto(-250, 250)



tommy.hideturtle()

time.sleep(20)
tommy.clear()  #清空屏幕了,然后设置背景色为黑色，滚动演员表

bg.bgcolor("pink")

tommy.clear()

import turtle


turtle.speed(1)

turtle.pensize(6)#：设置画笔的宽度；
turtle.left(30)
turtle.circle(90,300)  #半径大小
#画眼睛



turtle.right(100)
turtle.forward(60)
turtle.left(150)
turtle.forward(55)
turtle.right(110)
turtle.forward(40)
turtle.penup()
turtle.goto(-15,90)
#画眼睛了
turtle.begin_fill()
turtle.color("black")
turtle.circle(8)
turtle.end_fill()


turtle.penup()
turtle.goto(-75,90)
#画眼睛了
turtle.begin_fill()
turtle.color("black")
turtle.circle(8)
turtle.end_fill()

turtle.penup()
turtle.goto(0,70)
#画眼睛了
turtle.begin_fill()
turtle.color("red")
turtle.circle(8)
turtle.end_fill()

turtle.penup()
turtle.goto(-85,70)
#画眼睛了
turtle.begin_fill()
turtle.color("red")
turtle.circle(8)
turtle.end_fill()

turtle.penup()
turtle.goto(-50,50)
#画眼睛了

turtle.pendown()
turtle.color("black")
turtle.left(45)
turtle.circle(20,90)


#画另一只手
turtle.penup()
turtle.color("black")
turtle.goto(0,0)
turtle.right(35)
turtle.pendown()
turtle.forward(75)

turtle.left(85)
turtle.forward(25)
turtle.right(165)
turtle.forward(25)
turtle.left(90)
turtle.forward(35)
turtle.right(155)
turtle.forward(35)


turtle.left(75)
turtle.forward(20)
turtle.right(85)
turtle.forward(20)
turtle.right(85)
turtle.forward(25)


turtle.left(70)
turtle.forward(35)
turtle.left(15)
turtle.forward(20)

turtle.left(60)
turtle.forward(40)


#爱心

turtle.penup()
turtle.color("red")
turtle.right(180)
turtle.goto(135,135)
turtle.pendown()
turtle.circle(20,170)
turtle.forward(15)
turtle.left(45)

turtle.forward(55)

turtle.penup()
turtle.color("red")
turtle.right(250)
turtle.goto(135,135)
turtle.pendown()
turtle.circle(-20,170)
turtle.forward(15)
turtle.right(45)

turtle.forward(55)



turtle.penup()
turtle.goto(135,135)
turtle.pendown()
turtle.forward(45)
turtle.left(160)
turtle.forward(75)
turtle.right(160)
turtle.forward(55)
turtle.goto(135,100)


turtle.penup()
turtle.goto(-85,-140)
turtle.write("love u ",font=("微软雅黑",24,"normal"))

time.sleep(5)


done() #可以使窗口保持

pygame.mixer.music.stop()