# tutorial of simple fishing bot for mrpg

import time
import pyautogui as pyautogui
from PIL import ImageGrab

# days at the office
# octWork = [7,11,12,18,20,21]
# octthuis = [6,8,13,14,15,19,22,25,26,27,28]

# septWerk = [8,13,14,20,23,27,29]
# septThuis = [2,3,6,7,9,10,15,16,17,21,22,24,28,30]

# julWerk = [5,7,12,14,21,23,26,30]
# julThuis = [1,2,6,8,9,13,15,16,19,20,22,25,27,28,29]

# junWerk = [2, 7, 9, 14, 16, 21, 23, 25, 28, 30]
# junThuis = [3, 4, 8, 10, 11, 15, 17, 18, 22, 24, 29]

#decWerk = [2, 6, 8, 13, 16]
#decThuis = [1, 3, 7, 9, 10, 14, 15, 20, 21, 22, 23]

#==2022 ==
janW = [13,18,20,21,24,26,31]
janT = [3,4,5,6,7,10,11,12,14,17,19,25,27,28]

febW = [1,3,7,8,10,14,17,18,21,23]
febT = [2,4,9,11,15,16,22,24,25,28]

martW = [1,3,7,9,22,24,28,29,31]
martT = [2,4,8,10,11,14,15,16,17,18,21,23,25,30]


toWork = martT
month = "03"
year = "2022"
typeInp = "home"  # work or home


def checkIfDuplicates_1(listOfElems):
    ''' Check if given list contains any duplicates '''
    if len(listOfElems) != len(set(listOfElems)):
        print("List contains duplicates - quiting ")
        quit()


# pixel color on screen
def getColor(x, y):
    px = ImageGrab.grab().load()
    color = px[x, y]
    return color[0]


# single mouse click
def singleClick():
    pyautogui.mouseDown()
    time.sleep(0.2)
    pyautogui.mouseUp()
    time.sleep(0.2)


# check if the color of the given pixel is as expected
def checkColorAtCoord(x, y, col1):
    i = 1
    while i < 10:
        print("waiting for " + str(col1) + " .. " + str(i) + " seconds")
        i += 1
        time.sleep(1)
        if getColor(x, y) == col1:
            break
    if getColor(x, y) != col1:
        print("Required value not found found in the given time - quiting ")
        quit()


def FindCoordOfThuisdagKnop():
    i = 1
    while i < 100:
        print("Looking for blue button at coordinate " + str(600 + i * 5))
        i += 1
        if getColor(490, 600 + i * 5) == 5:
            return 600 + i * 5
    print("Blue button not found - quiting ")
    quit()


# main engine

def clickAndFill():
    print("Lets start ")
    checkIfDuplicates_1(toWork)

    y_coord_knop = 420

    if typeInp == "home":
        y_coord_knop = FindCoordOfThuisdagKnop()

    for r in range(len(toWork)):
        time.sleep(0.5)
        # check of the background is white
        checkColorAtCoord(100, 200, 255)
        # check if the button is blue
        checkColorAtCoord(490, y_coord_knop, 5)

        # reisdagen nieuw
        pyautogui.moveTo(490, y_coord_knop)  # reisdagen 490, 420 // thuiswerkdagen 490 >600
        singleClick()

        # datum veld
        pyautogui.moveTo(480, 340)
        singleClick()
        # check if the background is grey - window open
        checkColorAtCoord(100, 200, 183)

        day = str(toWork[r])
        if len(day) == 1:
            day = str(0) + day
        pyautogui.write(day + "-" + month + "-" + year)
        print("Filling", day + "-" + month + "-" + year)
        time.sleep(1)

        # accept datum
        pyautogui.moveTo(1640, 430)     # HD1080 y= 390  HD1200 y = 430
        singleClick()
        time.sleep(3)

    print("Code finished successefully")





def main():
    clickAndFill()


if __name__ == "__main__":
    main()


