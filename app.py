from win10toast import ToastNotifier
import requests
import time
import json
import random as okuyasu
from tkinter import *

root = Tk()
root.title("Okuyasu Motivator")

inter = StringVar()

def get_Quote():
    params = {
        'method':'getQuote',
        'lang':'en',
        'format':'json'
    }
    res = requests.get('http://api.forismatic.com/api/1.0/',params)
    jsonText =json.loads(res.text)
    return jsonText["quoteText"],jsonText["quoteAuthor"]

def motivate():
    try:
        var = inter.get()
        var = int(var) * 60
        root.destroy()
        quote,author = get_Quote()
        status = quote

        toaster = ToastNotifier()
        toaster.show_toast("Oi Josuke!",
        status, icon_path="okuyasu.ico", duration=7, threaded=True)
        while toaster.notification_active(): time.sleep(0.1)
        time.sleep(var)
        motivate()
    except Exception as ex:
        print(ex)
        motivate()

intervalLabel = Label(root, text="Interval in minutes:")
intervalLabel.pack()

interval = Entry(root, textvariable=inter)
interval.pack(padx=5,pady=5)

submit = Button(root, text="Motivate!", command=motivate)
submit.pack()

#motivate()

root.mainloop()
