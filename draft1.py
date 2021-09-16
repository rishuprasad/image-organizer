# import hashlib

# print(hashlib.md5(b"The quick brown fox jumps over the lazy dog"))

# image_file = open('img1.png')
# print(hashlib.md5(image_file).hexdigest())


# import hashlib
# m = hashlib.md5()
# m.update(b"The quick brown fox jumps over the lazy dog")
# print(m.hexdigest())

import hashlib
from PIL import Image

import pandas as pd
import pyodbc 

import imghdr



# img = Image.open(".\images\img2.png")
# imgBytes = img.tobytes()
# md5Hash = hashlib.md5(imgBytes)
# # with io.BytesIO() as memf:
# #     img.save(memf, 'PNG')
# #     data = memf.getvalue()
# #     m.update(data)
# print(md5Hash.hexdigest())




# import os module
import os
    
# varify the path using getcwd()
cwd = os.getcwd()
  
# print the current directory
print("Current working directory is:", cwd)



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
# Organizing images from an SQL database 
    
# Server: DESKTOP-CEMA4M6
# Database: ImageDB
# Table: dbo.tbl_images


connection = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-CEMA4M6;'
                      'Database=ImageDB;'
                      'Trusted_Connection=yes;')

cursor = connection.cursor()

# cursor.execute('SELECT * FROM database_name.table')



# sql_query = pd.read_sql_query('SELECT * FROM ImageDB.dbo.tbl_images', connection)
# print(sql_query)
# print(type(sql_query))


# import pymssql

# server = "DESKTOP-CEMA4M6"
# user = "sa"
# password
# db = 


# pymssql.connect()
# conn = pymssql.connect(server, user, password, "tempdb")
# cursor = conn.cursor(as_dict=True)


# input_hash = "asdfasdfasdfasdf"

select_hash = """
select count(*) from ImageDB.dbo.tbl_images
where HashMD5='{}'
"""

insert_img1 = """
insert into ImageDB.dbo.tbl_images 
(ImageFileName, Path, HashMD5, ImageFile) 
values 
(?, ?, ?, ?)
"""

insert_img2 = """
insert into ImageDB.dbo.tbl_images 
(ImageFileName, Path, HashMD5) 
values 
(?, ?, ?)
"""

# sql_query = pd.read_sql_query(select_hash.format(input_hash), connection)
# cursor.execute(select_hash)
# for row in cursor:
#     print(type(row))
#     print(row == 1)
# print(type(sql_query))
# print(sql_query[''][0])
# if sql_query[''][0] == 0:
#     img = Image.open(os.path.join("images", file))


os.chdir(r"C:\Data\Programming\Programs\Python\Image Organizer")
parent_dir = os.getcwd()

imgDirectory_str = r"C:\Data\Programming\Programs\Python\Image Organizer\images" 
imgDirectory = os.walk(imgDirectory_str) 



# # # # Add exif data column
# # # # Add storage column
# # # # Add keyword column

# # # # Think about universal saving (can have different input ext, but only save in jpg?)
# # # # Make a GUI
# # # # Create a cross-platform app (IOS, Android, etc.)
# # # # Search by keyword (show image, enter keyword, next image)
# # # # Pull out exif data (varchar(8000))
        

for roots, directories, files in imgDirectory:
    print((files))
    
    for file in files:
        # Check if each file is an image while traversing
        try:
            img = Image.open(os.path.join(roots, file))
        except:
            continue
    
        # img = Image.open(".\\images\\" + file)
        # img = Image.open(os.path.join("images", file))
        
        # imgBytes = img.tobytes()
        with open(os.path.join(roots, file), "rb") as f:
            imgBytes = bytearray(f.read())
        # print(imgBytes)
        # print(imgBytes)
        md5hash = hashlib.md5(imgBytes)
        md5hash = md5hash.hexdigest()
        print(file)
        print(md5hash)
        input_hash = md5hash
        sql_query = pd.read_sql_query(select_hash.format(input_hash), connection)
        print(imgDirectory_str)
        if sql_query[''][0] == 0:
            print("in")
            # cursor.execute(insert_img.format(str(file), str(os.path.join(imgDirectory)), input_hash, img))
            # print(type(file))
            # print(type(str(imgDirectory)))
            # print(str(imgDirectory))
            # print(type(input_hash))
            # print(type(str(imgBytes)))
            cursor.execute(insert_img1, (file, imgDirectory_str, input_hash, imgBytes))
            # cursor.execute(insert_img2, (file, imgDirectory2, input_hash))
            
print(pd.read_sql_query("select * from ImageDB.dbo.tbl_images", connection))



# import os
# import io
# import PIL.Image as Image

# from array import array

# def readimage(path):
#     count = os.stat(path).st_size / 2
#     with open(path, "rb") as f:
#         return bytearray(f.read())


# df = pd.read_sql_query("select * from ImageDB.dbo.tbl_images", connection)
# # print(df["ImageFile"][8])
# # for bytes in df[]
# for i, ImageFile in enumerate(df["ImageFile"]):
#     # img = Image.open(os.path.join("images", "img1.png"))
#     # bytes1 = img.tobytes()
#     # bytes2 = df["ImageFile"][3]
#     # print(df["HashMD5"])
#     # bytes3 = readimage("images\img1.png")
#     # print(type(bytes2))
#     # print(type(bytes3))
#     # ioBytes = io.BytesIO(bytes2)
#     ioBytes = io.BytesIO(ImageFile)
#     image = Image.open(ioBytes)
#     image.save("testing" + str(i) + ".png")

connection.commit()
cursor.close()
connection.close()


# select_all_desc = """
# select * from ImageDB.dbo.tbl_images
# """

# def execute_query(connection, query):
#     cursor = connection.cursor()
#     try:
#         cursor.execute(query)
#         connection.commit()
#         print("Query executed successfully")
#     except Error as e:
#         print(f"The error '{e}' occurred")

# execute_query(connection, select_all_desc)


    