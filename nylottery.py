"""
Program: Lottery Number Generator
Author: L-Sayers
Date Created: 5/1/2020
Date Completed: 5/1/2020
Last Revised: 5/1/2020
Description:  Genreates lottery numbers to the similatiude of the New York Powerball lottery. (Hey, you never know!)
"""

from breezypythongui import EasyFrame
import random

class lottery(EasyFrame):
	"""GUI style framework"""
	def __init__(self):
		EasyFrame.__init__(self, title = "Lottery Number Generator", background = "blue",width = 450, height = 250)
		"""Labels for the window and output area of numbers"""
		self.addLabel(text = "Welcome to the New York Powerball Lottery!!!", row = 0, column = 0, columnspan = 100, sticky = "NSEW", background = "white", foreground = "darkgreen", font="bold")
		self.addLabel(text = "Today's Lottery Numbers Are:", row = 1, column = 0, columnspan = 10, background = "blue", foreground = "white", font="bold")
		self.addLabel(text = "The PowerBall Number Is:", row = 2, column = 0, columnspan =1, sticky = "W", background = "blue", foreground = "white", font="bold")

		self.num1Label = self.addLabel(text= " ", row = 1, column = 1, columnspan = 5, background = "ghostwhite", foreground = "black", font="bold")
		self.num2Label = self.addLabel(text= " ", row = 1, column = 2, columnspan = 5, background = "ghostwhite", foreground = "black", font="bold")
		self.num3Label = self.addLabel(text= " ", row = 1, column = 3, columnspan = 5, background = "ghostwhite", foreground = "black", font="bold")
		self.num4Label = self.addLabel(text= " ", row = 1, column = 4, columnspan = 5, background = "ghostwhite", foreground = "black", font="bold")
		self.num5Label = self.addLabel(text= " ", row = 1, column = 5, columnspan = 5, background = "ghostwhite", foreground = "black", font="bold")
		
		self.pBLabel = self.addLabel(text = "  ", row = 2, column = 1, columnspan = 5, sticky = "W", background = "red", foreground = "ghostwhite", font="bold")
		
		self.play = self.addButton(text = "PLAY NOW!", row = 3, column = 0, columnspan = 20, command = self.play)
		
	def play (self):
		"""chooses 5 random numbers for the lottery"""
		num1 = str(random.randint(1,69))
		num2 = str(random.randint(1,69))
		num3 = str(random.randint(1,69))
		num4 = str(random.randint(1,69))
		num5 = str(random.randint(1,69))
		self.num1Label["text"] = num1
		self.num2Label["text"] = num2
		self.num3Label["text"] = num3
		self.num4Label["text"] = num4
		self.num5Label["text"] = num5

		"""chooses a random number for the powerball"""
		powerball = str(random.randint(1,26))
		self.pBLabel["text"] = (powerball)

"""Main function"""
def main():
	lottery().mainloop()
#global call to main
main()