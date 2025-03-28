from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
import json

# ---------------------------- SEARCH FINDER ------------------------------- #
def search():
    search = website_entry.get()
    search = search.capitalize()
    try:
        with open('data.json','r') as data_file:
            data = json.load(data_file)
            data_list = [(key, value) for (key,value) in data[search].items()]
            messagebox.showinfo(title=f"{search}", message=f"Email: {data_list[0][1]}\nPassword: {data_list[1][1]}")
            pyperclip.copy(f" '{data_list[0][1]}'   |   '{data_list[1][1]}'" )
    except KeyError as key_error:
        messagebox.showerror(title=f'{key_error}', message=f'The Key {key_error} Was Not Found.')
    except json.decoder.JSONDecodeError:
        messagebox.showerror(title=f'Expecting Value', message="No Data File Found.")
    except FileNotFoundError:
        messagebox.showerror(title=f'Error', message="File Not Found.")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    password_entry.focus()
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letter + password_symbols + password_numbers
    shuffle(password_list)

    password = ''.join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get().capitalize()
    email = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            'password': password
        }
    }
    if website_entry.get() == '' or email_username_entry.get() == '' or password_entry.get() == '':
        error_message = messagebox.showerror(title='Error', message="Nothing was type in any of the three boxes try to fill the boxes!")
    else:
        try:
            with open('data.json', mode='r') as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open('data.json', mode='w') as data_file:
                #Create a file with data
                json.dump(new_data, data_file, indent=4)
        except json.decoder.JSONDecodeError:
            with open('data.json', mode='w') as data_file:
                #Add data to the existing file
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open('data.json', mode='w') as data_file:
                #Saving the update data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)
            website_entry.focus()
# ---------------------------- UI SETUP ------------------------------- #
#Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#Canvas
canvas = Canvas(width=200, height=200)
image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

#Labels
website_label = Label()
website_label.config(text="Website:")
website_label.grid(column=0, row=1)

email_username_label = Label()
email_username_label.config(text="Email/Username:")
email_username_label.grid(column=0, row=2)

password_label = Label()
password_label.config(text="Password: ")
password_label.grid(column=0, row=3)

#Buttom
generate_password_buttom = Button(text='Generate Password', command=password_generator)
generate_password_buttom.grid(column=2, row=3)

add_buttom = Button(text='Add', width=36, command=save_data)
add_buttom.grid(column=1, row=4, columnspan=2)

search_buttom = Button(text="Search", width=15, command=search)
search_buttom.grid(column=2, row=1,columnspan=2)

#Entry
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()                               #When laungh the app the courser will start that entry

email_username_entry = Entry(width=35)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(END, 'yonelvynpython@gmail.com')        #When launch the app will 'email' will be put it automatically

password_entry = Entry(width=21, show='*')
password_entry.grid(column=1, row=3)

window.mainloop()


