import os
os.chdir(r"C:\Users\suhaa\Desktop\OCV\Chess_Detector\Dataset_Game")
IMAGE_SIZE=103
SCREEN_SIZE=512
NUM_TILES_SIDE=4
NUM_TILES_TOTAL=16
MARGIN = 4
ASSET_DIR = 'Assets'
ASSET_FILES= [x for x in os.listdir(ASSET_DIR) if x[-3:].lower()=='png']

