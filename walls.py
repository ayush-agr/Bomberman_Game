from glob import *
from termcolor import colored

class walls:
    def __init__(self,rows,columns):
        self.rows=rows
        self.columns=columns             
        for x in range(rows):
            arr.append([])
            for y in range(columns):
                arr[x].append(' ')
        x,y=0,0
        while x<self.rows:
            y=0
            while y<self.columns:
                if x==0 or x==1 or x==self.rows-2 or x==self.rows-1:
                    arr[x][y]=colored('#','green')
                elif y>=0 and y<=3:
                    arr[x][y]=colored('#','green')
                elif y>=self.columns-4 and y<=self.columns-1:
                    arr[x][y]=colored('#','green')
                else:
                    if int(x/2)%2==1:
                        arr[x][y]=' '
                    elif int(y/4)%2==1:
                        arr[x][y]=' '
                    else:
                        arr[x][y]=colored('#','green')
                y+=1
            x+=1

