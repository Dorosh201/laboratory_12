from tkinter import *
from tkinter import messagebox

def show():
    global photo
    photo = PhotoImage(file="222.png")
    label6.configure(image=photo)

def inf():
    s = edit4.get()
    if s == "111М":
        messagebox.showinfo("Про спеціальність", edit4.get() + '''\nСпеціальність 111 Математика\nОсвітня програма Комп'ютерна математика''')
    elif s == "СОМ":
        messagebox.showinfo("Про спеціальність", edit4.get() + '''\nСпеціальність 014 Середня освіта\nОсвітня програма Середня освіта. Математика, інформатика''')
    else:
        messagebox.showinfo("Про спеціальність", edit4.get() + "\nТакої спеціальності на факультеті немає")

root = Tk()
root.title('Анкета')
root.geometry('400x600+500+100')
root.configure(bg='skyblue')

label1 = Label(root, text="Прізвище:", font=('Arial', 12, 'bold'), bg='skyblue')
label1.place(x=20, y=20)
edit1 = Entry(root, width=25, font=('Arial', 11), bd=3, relief="ridge")
edit1.place(x=150, y=20)

label2 = Label(root, text="Ім'я:", font=('Arial', 12, 'bold'), bg='skyblue')
label2.place(x=20, y=60)
edit2 = Entry(root, width=25, font=('Arial', 11), bd=3, relief="ridge")
edit2.place(x=150, y=60)

label3 = Label(root, text="По батькові:", font=('Arial', 12, 'bold'), bg='skyblue')
label3.place(x=20, y=100)
edit3 = Entry(root, width=25, font=('Arial', 11), bd=3, relief="ridge")
edit3.place(x=150, y=100)

label_gender = Label(root, text="Стать:", font=('Arial', 12, 'bold'), bg='skyblue')
label_gender.place(x=20, y=140)
Checkbutton1 = Checkbutton(root, text="чоловіча", font=('Arial', 10), bg='skyblue')
Checkbutton1.place(x=150, y=140)
Checkbutton2 = Checkbutton(root, text="жіноча", font=('Arial', 10), bg='skyblue')
Checkbutton2.place(x=250, y=140)

label4 = Label(root, text="Курс:", font=('Arial', 12, 'bold'), bg='skyblue')
label4.place(x=20, y=180)
result1 = IntVar()
result1.set(1)
Radiobutton1 = Radiobutton(root, text="1", variable=result1, value=1, font=('Arial', 10), bg='skyblue')
Radiobutton1.place(x=150, y=180)
Radiobutton2 = Radiobutton(root, text="2", variable=result1, value=2, font=('Arial', 10), bg='skyblue')
Radiobutton2.place(x=200, y=180)
Radiobutton3 = Radiobutton(root, text="3", variable=result1, value=3, font=('Arial', 10), bg='skyblue')
Radiobutton3.place(x=250, y=180)
Radiobutton4 = Radiobutton(root, text="4", variable=result1, value=4, font=('Arial', 10), bg='skyblue')
Radiobutton4.place(x=300, y=180)

label5 = Label(root, text="Спеціальність:", font=('Arial', 12, 'bold'), bg='skyblue')
label5.place(x=20, y=220)
edit4 = Entry(root, width=25, font=('Arial', 11), bd=3, relief="ridge")
edit4.place(x=150, y=220)

button1 = Button(root, text="Про спеціальність", width=20, font=('Arial', 10, 'bold'), bg='lightblue', command=inf)
button1.place(x=120, y=270)

label6 = Label(root, bg='skyblue')
label6.place(x=100, y=320, width=200, height=150)

button2 = Button(root, text="Фото", width=20, font=('Arial', 10, 'bold'), bg='lightgreen', command=show)
button2.place(x=120, y=500)

root.mainloop()