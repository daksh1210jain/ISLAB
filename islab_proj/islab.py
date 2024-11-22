from tkinter import *
import socket
from tkinter import filedialog
from tkinter import messagebox
import os 
from PIL import Image, ImageTk

root=Tk()
root.title("ShareIt")
root.geometry("450x560+500+200")
root.configure(bg="#f4fdfe")
root.resizable(False,False)

def Send():
    window = Toplevel(root)
    window.geometry("450x560+500+200")
    window.configure(bg="#f4fdfe")
    window.resizable(False, False)
    def select_file():
        global filename
        filename = filedialog.askopenfilename(initialdir=os.getcwd(),title='Select_Image_File',filetype=(('file_type','*.txt'),('all files','*.*')))
    def sender():
        s=socket.socket()
        host=socket.gethostname()
        port=8080
        s.bind((host,port))
        s.listen(1)
        print(host)
        print('waiting for incoming connections....')
        conn,addr=s.accept()
        file=open(filename,'rb')
        file_data = file.read(1024)
        conn.send(file_data)
        print("Data Transmitted")

    upper_frame = Frame(window, bg="#f4fdfe", width=450, height=280)  # Blue background
    upper_frame.place(x=0, y=0)
    lower_frame = Frame(window, bg="#FFFFFF", width=450, height=280)  # White background
    lower_frame.place(x=0, y=280)
    Button(upper_frame, text="+ Select File", width=12, height=1, font="arial 14 bold", bg="#fff", fg="#000",command=select_file).place(x=50, y=100)
    Button(upper_frame, text="SEND", width=8, height=1, font="arial 14 bold", bg="#000", fg="#fff",command=sender).place(x=300, y=100)
    image_path = "images/sender.jfif"  # Replace with your actual image path
    bg_image = Image.open(image_path)
    bg_image = bg_image.resize((450, 280), Image.LANCZOS)  # Resize to fit the lower frame
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = Label(lower_frame, image=bg_photo, bg="#FFFFFF")
    bg_label.image = bg_photo  
    bg_label.place(x=0, y=0)  
    host = socket.gethostname()
    Label(window, text=f'ID: {host}', bg='white', fg='black', font=("Arial", 12, "bold")).place(x=140, y=290)
    window.mainloop()

def Receive():
    main = Toplevel(root)
    main.title("Receive")
    main.geometry("450x560+500+200")
    main.configure(bg="#f4fdfe")
    main.resizable(False,False)
    def receiver():
        ID=SenderID.get()
        filename1=incoming_file.get()
        s=socket.socket()
        port=8080
        s.connect((ID,port))
        file=open(filename1,'wb')
        file_data=s.recv(1024)
        file.write(file_data)
        file.close()
        print("file received successfully")
    image_icon2 = PhotoImage(file="images/receive.png")
    main.iconphoto(False,image_icon2)
    
    upper_frame = Frame(main, bg="#f4fdfe", width=450, height=280)  
    upper_frame.place(x=0, y=280)
    lower_frame = Frame(main, bg="#FFFFFF", width=450, height=280)  
    lower_frame.place(x=0, y=0)
    image_path = "images/receive.jpg"
    Label(main,text="Input sender id",font=('arial',10,'bold'),bg='#f4fdfe').place(x=20,y=340)
    SenderID = Entry(main,width=25,fg='black',border=2,bg='white',font=('arial',15))
    SenderID.place(x=20,y=370)
    SenderID.focus()
    Label(main,text="File name for the incoming file",font=('arial',10,'bold'),bg='#f4fdfe').place(x=20,y=420)
    incoming_file = Entry(main,width=25,fg='black',border=2,bg='white',font=('arial',15))
    incoming_file.place(x=20,y=450)
    rr=Button(main,text="Receive",width=13,bg="#39c790",font="arial 14 bold",command=receiver)
    rr.place(x=20,y=500)
    bg_image = Image.open(image_path)
    bg_image = bg_image.resize((450, 280), Image.LANCZOS)  
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = Label(lower_frame, image=bg_photo, bg="#FFFFFF")
    bg_label.image = bg_photo  
    bg_label.place(x=0, y=0)  
    main.mainloop()
#icon
image_icon = PhotoImage(file="images/icon.png")
root.iconphoto(False,image_icon)
Label(root,text="File Transfer",font=('Acumin Variable Concept',20,'bold'),bg='#f4fdfe').place(x=20,y=30)

send_image_path = "images/send.png"  
send_image = Image.open(send_image_path)
send_image = send_image.resize((100, 100), Image.LANCZOS)  # Resize to 50x50
send_photo = ImageTk.PhotoImage(send_image)

# Create the "send" button
send = Button(root, image=send_photo, bg="#f4fdfe", bd=0,command=Send)
send.place(x=50, y=100)

# Add a label for the "send" button
send_label = Label(root, text="Send", font=("Acumin Variable Concept", 10,"bold"), bg="#f4fdfe")
send_label.place(x=80, y=210) 

# Load and resize the "receive" image
receive_image_path = "images/receive.png"  # Replace with your actual image path
receive_image = Image.open(receive_image_path)
receive_image = receive_image.resize((100, 100), Image.LANCZOS)  # Resize to 50x50
receive_photo = ImageTk.PhotoImage(receive_image)

# Create the "receive" button
receive = Button(root, image=receive_photo, bg="#f4fdfe", bd=0,command=Receive)
receive.place(x=300, y=100)

# Add a label for the "receive" button
receive_label = Label(root, text="Receive", font=("Acumin Variable Concept", 10,"bold"), bg="#f4fdfe")
receive_label.place(x=328, y=210)

background_image_path = "images/background.png"  # Replace with your actual image path
background_image = Image.open(background_image_path)
background_image = background_image.resize((450, 350), Image.LANCZOS)  # Resize to fit the area below buttons
background_photo = ImageTk.PhotoImage(background_image)

# Add the resized background image below the buttons
background_label = Label(root, image=background_photo)
background_label.place(x=0, y=250) 

root.mainloop()
