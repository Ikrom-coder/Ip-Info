from tkinter import *
from tkinter import ttk
import requests
import webbrowser

my_ip_public = requests.get('https://api.ipify.org').text

master = Tk()
master.title('IP Info')
# master.iconbitmap('assets/appipic.ico')
master.geometry("900x600")

number = StringVar()


def ip_info_getter():
    width = 0
    height = 100
    number2 = (number.get())
    response = requests.get(f"http://ip-api.com/json/{str(number2)}").json()
    for k, v in response.items():
        ttk.Label(master, text=f'{k} -> {v}', font='Arial 15').place(x=width, y=height)
        height += 30


def cleaner():
    width = 0
    height = 100
    number2 = (number.get())
    response = requests.get(f"http://ip-api.com/json/{str(number2)}").json()
    for i in response.items():
        ttk.Label(master, text=" "*700, font='Arial 15').place(x=width, y=height)
        height += 30


def callback(url):
   webbrowser.open_new_tab(url)


ttk.Label(master, text='If you do not know your public IP address visit to the site ->').place(x=1, y=6)
link = ttk.Label(master, text='alltechtools.com/my_ip.asp').place(x=350, y=6)
# link.bind("<Button-1>", lambda e: callback("alltechtools.com/my_ip.asp"))
ttk.Label(master, text=f'Public IP Address of this computer: {str(my_ip_public)}').place(x=1, y=25)
ttk.Label(master, text='Write IP Address:', font='Arial 20').place(x=1, y=50)
e1 = Entry(master, textvariable=number, width=40).place(x=220, y=60)
btn = ttk.Button(master, text='Get Info', width=10, command=ip_info_getter).place(x=500, y=58)
btn_clear = ttk.Button(master, text='Clear', width=10, command=cleaner).place(x=600, y=58)

master.mainloop()
