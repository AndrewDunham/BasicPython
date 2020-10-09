#!/usr/bin/env python

#Andrew Dunham
#Last Updated: December 30, 2018
from tkinter import *
from tkinter import ttk

def readInputFile(filename):
	arrayOfStuff = []
	inputFile = open(filename, "r")
	stringss = inputFile.readline().split(",")
	arrayOfStuff.append(stringss)
	return(arrayOfStuff)

def main():
	#inputStuff = readInputFile("myContacts.txt")

	root = Tk()#Start of tkinter stuff
	frame = Frame(root)

	Label(root, text="First Name").grid(row=0, sticky=W, padx=6)#Sticky is expansion
	Entry(root).grid(row=0, column=1, sticky=E, pady=4)
	
	
	Label(root, text="Last Name").grid(row=1, sticky=W, padx=6)#Sticky is expansion
	Entry(root).grid(row=1, column=1, sticky=E, pady=4)

	avatar = PhotoImage(file="avatarTemplate256.png", height="128",width="128")
	label = Label(root, image=avatar, height="128",width="128")

	Button(root, text="Submit").grid()
	label.grid()

	root.mainloop()#End of tkinter stuff
if __name__ == "__main__":
	main()
