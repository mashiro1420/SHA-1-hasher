import hashlib
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import os


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.lb_title = tk.Label(self, text="Biến chuỗi thành hash")
        self.lb_input = tk.Label(self, text="Nhập chuỗi:")
        # self.tx_string = Entry(self, width = 30)
        self.tx_string = Text(self, width = 30, height = 4)
        self.btn_hash = Button(self, text="Tính", command=self.confirm_hash_string, width=15)
        self.lb_output = tk.Label(self, text="Kết quả:")
        self.lb_result = tk.Label(self, text='')
        self.lb_title.pack(side="top", fill="none", expand=False)
        self.lb_input.place(x=35, y=50)
        self.tx_string.place(x=110, y=30)
        self.btn_hash.place(x=140, y=110)
        self.lb_output.place(x=175, y=150)
        self.lb_result.place(x=70, y=180)
    def confirm_hash_string(self):
        # hash = hash_string(self.tx_string.get())
        hash = hash_string(self.tx_string.get("1.0",'end-1c'))
        self.lb_result.config(text=hash)

class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.lb_title = tk.Label(self, text="Biến file thành hash")
        self.lb_input = tk.Label(self, text="Chọn file:")
        self.btn_upload = Button(self, text="Upload", command=self.upload_file, width = 15)
        self.btn_hash = Button(self, text="Tính", command=self.confirm_hash_file, width=15)
        self.lb_output = tk.Label(self, text="Kết quả:")
        self.lb_result = tk.Label(self, text='')
        self.lb_title.pack(side="top", fill="none", expand=False)
        self.lb_input.place(x=70, y=30)
        self.btn_upload.place(x=140, y=30)
        self.btn_hash.place(x=140, y=70)
        self.lb_output.place(x=175, y=110)
        self.lb_result.place(x=70, y=150)
    def upload_file(self):
        self.filename = upload()
    def confirm_hash_file(self):
        hash = hash_file(self.filename)
        self.lb_result.config(text=hash)

class Page3(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.lb_title = tk.Label(self, text="So sánh 2 file")
        self.lb_input1 = tk.Label(self, text="Chọn file thứ nhất:")
        self.btn_upload1 = Button(self, text="Upload first file", command=self.upload_file1, width = 20)
        self.lb_input2 = tk.Label(self, text="Chọn file thứ hai:")
        self.btn_upload2 = Button(self, text="Upload second file", command=self.upload_file2, width = 20)
        self.btn_hash = Button(self, text="Tính", command=self.confirm_compare, width=15)
        self.lb_output = tk.Label(self, text="Kết quả:")
        self.lb_result = tk.Label(self, text='')
        self.lb_title.pack(side="top", fill="none", expand=False)
        self.lb_input1.place(x=70, y=30)
        self.btn_upload1.place(x=180, y=30)
        self.lb_input2.place(x=70, y=70)
        self.btn_upload2.place(x=180, y=70)
        self.btn_hash.place(x=140, y=110)
        self.lb_output.place(x=175, y=150)
        self.lb_result.place(x=145, y=190)
    def upload_file1(self):
        self.filename1 = upload()
        self.btn_upload1.config(text="Đã chọn")
    def upload_file2(self):
        self.filename2 = upload()
        self.btn_upload2.config(text="Đã chọn")
    def confirm_compare(self):
        hash1 = hash_file(self.filename1)
        size1 = size_file(self.filename1)
        hash2 = hash_file(self.filename1)
        size2 = size_file(self.filename1)
        if(size1 == size2 and hash1 == hash2):
            self.lb_result.config(text="Hai file giống nhau")
        else:
            self.lb_result.config(text="Hai file khác nhau")

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)   
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)        

        b1 = tk.Button(buttonframe, text="Băm hàm", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Băm file", command=p2.lift)    
        b3 = tk.Button(buttonframe, text="So sánh file", command=p3.lift)      

        b1.pack(side="left")
        b2.pack(side="left")     
        b3.pack(side="left")     

        p1.show()

def hash_string(string):
        hash = hashlib.sha1()
        hash.update(string.encode())
        return hash.hexdigest()

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


def upload():
    filename = filedialog.askopenfilename(initialdir = "/Schoolwork/Nam 4 ky 1/T2 - An toan bao mat thong tin/",
                                          title = "Select a File",
                                          filetype = (('Text files', '*.txt'),("All files", "*.*")))
    return filename

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x250")
    root.mainloop()