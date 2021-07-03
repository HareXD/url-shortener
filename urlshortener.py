from tkinter import *
import pyshorteners
import pyperclip

root = Tk()
root.title("URL Shortener")
root.geometry("260x210")
root.resizable(False, False)
root.columnconfigure(0,weight=1)
root.configure(bg="gray77")

url = StringVar()
url_address = StringVar()

def urlshortener():
    urladdress=url.get()
    url_short=pyshorteners.Shortener().tinyurl.short(urladdress)
    url_address.set(url_short)

def copyurl():
    url_short=url_address.get()
    pyperclip.copy(url_short)

main_label = Label(root,text="Paste Your URL Here:",font=("Cascadia Code",15,"bold"),bg="gray77").grid()
url_entry = Entry(root,textvariable=url,relief="ridge",borderwidth=4,width=24).grid()
generate_button = Button(root,text="Generate Shortened URL",command=urlshortener,relief="ridge",borderwidth=4,bg="gray88").grid()
shortened_url_label = Label(root,text="Shortened URL:",font=("Cascadia Code",15,"bold"),bg="gray77").grid()
shortened_url_entry= Entry(root,textvariable=url_address,relief="ridge",borderwidth=4,width=25,state="readonly").grid()
copy_button= Button(root,text="Copy The URL",command=copyurl,relief="ridge",borderwidth=4,bg="gray88").grid()
made_by_label = Label(root,text="Made By Harun",bg="gray77",font=("Cascadia Code",15,"bold")).grid()

root.mainloop()
