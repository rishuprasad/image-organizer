# ------------------------------------------------------------------------------------
# Organizing images from a directory into another directory

        
# os.chdir(r"C:\Data\Programming\Programs\Python\Image Organizer")
# parent_dir = os.getcwd()

# imgDirectory = os.walk("C:\Data\Programming\Programs\Python\Image Organizer\images")       

        
# hashList = []
# imgList = []

# for roots, directories, files in imgDirectory:
#     for file in files:
#         # img = Image.open(".\\images\\" + file)
#         img = Image.open(os.path.join("images", file))
#         imgBytes = img.tobytes()
#         md5hash = hashlib.md5(imgBytes)
#         md5hash = md5hash.hexdigest()
#         if not md5hash in hashList:
#             hashList.append(md5hash)
#             imgList.append(file)

# print(hashList)
# print(imgList)


# import shutil

# newDir = "organized"

# try:
#     os.mkdir(newDir)
# except: 
#     print("Directory already existed.")    
    
# for img in imgList:
#     shutil.copy2(os.path.join("images", img), os.path.join(newDir, img))
    

# ------------------------------------------------------------------------------------
