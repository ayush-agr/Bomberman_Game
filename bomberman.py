from glob import *
from person import person
from termcolor import colored

class Bomberman(person):

	def __init__(self,x,y):
		super().__init__(x,y)
		for i in range(2):
			for j in range(4):
				arr[2+i][4+j]=man[i][j]

	def remove_it(self):
		for i in range(2):
			for j in range(4):
				arr[self.x+i][self.y+j]=' '

	def is_enemy_nearby(self):
		if arr[self.x][self.y-4]==colored('E','red') or arr[self.x][self.y+4]==colored('E','red') or arr[self.x-2][self.y]==colored('E','red') or arr[self.x+2][self.y]==colored('E','red'):
			return 1
		else:
			return 0
