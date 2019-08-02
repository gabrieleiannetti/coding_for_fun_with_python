#!/usr/bin/python3

#coding: latin1


'''
@author: Lars Heppert
@book: Coding for Fun mit Python
@chapter: 1
'''
import pygame, sys, math, datetime

windowMargin            = 30
windowWidth             = 600
windowHeight            = windowWidth
windowCenter            = windowWidth/2, windowHeight/2
clockMarginWidth        = 20
secondColor             = (255, 0, 0)
minuteColor             = (100, 200, 0)
hourColor               = (100, 200, 0)
clockMarginColor        = (130, 130, 0)
clockBackgroundColor    = (20, 40, 30)
backgroundColor         = (255, 255, 255)
hourCursorLength        = windowWidth/2.0-windowMargin-140
minuteCursorLength      = windowWidth/2.0-windowMargin-40
secondCursorLength      = windowWidth/2.0-windowMargin-10

virtualSpeed    = 1
useVirtualTimer = False

def handleEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            sys.exit(0)

def getCirclePoint(position, scale, cursorLength):
    degrees = getCursorPositionDegrees(position, scale)
    bogenmass = gradToBogenmass(degrees)
    xPos = round(math.cos(bogenmass)*cursorLength+windowCenter[0])
    yPos = round(math.sin(bogenmass)*cursorLength+windowCenter[1])
    return (xPos, yPos)

def gradToBogenmass(degrees):
    # python bietet auch die Funktion math.radians(degrees),
    # welche die Umrechnung genauso ausfuehrt, aber so wird 
    # der Sachverhalt deutlicher
    return degrees/180.0*math.pi

def getCursorPositionDegrees(position, scale):
    cursorOffset = -90 # 12 o'Clock is -90 degrees
    degrees = 360 / scale * position + cursorOffset
    return degrees

def drawCursor(color, width, length, position, scale):

    end = getCirclePoint(position, scale, length);

    pygame.draw.line(screen, color, windowCenter, end, width)

def drawBackground():

    screen.fill(backgroundColor)

    pygame.draw.ellipse(
        screen, 
        clockMarginColor, 
        (
            windowMargin, 
            windowMargin, 
            windowWidth -2 * windowMargin, 
            windowWidth -2 * windowMargin
        )
    )

    pygame.draw.ellipse(
        screen, 
        clockBackgroundColor, 
        (
            windowMargin + clockMarginWidth / 2, 
            windowMargin + clockMarginWidth / 2, 
            windowWidth - (windowMargin + clockMarginWidth / 2) * 2, 
            windowWidth - (windowMargin + clockMarginWidth / 2) * 2
        )
    )
    
def drawForeground():

    pygame.draw.ellipse(
        screen, 
        clockMarginColor, 
        (
            windowWidth / 2.0 - 9, 
            windowHeight / 2.0 - 9, 
            18, 
            18
        )
    )

hour    = 0
minute  = 0
second  = 0
micro   = 0

def timeGoesOn():
    global hour, minute, second, micro
    micro += virtualSpeed
    if micro >= 2: # halve seconds - not micro seconds
        second += 1
        micro %= 2
    if second > 60:
        minute += 1
        second %= 60
    if minute > 60:
        hour += 1
        minute %= 60
    if hour > 12:
        hour %= 12

def drawCurrentTime():

    if useVirtualTimer:

        global hour, minute, second, micro
        timeGoesOn()

    else:

        now     = datetime.datetime.now()

        hour    = now.hour
        minute  = now.minute
        second  = now.second
        micro   = now.microsecond

    drawCursor(  hourColor, 15, hourCursorLength,   hour+minute/60.0, 12)
    drawCursor(minuteColor,  8, minuteCursorLength, minute+second/60.0, 60)
    drawCursor(secondColor,  3, secondCursorLength, second+micro/1000000.0, 60)


def main():
    
    # Initialise screen
    global screen
    pygame.init()
    
    screen = pygame.display.set_mode(
        (
            windowWidth, 
            windowHeight
        ), 
        pygame.HWSURFACE | pygame.DOUBLEBUF
    );
    
    pygame.display.set_caption('Analog Clock');

    # Event loop
    while True:
        handleEvents()
        drawBackground()
        drawCurrentTime() 
        drawForeground()
        pygame.display.flip()
        pygame.time.delay(10)

if __name__ == '__main__':
    main()
