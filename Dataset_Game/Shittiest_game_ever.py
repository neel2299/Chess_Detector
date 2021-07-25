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
screen = display.set_mode((512, 512))
display.set_caption('Boring game')
color = (0, 255, 153)
screen.fill(color)
display.flip()
current_events=pygame.event.get()
running = True
knight = tile(10,10, "Knight.png")
bishop=tile(10,10,"bishop.png")
king=tile(10,10,"King.png")
queen=tile(10,10,"Queen.png")
rook=tile(10,10,"Rook.png")
pawn=tile(10,10,"pawn.png")
screen.blit(pawn.image,(20,250))
screen.blit(knight.image,(120,250))
screen.blit(bishop.image,(220,250))
screen.blit(rook.image,(320,250))
screen.blit(queen.image,(20,350))
screen.blit(king.image,(120,350))
display.flip()
count=192
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
        print("pawn")
        save_string=str(count)+"_"+"pawn.png"
        image.save(file.image,save_string)
    elif pos[0]>120 and pos[0]<216 and pos[1]>250 and pos[1]<346:
        print("knight")
        save_string = str(count) + "_" + "knight.png"
        image.save(file.image, save_string)
    elif pos[0]>220 and pos[0]<316 and pos[1]>250 and pos[1]<346:
        print("bishop")
        save_string = str(count) + "_" + "bishop.png"
        image.save(file.image, save_string)
    elif pos[0]>320 and pos[0]<416 and pos[1]>250 and pos[1]<346:
        print("rook")
        save_string = str(count) + "_" + "rook.png"
        image.save(file.image, save_string)
    elif pos[0]>20 and pos[0]<116 and pos[1]>350 and pos[1]<446:
        print("queen")
        save_string = str(count) + "_" + "queen.png"
        image.save(file.image, save_string)
    elif pos[0]>120 and pos[0]<216 and pos[1]>350 and pos[1]<446:
        print("king")
        save_string = str(count) + "_" + "king.png"
        image.save(file.image, save_string)
    elif pos[0]>200 and pos[0]<296 and pos[1]>20 and pos[1]<116:
        print("empty")
        save_string = str(count) + "_" + "empty.png"
        image.save(file.image, save_string)
    count+=1


