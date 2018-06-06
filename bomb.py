from glob import *
import glob
from termcolor import colored

bomb_shape=[[colored('[','magenta'),colored('0','magenta'),colored('0','magenta'),colored(']','magenta')],[colored('[','magenta'),colored('0','magenta'),colored('0','magenta'),colored(']','magenta')]]
class bomb:

	def __init__(self,x,y):
		self.x=x
		self.y=y


	def plant_bomb(self,num):
		for i in range(2):
			for j in range(4):
				if arr[self.x+i][self.y+j]==' 'or arr[self.x+i][self.y+j]==colored(num+1,'magenta'):
					if j==1 or j==2:
						arr[self.x+i][self.y+j]=colored(num,'magenta')
					else:
						arr[self.x+i][self.y+j]=bomb_shape[i][j]

	def remove_bomb(self):
		for i in range(2):
			for j in range(4):
				arr[self.x+i][self.y+j]=' '

	def show_effect(self,obj):
		#killing bomberman if it is in range of bomb blast
		if (obj.x >= self.x-2 and obj.x <= self.x+3 and obj.y >= self.y and obj.y <= self.y+3) or (obj.x >= self.x and obj.x<=self.x+1 and obj.y>=self.y-4 and obj.y<=self.y+7):
			glob.dead =1
		elif (obj.x +1>= self.x-2 and obj.x+1 <= self.x+3 and obj.y+3 >= self.y and obj.y +3<= self.y+3) or (obj.x +1>= self.x and obj.x+1<=self.x+1 and obj.y+3>=self.y-4 and obj.y+3<=self.y+7):
			glob.dead=1
		#removing bricks if it is on range of blast effect
		for obj in brick_objs:
			if (obj.x >= self.x-2 and obj.x <= self.x+3 and obj.y >= self.y and obj.y <= self.y+3) or (obj.x >= self.x and obj.x<=self.x+1 and obj.y>=self.y-4 and obj.y<=self.y+7):
				obj.remove_it()
				brick_objs.remove(obj)
			elif (obj.x +1>= self.x-2 and obj.x+1 <= self.x+3 and obj.y+3 >= self.y and obj.y +3<= self.y+3) or (obj.x +1>= self.x and obj.x+1<=self.x+1 and obj.y+3>=self.y-4 and obj.y+3<=self.y+7):
				obj.remove_it()
				brick_objs.remove(obj)
		#removing emeny if it is in  range of bomb
		for obj in enemy_objs:
			if (obj.x >= self.x-2 and obj.x <= self.x+3 and obj.y >= self.y and obj.y <= self.y+3) or (obj.x >= self.x and obj.x<=self.x+1 and obj.y>=self.y-4 and obj.y<=self.y+7):
				obj.remove_it()
				enemy_objs.remove(obj)
				glob.score+=100
			elif (obj.x +1>= self.x-2 and obj.x+1 <= self.x+3 and obj.y+3 >= self.y and obj.y +3<= self.y+3) or (obj.x +1>= self.x and obj.x+1<=self.x+1 and obj.y+3>=self.y-4 and obj.y+3<=self.y+7):
				obj.remove_it()
				enemy_objs.remove(obj)
				glob.score+=100

	def show_blast(self):
		i=self.x-2
		while i<=self.x+3:
			j=self.y
			while j<=self.y+3:
				if arr[i][j]!=colored('#','green'):
					arr[i][j]=colored('^','cyan')
				j+=1
			i+=1	
		i=self.x
		while i<=self.x+1:
			j=self.y-4
			while j<=self.y+7:
				if arr[i][j]!=colored('#','green'):
					arr[i][j]=colored('^','cyan')
				j+=1
			i+=1	
	def clear_blast(self):
		i=self.x-2
		while i<=self.x+3:
			j=self.y
			while j<=self.y+3:
				if arr[i][j]!=colored('#','green'):
					arr[i][j]=' '
				j+=1
			i+=1	
		i=self.x
		while i<=self.x+1:
			j=self.y-4
			while j<=self.y+7:
				if arr[i][j]!=colored('#','green'):
					arr[i][j]=' '
				j+=1
			i+=1	