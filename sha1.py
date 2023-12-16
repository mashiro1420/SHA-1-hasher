import hashlib
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os

def hash_file(filename):
    hash = hashlib.sha1()
    with open(filename,'rb') as file:
       chunk = 0
       while chunk != b'':
           chunk = file.read(1024)
           hash.update(chunk)
    return hash.hexdigest()

def size_file(filename):
    file_stats = os.stat(filename)
    return file_stats.st_size

def hash_string(string):
    hash = hashlib.sha1()
    hash.update(string.encode())
    return hash.hexdigest()

def upload():
    filename = filedialog.askopenfilename(initialdir = "/Schoolwork/Nam 4 ky 1/T2 - An toan bao mat thong tin/",
                                          title = "Select a File",
                                          filetype = (('Text files', '*.txt'),("All files", "*.*")))
    return filename

print("Chương trình tạo hàm băm SHA-1\nChọn 1 - Băm chuỗi\nChọn 2 - Băm file\nChọn 3 - So sánh 2 file")
option = (input("Lựa chọn: "))
while option != "1" and option !="2" and option !="3":
    option = input("Vui lòng chọn lại đúng theo hướng dẫn:")
else:
    option=int(option)
    if option == 1:
        string = input("Nhập chuỗi: ")
        hash = hash_string(string)
        print("Giá trị băm của chuỗi là: ",hash)
    elif option == 2:
        print("Chọn file:")
        filename = upload()
        while filename == '':
            print("Chọn lại file:")
            filename = upload()
        else:
            hash = hash_file(filename)
            print("Giá trị băm của file là: ",hash)
    elif option == 3:
        print("Chọn file thứ nhất: ")
        file1 = upload()
        size1 = size_file(file1)
        hash1 = hash_file(file1)
        print("Chọn file thứ hai: ")
        file2 = upload()
        size2 = size_file(file2)
        hash2 = hash_file(file2)
        if(size1 == size2 and hash1 == hash2):
            print("Hai file giống nhau.")
        else:
            print("Hai file khác nhau.")

