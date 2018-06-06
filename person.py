from glob import *

class person:

	def __init__(self,x,y):
		self.x=x
		self.y=y


	def move_left(self,obj):
		if arr[self.x][self.y-4]==' ' and arr[self.x+1][self.y-4]==' ':
			self.remove_it()
			self.y-=4
			for i in range(2):
				for j in range(4):
					arr[self.x+i][self.y+j]=obj[i][j]
			return 1
		else:
			return 0

	def move_right(self,obj):
		if arr[self.x][self.y+7]==' ' and arr[self.x+1][self.y+7]==' ':
			self.remove_it()
			self.y+=4
			for i in range(2):
				for j in range(4):
					arr[self.x+i][self.y+j]=obj[i][j]
			return 1
		else:
			return 0

	def move_up(self,obj):
		if arr[self.x-2][self.y]==' ' and arr[self.x-2][self.y+1]==' ' and arr[self.x-2][self.y+2]==' ' and arr[self.x-2][self.y+3]==' ':
			self.remove_it()
			self.x-=2
			for i in range(2):
				for j in range(4):
					arr[self.x+i][self.y+j]=obj[i][j]
			return 1
		else:
			return 0

	def move_down(self,obj):
		if arr[self.x+3][self.y]==' ' and arr[self.x+3][self.y+1]==' ' and arr[self.x+3][self.y+2]==' ' and arr[self.x+3][self.y+3]==' ':
			self.remove_it()
			self.x+=2
			for i in range(2):
				for j in range(4):
					arr[self.x+i][self.y+j]=obj[i][j]
			return 1
		else:
			return 0