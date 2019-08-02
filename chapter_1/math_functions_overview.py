#!/usr/bin/python3

import math


scale = 12.0
position = 6

windowWidth = 600
windowMargin = 30
windowHeight = windowWidth
windowCenter = windowWidth/2, windowHeight/2

hourCursorLength = windowWidth/2.0-windowMargin-140


def main():

    degrees = getCursorPositionDegrees(position, scale)
    bogenmass = gradToBogenmass(degrees)
    x, y = getCirclePoint(position, scale, hourCursorLength)

    print("degrees: %s" % degrees)
    print("bogenmass: %s" % bogenmass)
    print("relative x- and y-Pos: (%s, %s)" % (x, y))

    rad = (math.pi / 2) # 90 degrees

    # use rad values for calculating the x and y coord into the unit circle!
    # 
    # good picture about the unit circle with rad and degrees: 
    # https://en.wikipedia.org/wiki/File:Unit_circle_angles_color.svg
    x = round(math.cos(rad), 2)
    y = round(math.sin(rad), 2)
    print("x- and y-Pos in unit circle for rad=%s: (%s, %s)" % (rad, x, y))


def getCursorPositionDegrees(position, scale):
    
    # Calculating the offset is required to map the calculated angle 
    # to the right-handed cartesian coordinate system.
    cursorOffset = -90

    return ((360 / scale) * position) + cursorOffset # return degrees


def gradToBogenmass(degrees):
    
    # from the book
    ##return degrees/180.0*math.pi
    
    # transformed formular for calculating the radian from maths literature
    ##return (math.pi/180) * degrees
    
    # standard librarty function call from math Pythons math lib
    return math.radians(degrees)


def getCirclePoint(position, scale, cursorLength):
    
    # should return relative position for the cursor...
    degrees = getCursorPositionDegrees(position, scale)
    bogenmass = gradToBogenmass(degrees)
    
    xPos = round(math.cos(bogenmass)*cursorLength+windowCenter[0])
    yPos = round(math.sin(bogenmass)*cursorLength+windowCenter[1])
    
    return (xPos, yPos)


main()
