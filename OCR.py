import cv2
import pytesseract
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image


def scan():
    
    def select():
        global file
        file = filedialog.askopenfilename()

        img = Image.open(file)

        img = img.resize((400, 300), Image.ANTIALIAS)

        img = ImageTk.PhotoImage(img)

        panel = Label(SCAN,image = img)

        panel.image = img
        l3 = Label(SCAN,text="IMAGE PREVIEW",font=("Cambria",15),bg='aqua',padx=20,pady=10).pack()
        panel.pack()
        l4 = Label(SCAN,text="       ",font=("Arial",5),bg='aqua',padx=20,pady=3).pack()
        btn1 = Button(SCAN,text="PROCESS",padx=8,font=("",10),bg='aqua',activebackground="aqua",relief=GROOVE,command=process).pack()
        
    def process():
        pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
        originalImage = cv2.imread(file)
        grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)

        originalImage = cv2.imread(file)


        img = cv2.imwrite('D:/black-and-white.png',grayImage)
        Text = pytesseract.image_to_string('D:/black-and-white.png')
        l5 = Label(SCAN,text="The Image has been Processed",font=("Arial",15),bg='cyan',padx=20,pady=10).pack()


        myfile = open(r'File.txt','w+')
        myfile.write(Text)
        myfile.close()

        frame = LabelFrame(window,text='',padx=50,pady=50)
        frame.pack(padx=10,pady=10)

        
        OUTPUT = Toplevel(window)
        OUTPUT.title("EXTRACTED TEXT")
        OUTPUT.geometry('600x600')
        OUTPUT.config(bg="#fa8072")

        l6 = Label(OUTPUT,text="EXTRACTED TEXT",font=("Times New Roman bold",27),bg='#fa8072',padx=20,pady=10).pack()
        l7 = Label(OUTPUT,text=Text,font=("Cambria",13),bg='#fa8072',padx=20,pady=10).pack()
        l8 = Label(OUTPUT,text="The Above Text is Saved as an Editable (.txt) file which is saved in the current directory",bg="#fa8072",font=("Goudy old style",12)).pack()
    
    
    SCAN = Toplevel(window)
    SCAN.title("PROCESSING")
    SCAN.geometry('960x600')
    SCAN.config(bg="cyan")
    l = Label(SCAN,text='WELCOME TO SCAN IT',font=("Arial",30),bg='aqua',padx=20,pady=10).pack()
    l1 = Label(SCAN,text='Click Here to Select the Image (jpg/png/jpeg/jfif/)',font=("Arial",15),bg='aqua',padx=20,pady=10).pack()
    Btn = Button(SCAN,text="CHOOSE",padx=8,font=("",10),bg='aqua',activebackground="aqua",relief=GROOVE,command=select).pack()
    
window = Tk()
window.title('OCR')
window.iconbitmap(r'OCRICON.ico')
window.configure(bg='yellow')
window.geometry('600x600')

Img = ImageTk.PhotoImage(Image.open(r"ocrimg1.png"))
label = Label(image=Img,bg="yellow").pack()


l6 = Label(window,text="       ",font=("Arial",15),bg='yellow',padx=20,pady=5).pack()
btn = Button(window,text="SCAN IT!",font=('Arial',50),relief=GROOVE,bg="yellow",activebackground="yellow",command=scan).pack()

l2 = Label(window,text="DIGITALIZE YOUR DOCUMENTS!!",font=('Arial',15,'underline'),bg="yellow").pack()

window.mainloop()