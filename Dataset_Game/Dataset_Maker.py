import os
import shutil
raw_path=r"C:\Users\suhaa\Desktop\OCV\Chess_Detector\Dataset_Game\Marked_Dataset"
gen=os.walk(raw_path)
count=0
filelis=next(gen)[2]

#raw path is the raw dataset path and we are shifting files to folders in base path
base_path=r"C:\Users\suhaa\Desktop\OCV\Chess_Detector\Dataset_Game\Data\VALIDATION"
for file in filelis:
    FILE=file.lower()
    if "wpawn" in FILE: #file("Wbishop"):
        #print("##########################################")
        shift_path=base_path+"\\WP\\"+file
        from_path=raw_path+"\\"+file
        shutil.copyfile(from_path,shift_path)
    if "wknight" in FILE: #file("Wbishop"):
        #print("##########################################")
        shift_path=base_path+"\\WN\\"+file
        from_path=raw_path+"\\"+file
        shutil.copyfile(from_path,shift_path)
    if "wbishop" in FILE: #file("Wbishop"):
        #print("##########################################")
        shift_path=base_path+"\\WB\\"+file
        from_path=raw_path+"\\"+file
        shutil.copyfile(from_path,shift_path)
    if "wrook" in FILE: #file("Wbishop"):
        #print("##########################################")
        shift_path=base_path+"\\WR\\"+file
        from_path=raw_path+"\\"+file
        shutil.copyfile(from_path,shift_path)
    if "wqueen" in FILE: #file("Wbishop"):
        #print("##########################################")
        shift_path=base_path+"\\WQ\\"+file
        from_path=raw_path+"\\"+file
        shutil.copyfile(from_path,shift_path)
    if "wking" in FILE: #file("Wbishop"):
        #print("##########################################")
        shift_path=base_path+"\\WK\\"+file
        from_path=raw_path+"\\"+file
        shutil.copyfile(from_path,shift_path)



    if "bpawn" in FILE: #file("Wbishop"):
        #print("##########################################")
        shift_path=base_path+"\\BP\\"+file
        from_path=raw_path+"\\"+file
        shutil.copyfile(from_path,shift_path)
    if "bknight" in FILE: #file("Wbishop"):
        #print("##########################################")
        shift_path=base_path+"\\BN\\"+file
        from_path=raw_path+"\\"+file
        shutil.copyfile(from_path,shift_path)
    if "bbishop" in FILE: #file("Wbishop"):
        #print("##########################################")
        shift_path=base_path+"\\BB\\"+file
        from_path=raw_path+"\\"+file
        shutil.copyfile(from_path,shift_path)
    if "brook" in FILE: #file("Wbishop"):
        #print("##########################################")
        shift_path=base_path+"\\BR\\"+file
        from_path=raw_path+"\\"+file
        shutil.copyfile(from_path,shift_path)
    if "bqueen" in FILE: #file("Wbishop"):
        #print("##########################################")
        shift_path=base_path+"\\BQ\\"+file
        from_path=raw_path+"\\"+file
        shutil.copyfile(from_path,shift_path)
    if "bking" in FILE: #file("Wbishop"):
        #print("##########################################")
        shift_path=base_path+"\\BK\\"+file
        from_path=raw_path+"\\"+file
        shutil.copyfile(from_path,shift_path)
    if "empty" in FILE: #file("Wbishop"):
        #print("##########################################")
        shift_path=base_path+"\\empty\\"+file
        from_path=raw_path+"\\"+file
        shutil.copyfile(from_path,shift_path)
