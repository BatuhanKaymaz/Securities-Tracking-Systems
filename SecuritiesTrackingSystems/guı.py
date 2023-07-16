import tkinter as tk
import webbrowser
import win32gui
from PIL import ImageTk, Image
import pyautogui
import time
import os

#Uygulama ana bileşenlerini oluşturma
master = tk.Tk()
master.title("Menkul Kıymetler Takip")
#master.geometry("1000x750")
full =master.attributes("-fullscreen",True)
small= master.attributes("-fullscreen",False)
#Ekranları bölme
left_frame = tk.Frame(master, width=300, height=1000, bg="GREY")
left_frame.pack(side="left")
right_frame = tk.Frame(master,bg="white")
right_frame.place(x=500,y=500)

#Bitcoin için bilgi al
def bitcoin ():
    btc=tk.Label(master,text="Bitcoin :  ")
    btc.config(bg="grey",font=("Normal",20))
    btc.place(x=50,y=200)
    def get_btc():
        webbrowser.open("https://www.binance.com/tr/trade/BTC_USDT?theme=dark&type=spot")
        time.sleep(10)
        screenshot = pyautogui.screenshot()
        screenshot.save("btc.png")
        screenshot = screenshot.resize((10, 10), Image.ANTIALIAS)
        image = Image.open("btc.png")
        image = image.resize((1200, 1200), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(master, image=photo)
        label.place(x=500,y=0)
        label.mainloop()
    btc_button = tk.Button(master,text="Ara",command=get_btc)
    btc_button.config(width=10,height=1,bg="white",font=("Normal",15))
    btc_button.place(x=155,y=200)

#döviz için bilgi al
def doviz ():
    dovizz=tk.Label(master,text="Dolar :  ")
    dovizz.config(bg="grey",font=("Normal",20))
    dovizz.place(x=50,y=400)
    def get_doviz():
        webbrowser.open("https://www.altinkaynak.com/Doviz/Kur/Guncel")
        time.sleep(10)
        screenshot = pyautogui.screenshot()
        screenshot.save("dolar.png")
        screenshot = screenshot.resize((10, 10), Image.ANTIALIAS)
        image = Image.open("dolar.png")
        image = image.resize((1200, 1200), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(master, image=photo)
        label.place(x=500,y=0)
        label.mainloop()
    doviz_button = tk.Button(master,text="Ara",command=get_doviz)
    doviz_button.config(width=10,height=1,bg="white",font=("Normal",15))
    doviz_button.place(x=155,y=400)

#Altın için bilgi al
def altin ():
    altinn=tk.Label(master,text="Altın :  ")
    altinn.config(bg="grey",font=("Normal",20))
    altinn.place(x=50,y=600)
    def get_altin():
        webbrowser.open("https://www.altinkaynak.com/Doviz/Kur/Guncel")
        time.sleep(10)
        screenshot = pyautogui.screenshot()
        screenshot.save("altin.png")
        screenshot = screenshot.resize((10, 10), Image.ANTIALIAS)
        image = Image.open("altin.png")
        image = image.resize((1200, 1200), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(master, image=photo)
        label.place(x=500,y=0)
        label.mainloop()
    altin_button = tk.Button(master,text="Ara",command=get_altin)
    altin_button.config(width=10,height=1,bg="white",font=("Normal",15))
    altin_button.place(x=155,y=600)

bitcoin() 
doviz()
altin()
master.mainloop()