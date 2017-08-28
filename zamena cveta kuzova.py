# -*- coding: cp1251 -*-
import random
from PIL import Image
from PIL import ImageDraw

a1 = random.randint(1, 255)
b1 = random.randint(1, 255)
c1 = random.randint(1, 255)

image = Image.open("kuzov.png") #Открываем изображение. 
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования. 
width = image.size[0] #Определяем ширину. 
height = image.size[1] #Определяем высоту. 	
pix = image.load() #Выгружаем значения пикселей.
for i in range(width):
	for j in range(height):
		a = pix[i, j][0]
		b = pix[i, j][1]
		c = pix[i, j][2]
		#print (a,b,c)
		if a > 0 or b > 0 or c >0:
		  draw.point((i, j), (a1, b1, c1))
image.save("kuzov.png", "PNG")
del draw
