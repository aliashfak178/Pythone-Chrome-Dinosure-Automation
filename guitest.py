import pyautogui as pgui 
import time
from PIL import Image,ImageGrab

def hit(Key):
    pgui.keyDown(Key)
    return 

def isCollid(data):
    #Drow the Ractangle for bird
    for i in range(235,365):
        for j in range(380,450):
            if data[i,j] < 100:
                hit('down')
                return 
             

    #Drow the Ractangle for cactus
    for i in range(300,425):
        for j in range(450,550):
            if data[i,j] < 100:
                hit('up')
                return 
    return          


if __name__ == "__main__":
    print("Hay... Dino game is start in 2 sec:")
    time.sleep(2)
    hit('up')
    while True:
        Image=ImageGrab.grab().convert('L')
        data=Image.load()
        isCollid(data)

    """
        #Drow the Ractangle for cactus
        for i in range(300,425):
            for j in range(450,550):
                data[i,j] = 0

        #Drow the Ractangle for bird
        for i in range(235,365):
            for j in range(380,450):
                data[i,j] = 171       
        Image.show()
        break
    """