from tkinter import *
import tkinter as tk
from tkinter import messagebox
from bs4 import BeautifulSoup
import requests

url="https://cricbuzz.com/"

def score():
	#team1,team2,team1_score,team2_score=data
	response=requests.get(url)
	soup=BeautifulSoup(response.text,"html.parser")
	team_1=soup.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
	team_2=soup.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()

	team_1_score=soup.find_all(class_="cb-ovr-flo")[8].get_text()
	team_2_score=soup.find_all(class_="cb-ovr-flo")[10].get_text()
	try:
		live=soup.find_all(class_="cb-ovr-flo cb-text-live")[0].get_text()
	except:
		live=soup.find_all(class_="cb-ovr-flo cb-text-complete")[0].get_text()

	team1=Label(root,text=team_1+"\t\t"+team_2,font=("font awesome",15,"bold italic"),bg="#00237d",fg="#f5873b").place(x=260,y=120)
	

	if team_1_score=="":
		didbat1=Label(root,text="Match Did Not\nstarts yet.",font=("font awesome",15,"bold italic"),bg="#00237d",fg="#f5873b").place(x=240,y=170)
	else:
		team1_score=Label(root,text=team_1_score,font=("font awesome",15,"bold italic"),bg="#00237d",fg="#f5873b").place(x=250,y=170)
		if team_2_score=="":
			didbat2=Label(root,text="Did not\nbat yet",font=("font awesome",15,"bold italic"),bg="#00237d",fg="#f5873b").place(x=420,y=170)
		else:
			team2_score=Label(root,text=team_2_score,font=("font awesome",15,"bold italic"),bg="#00237d",fg="#f5873b").place(x=450,y=170)

	
	winlive=Label(root,text=live,font=("font awesome",15,"bold italic"),bg="#00237d",fg="#f5873b").place(x=80,y=240)
	
		
root=tk.Tk()
root.title("IPL live ScoreCard | Manjunathan C.")
root.config(bg="#00237d")
root.geometry("800x500")
ico=PhotoImage(file="icon.png")
root.iconphoto(True,ico)

label1=Label(root,text="IPL live ScoreCard",font=("font awesome",18,"bold italic"),bg="#00237d",fg="#f5873b").pack()

refresh=Button(root,text="Refresh",font=("font awesome",15,"bold italic"),bg="#f5873b",fg="#00237d",borderwidth=5,command=score).place(x=330,y=370)

refresh=Button(root,text="Exit",font=("font awesome",15,"bold italic"),bg="#f5873b",fg="#00237d",borderwidth=5,command=root.destroy).place(x=353,y=430)
score()
root.mainloop()