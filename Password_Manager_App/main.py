from tkinter import *
from tkinter import messagebox
p1=None
p2=None
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    if len(input3.get())!=0 or len(input4.get())!=0:
        messagebox.showerror("Error", "Password field already has content!\nClear to generate again.")
    # Password Generator Project
    else:
        import random
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                   'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                   'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        nr_letters = random.randint(8, 10)
        nr_symbols = random.randint(2, 4)
        nr_numbers = random.randint(2, 4)

        # for char in range(nr_letters):
        #     password_list.append(random.choice(letters))
        password_list = [random.choice(letters) for _ in range(nr_letters)]

        # for char in range(nr_symbols):
        #     password_list += random.choice(symbols)
        password_list = password_list + [random.choice(symbols) for _ in range(nr_symbols)]

        # for char in range(nr_numbers):
        #     password_list += random.choice(numbers)
        password_list =password_list + [random.choice(numbers) for _ in range(nr_numbers)]

        random.shuffle(password_list)

        # password = ""
        # for char in password_list:
        #     password += char
        password= "".join(password_list)

        input3.insert(END, password)
        input4.insert(END, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    prompt = None
    if len(input1.get())==0 or len(input2.get())==0 or len(input3.get())==0 or len(input4.get())==0:
        messagebox.showerror("Error", "Please enter details in all fields!")
    else:
        with open('data.txt', 'a+') as file:
            file.seek(0)
            for x in file.readlines():
                if input1.get() in x and input2.get() in x:
                    prompt = messagebox.askyesno("Warning", "A password for this website and email/username already exists!\nDo you wanna overwrite it?")
                    break
            if prompt:
                if input3.get()==input4.get():
                    file.seek(0)
                    file.truncate()
                    file.write(f"{input1.get()} | {input2.get()} | {input3.get()}\n")
                    input1.delete(0, END)
                    input2.delete(0, END)
                    input3.delete(0, END)
                    input4.delete(0, END)
                    messagebox.showinfo("Info", "Password successfully overwritten!")
                    return
                else:
                    messagebox.showerror("Error", "Passwords don't match!")
            elif prompt==False:
                messagebox.showinfo("Password already exists!", "The password was not overwritten!")
            else:
                if input3.get()==input4.get():
                    file.write(f"{input1.get()} | {input2.get()} | {input3.get()}\n")
                    input1.delete(0, END)
                    input2.delete(0, END)
                    input3.delete(0, END)
                    input4.delete(0, END)
                    messagebox.showinfo("Info", "Password successfully saved!")
                    return
                else:
                    messagebox.showerror("Error", "Passwords don't match!")


def show_password():
    if len(input3.get())==0 or len(input4.get())==0:
        messagebox.showerror("Error", "Please enter passwords to show!")
    else:
        if input3.cget("show")=="*":
            show_password_button.config(text="Hide password")
            input3.config(show= "")
            input4.config(show= "")
        else:
            show_password_button.config(text="Show password")
            input3.config(show="*")
            input4.config(show="*")

# ---------------------------- UI SETUP ------------------------------- #
window= Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo = PhotoImage(file="logo.png")
canvas = Canvas(window, width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

label1 = Label(window, text="Website: ")
label1.grid(row=1, column=0)

input1 = Entry(window, width=47)
input1.grid(row=1, column=1,columnspan=2)
input1.focus()

label2 = Label(window, text="Email/Username: ")
label2.grid(row=2, column=0)

input2 = Entry(window, width=47)
input2.grid(row=2, column=1,columnspan=2)

label3 = Label(window, text="Password: ")
label3.grid(row=3, column=0)

input3 = Entry(window, width=33, show = "*")
input3.grid(row=3, column=1,columnspan=1)

label4 = Label(window, text="Retype password: ")
label4.grid(row= 4, column=0)

input4 = Entry(window, width=33, show = "*")
input4.grid(row=4, column=1,columnspan=1)

show_password_button = Button(window, text="Show Password", width =11,command= show_password)
show_password_button.grid(row=3, column=2)

generate_button= Button(window,text= "Generate",highlightthickness=0,width=8,command=generate_password)
generate_button.grid(row=4, column=2)

add_button= Button(window,text="Add",highlightthickness=0,width=39, command= save_password)
add_button.grid(row=5, column=1, columnspan=2)
window.mainloop()