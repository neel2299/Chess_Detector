import cv2 as cv
import os
import pygame
from pygame import display,Surface,image
from Tile import tile,special_tile

import Game_Config as gc
from pygame.locals import *
def wait():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                global running
                running=False
                return (0,0)
            if event.type == MOUSEBUTTONUP :
                pos = pygame.mouse.get_pos()
                return pos
pygame.init()
screen = display.set_mode((512, 680))
display.set_caption('Boring game')
color = (0, 255, 153)
screen.fill(color)
display.flip()
current_events=pygame.event.get()
running = True
knight = tile(10,10, "BKnight.png")
bishop=tile(10,10,"Bbishop.png")
king=tile(10,10,"BKing.png")
queen=tile(10,10,"BQueen.png")
rook=tile(10,10,"BRook.png")
pawn=tile(10,10,"Bpawn.png")
screen.blit(pawn.image,(20,250))
screen.blit(knight.image,(120,250))
screen.blit(bishop.image,(220,250))
screen.blit(rook.image,(320,250))
screen.blit(queen.image,(20,350))
screen.blit(king.image,(120,350))

Wknight = tile(10,10, "WKnight.png")
Wbishop=tile(10,10,"Wbishop.png")
Wking=tile(10,10,"WKing.png")
Wqueen=tile(10,10,"WQueen.png")
Wrook=tile(10,10,"WRook.png")
Wpawn=tile(10,10,"Wpawn.png")
screen.blit(Wpawn.image,(20,490))
screen.blit(Wknight.image,(120,490))
screen.blit(Wbishop.image,(220,490))
screen.blit(Wrook.image,(320,490))
screen.blit(Wqueen.image,(20,590))
screen.blit(Wking.image,(120,590))


display.flip()
count=0
path=r"C:\Users\suhaa\Desktop\OCV\Chess_Detector\Pieces"+"\\"
os.chdir(r"C:\Users\suhaa\Desktop\OCV\Chess_Detector\Dataset_Game\Marked_Dataset")
while running:
    string=str(count)+r".png"
    print(string)
    file = special_tile(10, 10, string,path)
    screen.blit(file.image, (200, 20))
    display.flip()
    #current_events=pygame.event.get()
    #for event in current_events:
    # if event.type == pygame.QUIT:
    #     running = False
    # if event.type == pygame.MOUSEBUTTONUP:
    #     pos = pygame.mouse.get_pos()
    pos = wait()
    if pos[0]>20 and pos[0]<116 and pos[1]>250 and pos[1]<346:
        print("Bpawn")
        save_string=str(count)+"_"+"Bpawn.png"
        image.save(file.image,save_string)
    elif pos[0]>120 and pos[0]<216 and pos[1]>250 and pos[1]<346:
        print("Bknight")
        save_string = str(count) + "_" + "Bknight.png"
        image.save(file.image, save_string)
    elif pos[0]>220 and pos[0]<316 and pos[1]>250 and pos[1]<346:
        print("Bbishop")
        save_string = str(count) + "_" + "Bbishop.png"
        image.save(file.image, save_string)
    elif pos[0]>320 and pos[0]<416 and pos[1]>250 and pos[1]<346:
        print("Brook")
        save_string = str(count) + "_" + "Brook.png"
        image.save(file.image, save_string)
    elif pos[0]>20 and pos[0]<116 and pos[1]>350 and pos[1]<446:
        print("Bqueen")
        save_string = str(count) + "_" + "Bqueen.png"
        image.save(file.image, save_string)
    elif pos[0]>120 and pos[0]<216 and pos[1]>350 and pos[1]<446:
        print("Bking")
        save_string = str(count) + "_" + "Bking.png"
        image.save(file.image, save_string)
    # elif pos[0]>200 and pos[0]<296 and pos[1]>20 and pos[1]<116:
    #     print("empty")
    #     save_string = str(count) + "_" + "empty.png"
    #     image.save(file.image, save_string)

    ##########################################################################
    elif pos[0]>20 and pos[0]<116 and pos[1]>490 and pos[1]<586:
        print("Wpawn")
        save_string=str(count)+"_"+"Wpawn.png"
        image.save(file.image,save_string)
    elif pos[0]>120 and pos[0]<216 and pos[1]>490 and pos[1]<586:
        print("Wknight")
        save_string = str(count) + "_" + "Wknight.png"
        image.save(file.image, save_string)
    elif pos[0]>220 and pos[0]<316 and pos[1]>490 and pos[1]<586:
        print("Wbishop")
        save_string = str(count) + "_" + "Wbishop.png"
        image.save(file.image, save_string)
    elif pos[0]>320 and pos[0]<416 and pos[1]>490 and pos[1]<586:
        print("Wrook")
        save_string = str(count) + "_" + "Wrook.png"
        image.save(file.image, save_string)
    elif pos[0]>20 and pos[0]<116 and pos[1]>590 and pos[1]<686:
        print("Wqueen")
        save_string = str(count) + "_" + "Wqueen.png"
        image.save(file.image, save_string)
    elif pos[0]>120 and pos[0]<216 and pos[1]>590 and pos[1]<686:
        print("Wking")
        save_string = str(count) + "_" + "Wking.png"
        image.save(file.image, save_string)
    elif pos[0]>200 and pos[0]<296 and pos[1]>20 and pos[1]<116:
        print("empty")
        save_string = str(count) + "_" + "empty.png"
        image.save(file.image, save_string)


    count+=1


