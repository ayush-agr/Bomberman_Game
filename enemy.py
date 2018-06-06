from glob import *
import random
from person import person
from termcolor import colored
import glob

class enemy(person):

	def __init__(self,x,y,move,count):
		super().__init__(x,y)
		self.move=move
		self.count=count

	def remove_it(self):
		for i in range(2):
			for j in range(4):
				arr[self.x+i][self.y+j]=' '

	def place_enemy(self):
		for i in range(2):
			for j in range(4):
				arr[self.x+i][self.y+j]=enmy[i][j]



	def move_enemy(self,level):
		mthds={1: self.move_right,2: self.move_left,3: self.move_up,4: self.move_down}
		temp=random.randint(1,4)
		if self.count==10-level or not(mthds[self.move](glob.enmy)):
			mthds[temp](glob.enmy)
			self.move=temp
			self.count=0
		else:
			self.count+=1
		#while mthds[temp]()!=1:
		#	temp=random.randint(1,4)
		# if self.move_right():
		# 	return 
		# if self.move_left():
		# 	return
		# if self.move_down():
		# 	return 
		# if self.move_up():
		# 	return
