from tkinter import *
import tkinter as tk
from tkinter import messagebox
from bs4 import BeautifulSoup
import requests
import webbrowser
url="https://cricbuzz.com/"
def score():
	response=requests.get(url)
	soup=BeautifulSoup(response.text,"html.parser")
	t_1=soup.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
	t_2=soup.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
	t_1_s=soup.find_all(class_="cb-ovr-flo")[8].get_text()
	t_2_s=soup.find_all(class_="cb-ovr-flo")[10].get_text()
	try:
		live=soup.find_all(class_="cb-ovr-flo cb-text-live")[0].get_text()
	except:
		live=soup.find_all(class_="cb-ovr-flo cb-text-complete")[0].get_text()
	t1=Label(root,text=t_1+"\t\t"+t_2,font=("font awesome",15,"bold italic"),bg="#00237d",fg="#f5873b").place(x=260,y=120)
	if t_1_s=="":
		didbat1=Label(root,text="Match Did Not\nstarts yet.",font=("font awesome",15,"bold italic"),bg="#00237d",fg="#f5873b").place(x=240,y=170)
	else:
		t1_s=Label(root,text=t_1_s,font=("font awesome",15,"bold italic"),bg="#00237d",fg="#f5873b").place(x=250,y=170)
		if t_2_s=="":
			didbat2=Label(root,text="Did not\nbat yet",font=("font awesome",15,"bold italic"),bg="#00237d",fg="#f5873b").place(x=420,y=170)
		else:
			t2_s=Label(root,text=t_2_s,font=("font awesome",15,"bold italic"),bg="#00237d",fg="#f5873b").place(x=450,y=170)
	winlive=Label(root,text=live,font=("font awesome",15,"bold italic"),bg="#00237d",fg="#f5873b").place(x=80,y=240)
root=tk.Tk()
root.title("IPL live ScoreCard | Manjunathan C.")
root.config(bg="#00237d")
root.geometry("800x600")
ico=PhotoImage(file="icon.png")
root.iconphoto(True,ico)
label1=Label(root,text="IPL live ScoreCard",font=("font awesome",18,"bold italic"),bg="#00237d",fg="#f5873b").pack()
refresh=Button(root,text="Refresh",font=("font awesome",15,"bold italic"),bg="#f5873b",fg="#00237d",borderwidth=5,command=score).place(x=330,y=370)
exit=Button(root,text="Exit",font=("font awesome",15,"bold italic"),bg="#f5873b",fg="#00237d",borderwidth=5,command=root.destroy).place(x=353,y=430)
contact=Button(root,text="Contact",font=("font awesome",15,"bold italic"),bg="#f5873b",fg="#00237d",borderwidth=5,command=lambda:webbrowser.open("https://github.com/cmanjunathan45/")).place(x=330,y=490)
score()
root.mainloop()
