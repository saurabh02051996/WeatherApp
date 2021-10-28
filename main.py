import tkinter as tk
from PIL import ImageTk,Image
import requests


root=tk.Tk()
root.title("Weather Forecast App ")
root.geometry("680x600+100+50")
root.resizable(False,False)
#Api key : 3776e10e087728b95240a44f6d62f056
#Api url : api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
def format_response(weather):
    try:
        city = (weather['name'])
        condition = (weather['weather'][0]['description'])
        temp = (weather['main']['temp'])
        # c_temp=((temp-32)*5/9)
        
        humidity=weather['main']['humidity']
        windspeed=weather['wind']['speed']
        final_str='City:%s\n\nCondition:%s\n\nTemprature(°F):%s\n\nHumidity(Percent):%s\n\nWind speed(km/h):%s'%(city,condition,temp,humidity,windspeed)
    except:
        final_str='There was a problem retrieving that information'    
    return final_str    


def get_weather(city):
    weather_key = '3776e10e087728b95240a44f6d62f056'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params={'APPID':weather_key,'q':city,'units':'imperial'}
    response=requests.get(url,params)
    # print(response.json())
    weather=response.json()

    # print(weather['name'])
    # print(weather['weather'][0]['description'])
    # print(weather['main']['temp'])

    result['text']=format_response(weather)
    icon_name=weather['weather'][0]['icon']
    open_image(icon_name)

## create function for icon ##
def open_image(icon):
    size=int(frame_two.winfo_height()*.5)
    img=ImageTk.PhotoImage(Image.open('./images/'+icon+'.png'))
    weather_icon.delete('all')
    weather_icon.create_image(0,0,anchor='nw',image=img)
    weather_icon.image=img


## create window background image ##
img=ImageTk.PhotoImage(file="images/image5.jpg")
img_label=tk.Label(root,image=img)
img_label.place(x=0,y=0,relwidth=1,relheight=1)

## create heading title ##
heading_title=tk.Label(img_label,text="Earth Including Over 200,000 Cities!",fg="red",bg='lightgreen',font=("times new roman",20,"bold"),width=28)
heading_title.place(x=80,y=19)

## create frame1 ##
frame_one=tk.Frame(img_label,bg="skyblue",bd=5)
frame_one.place(x=80,y=60,width=460,height=50)
## create entry field ##
entry_box=tk.Entry(frame_one,font=("times new roman",25),width=18,bg="lightgreen")
entry_box.grid(row=0,column=0,sticky="W")

## create button ##
btn=tk.Button(frame_one,text="Get Weather",fg="red",bg="lightgreen",cursor='hand2',font=("times new roman",15),width=11,command=lambda:get_weather(entry_box.get()))
btn.grid(row=0,column=1,padx=7)

## create frame2 for showing  data ##
frame_two=tk.Frame(img_label,bg="white")
frame_two.place(x=80,y=135,width=460,height=320)

result=tk.Label(frame_two,font=40,bg="violet",justify='left',anchor='nw')
result.place(relwidth=1,relheight=1)

## create canvas for icon image which is shown on result and result is shown on frame _two  ##
weather_icon=tk.Canvas(result,bg='violet',bd=0,highlightthickness=0)
weather_icon.place(relx=.75,rely=0,relwidth=1,relheight=.5)

root.mainloop()