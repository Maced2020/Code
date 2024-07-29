#me making buttons to do random stuff
# started AUG 27 2021 
 
import tkinter
import tkmacosx
import webbrowser
import os

#testing

def open_youtube():
    youtube_link = webbrowser.get('firefox').open('http://www.youtube.com') 
    return youtube_link

def open_twitch():
    twitch_link = webbrowser.get('firefox').open('http://twitch.tv')
    return twitch_link

def open_visual_studio():
    visual_studio = os.system("code .")
    return visual_studio


def tims_favorites():
    window = tkinter.Tk()
    window.title('Easy Button')
    window.geometry('800x600')
    quit_button = tkmacosx.Button(window, text="QUIT", bg='black',fg='white',command=quit)
    youtube_button = tkmacosx.Button (window, text="Youtube", bg='black', fg='white', command=open_youtube)
    twitch_button = tkmacosx.Button(window, text="Twitch", bg='black', fg='white', command=open_twitch)
    visual_studio_button = tkmacosx.Button(window, text="Visual Studio", bg='black', fg='white', command=open_visual_studio)
    visual_studio_button.pack()
    twitch_button.pack()
    youtube_button.pack()
    quit_button.pack() #this packs the button together and ensures it works. 
    window.mainloop() #not sure why i need this but with out it I can't get the screen to load.

tims_favorites()