from tkinter import *
from datetime import *
from tkinter import font
import requests

window = Tk()
window.geometry("1024x762")
response=requests.get("https://api.openweathermap.org/data/2.5/onecall?lat=41.894134&lon=61.388045&units=metric&exclude={part}&appid=b25b7e1662811a678ab6023956214e44")
response.raise_for_status()
ob_havo=response.json()

kun = datetime.now()
bugun=datetime.now()
oylar=["","Yanvar","Fevral","Mart","Aprel","May","Iyun","Iyul","Avgust","Sentabr","Oktabr","Noyabr","Dekabr"]
b=30
a=20
kunlar=(ob_havo["daily"])
rasm = PhotoImage(file=f"png_images/01d.png")
Label(image=rasm).place(x=b,y = a)

for kunlik in kunlar:
    icon_raqam=kunlik["weather"][0]["icon"]
    gradus=kunlik["temp"]["day"]
    
    Label(text=f"  {bugun.day} -{oylar[kun.month]} {gradus}C°",font=("arial black",10,"bold")).place(x=10,y=a)
    bugun=bugun + timedelta(days=1)
    print(bugun.day)
    a+=100
    b+=100

    

window.mainloop()
