from glob import *
from termcolor import colored
import glob

brk=[[colored('|','yellow'),colored('_','yellow'),colored('_','yellow'),colored('|','yellow')],[colored('|','yellow'),colored('_','yellow'),colored('_','yellow'),colored('|','yellow')]]

class bricks:

	def __init__(self,x,y):
		self.x=x
		self.y=y


	def remove_it(self):
		for i in range(2):
			for j in range(4):
				arr[self.x+i][self.y+j]=' '

		glob.score+=20

	def place_brick(self):
		for i in range(2):
			for j in range(4):
				arr[self.x+i][self.y+j]=brk[i][j]
