from tkinter import *

root = Tk()
root.geometry("420x550") # Set GUI dimensions
root.title("Data Mining - Group 5")

def process():
    inputs = []
    print(educ_level.get(), inst_level.get())

    if educ_level.get() == "School":
        inputs.append(0)
    elif educ_level.get() == "University":
        inputs.append(1)
    elif educ_level.get() == "College":
        inputs.append(2)

    if inst_level.get() == "Public":
        inputs.append(0)
    elif inst_level.get() == "Private":
        inputs.append(1)

    if gender.get() == "Male":
        inputs.append(0)
    elif gender.get() == "Female":
        inputs.append(1)

    inputs.append(age.get())
    
    if device.get() == "Mobile":
        inputs.append(0)
    elif device.get() == "Computer":
        inputs.append(1)
    elif device.get() == "Tab":
        inputs.append(2)

    if if_IT.get() == "Yes":
        inputs.append(0)
    elif if_IT.get() == "No":
        inputs.append(1)

    if type_loc.get() == "Rural":
        inputs.append(0)
    elif type_loc.get() == "Town":
        inputs.append(1)

    if finance.get() == "Poor":
        inputs.append(0)
    elif finance.get() == "Mid":
        inputs.append(1)
    elif finance.get() == "Rich":
        inputs.append(2)

    if internet.get() == "Mobile Data":
        inputs.append(0)
    elif internet.get() == "Wi-Fi":
        inputs.append(1)

    if network.get() == "4G":
        inputs.append(0)
    elif network.get() == "3G":
        inputs.append(1)
    elif network.get() == "2G":
        inputs.append(2)

    print("Inputs:", inputs)


# DOCU: This block of codes will render the headings in GUI
title = Label(root, text = "Student Flexibility in Online Learning", font = ("Arial Bold", 15), bg = "#202020", fg = "white", padx = 30, pady = 10).pack(fill = X)
instruction = Label(root, text = "Please answer the following required fields.", anchor = "w", font = ("Comic Sans", 11), padx = 10, pady = 5).pack(fill = "both")

# DOCU: This block of codes will render the input fields in GUI
frame1 = Frame(root)
frame1.place(x = 0, y = 100)
educ_level = StringVar()
educ_level.set("School")
educ_level_label = Label(frame1, text = "Q1: What is your education level?", anchor = "w", font = ("Comic Sans", 11), padx = 10, pady = 5).pack(fill = "x", side = "left")
educ_level_menu = OptionMenu(frame1, educ_level, "School", "University", "College").pack(fill = "x", side = "left")

frame2 = Frame(root)
frame2.place(x = 0, y = 130)
inst_level = StringVar()
inst_level.set("Public")
inst_level_label = Label(frame2, text = "Q2: What is your institution type?", anchor = "w", font = ("Comic Sans", 11), padx = 10, pady = 5).pack(fill = "x", side = "left")
inst_level_menu = OptionMenu(frame2, inst_level, "Public", "Private").pack(fill = "x", side = "left")

frame3 = Frame(root)
frame3.place(x = 0, y = 160)
gender = StringVar()
gender.set("Male")
gender_label = Label(frame3, text = "Q3: What is your gender?", anchor = "w", font = ("Comic Sans", 11), padx = 10, pady = 5).pack(fill = "x", side = "left")
gender_menu = OptionMenu(frame3, gender, "Male", "Female").pack(fill = "x", side = "left")

frame4 = Frame(root)
frame4.place(x = 0, y = 190)
age = IntVar()
age_label = Label(frame4, text = "Q4: What is your age?", anchor = "w", font = ("Comic Sans", 11), padx = 10, pady = 5).pack(fill = "x", side = "left")
age_entry = Entry(frame4, textvariable = age).pack(fill = "x", side = "left")

frame5 = Frame(root)
frame5.place(x = 0, y = 220)
device = StringVar()
device.set("Mobile")
device_label = Label(frame5, text = "Q5: What device do you use?", anchor = "w", font = ("Comic Sans", 11), padx = 10, pady = 5).pack(fill = "x", side = "left")
device_menu = OptionMenu(frame5, device, "Mobile", "Computer", "Tab").pack(fill = "x", side = "left")

frame6 = Frame(root)
frame6.place(x = 0, y = 250)
if_IT = StringVar()
if_IT.set("Yes")
if_IT_label = Label(frame6, text = "Q6: Are you an IT student?", anchor = "w", font = ("Comic Sans", 11), padx = 10, pady = 5).pack(fill = "x", side = "left")
if_IT_menu = OptionMenu(frame6, if_IT, "Yes", "No").pack(fill = "x", side = "left")

frame7 = Frame(root)
frame7.place(x = 0, y = 280)
type_loc = StringVar()
type_loc.set("Rural")
type_loc_label = Label(frame7, text = "Q7: Is your location an urban or town area?", anchor = "w", font = ("Comic Sans", 11), padx = 10, pady = 5).pack(fill = "x", side = "left")
type_loc_menu = OptionMenu(frame7, type_loc, "Rural", "Town").pack(fill = "x", side = "left")

frame8 = Frame(root)
frame8.place(x = 0, y = 310)
finance = StringVar()
finance.set("Poor")
finance_label = Label(frame8, text = "Q8: What is your financial condition?", anchor = "w", font = ("Comic Sans", 11), padx = 10, pady = 5).pack(fill = "x", side = "left")
finance_menu = OptionMenu(frame8, finance, "Poor", "Mid", "Rich").pack(fill = "x", side = "left")

frame9 = Frame(root)
frame9.place(x = 0, y = 340)
internet = StringVar()
internet.set("Mobile Data")
internet_label = Label(frame9, text = "Q9: What is your internet type?", anchor = "w", font = ("Comic Sans", 11), padx = 10, pady = 5).pack(fill = "x", side = "left")
internet_menu = OptionMenu(frame9, internet, "Mobile Data", "Wi-Fi").pack(fill = "x", side = "left")

frame10 = Frame(root)
frame10.place(x = 0, y = 370)
network = StringVar()
network.set("4G")
network_label = Label(frame10, text = "Q10: What is your network type?", anchor = "w", font = ("Comic Sans", 11), padx = 10, pady = 5).pack(fill = "x", side = "left")
network_menu = OptionMenu(frame10, network, "4G", "3G", "2G").pack(fill = "x", side = "left")

# DOCU: This block of codes will render the buttons in GUI
submit_frame = Frame(root)
submit_frame.place(x = 300, y = 400)
submit = Button(submit_frame, text = "Submit", command = process, font = ("Comic Sans", 10), bg = "#0066A2", fg = "white", activebackground = "#0066A2", activeforeground = "white", padx = 20).pack(fill = "x", side = "right", padx = 10)

root.mainloop()