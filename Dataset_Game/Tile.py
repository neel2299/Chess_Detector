import os
import random
import Game_Config as gc
from pygame import image, transform
class tile:     #planning to create tile in this way=> 30 10 ()
    def __init__(self,row,col,name):
        self.row=row
        self.col=col
        self.name=name
        self.image_path = os.path.join(gc.ASSET_DIR, self.name)
        self.image = image.load(self.image_path)
        self.image = transform.scale(self.image, (gc.IMAGE_SIZE - 2 * gc.MARGIN, gc.IMAGE_SIZE - 2 * gc.MARGIN))


class special_tile():
    def __init__(self,row,col,name,path):
        self.row = row
        self.col = col
        self.name = name
        self.image_path = path+self.name
        print(self.image_path)
        self.image = image.load(self.image_path)
        self.image = transform.scale(self.image, (gc.IMAGE_SIZE - 2 * gc.MARGIN, gc.IMAGE_SIZE - 2 * gc.MARGIN))

