from tkinter import *
from tkinter import messagebox

window = Tk()
window.title(' BMI CALCULATOR ')
window.geometry('500x500')
window.config(bg='skyblue')

def reset():
    age_tf.delete(0,'end')
    height_tf.delete(0,'end')
    weight_tf.delete(0,'end')

def calculate_bmi():
    kg = int(weight_tf.get())
    m = int(height_tf.get())/100
    bmi = kg/(m*m)
    bmi = round(bmi, 1)
    bmi_index(bmi)

def bmi_index(bmi):
    
    if bmi < 18.5:
        messagebox.showinfo(' BMI CALCULATOR ', f'BMI = {bmi} is Underweight')
    elif (bmi > 18.5) and (bmi < 24.9):
        messagebox.showinfo(' BMI CALCULATOR ', f'BMI = {bmi} is Normal')
    elif (bmi > 24.9) and (bmi < 29.9):
        messagebox.showinfo(' BMI CALCULATOR ', f'BMI = {bmi} is Overweight')
    elif (bmi > 29.9) and (bmi<39.9):
        messagebox.showinfo(' BMI CALCULATOR ', f'BMI = {bmi} is Obesity') 
    else:
        messagebox.showinfo(' BMI CALCULATOR ', f'BMI = {bmi} is Extreme Obesity')   

var = IntVar()

frame = Frame(window,padx=70, pady=50,bg='black')
frame.pack(expand=True)

age_lb = Label(frame,text="  Enter Age(2-120) ",bg='lightgreen')
age_lb.grid(row=1, column=1,padx=10)

age_tf = Entry(frame,bg='lightgreen' )
age_tf.grid(row=1, column=2, pady=10)

gen_lb = Label(frame,text='     Select Gender     ',bg='lightgreen')
gen_lb.grid(row=2, column=1,padx=10)

frame2 = Frame(frame)
frame2.grid(row=2, column=2, pady=10)

male_rb = Radiobutton(frame2,text = 'Male',variable = var,value = 1,bg='lightgreen')
male_rb.pack(side=LEFT)

female_rb = Radiobutton(frame2,text = 'Female',variable = var,value = 2,bg='lightgreen')
female_rb.pack(side=RIGHT)

height_lb = Label(frame,text="Enter Height (cm)  ",bg='lightgreen')
height_lb.grid(row=3, column=1)

weight_lb = Label(frame,text="Enter Weight (kg)  ",bg='lightgreen')
weight_lb.grid(row=4, column=1)

height_tf = Entry(frame,bg='lightgreen')
height_tf.grid(row=3, column=2, pady=10)

weight_tf = Entry(frame,bg='lightgreen')
weight_tf.grid(row=4, column=2, pady=10)

frame3 = Frame(frame,bg='black')
frame3.grid(row=5, columnspan=3, pady=10)

cal_btn = Button(frame3,text='Calculate',command=calculate_bmi,bg='green')
cal_btn.pack(side=LEFT,padx=20,)

reset_btn = Button(frame3,text=' Reset ',command=reset,bg='yellow')
reset_btn.pack(side=LEFT,padx=20)

exit_btn = Button(frame3,text='  Exit  ',command=lambda:window.destroy(),bg='red')
exit_btn.pack(side=RIGHT,padx=20)

window.mainloop()