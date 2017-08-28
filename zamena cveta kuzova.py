# -*- coding: cp1251 -*-
import random
from PIL import Image
from PIL import ImageDraw



t = ((173,255,47),(255,255,47),(1,255,1),(45,55,47),(19,255,255))

a1 = random.randint(0, len(t))
print(a1)

image = Image.open("kuzov.png") #��������� �����������. 
draw = ImageDraw.Draw(image) #������� ���������� ��� ���������. 
width = image.size[0] #���������� ������. 
height = image.size[1] #���������� ������. 	
pix = image.load() #��������� �������� ��������.
for i in range(width):
	for j in range(height):
		a = pix[i, j][0]
		b = pix[i, j][1]
		c = pix[i, j][2]
		#print (a,b,c)
		if a > 0 or b > 0 or c >0:
		  draw.point((i, j), (t[a1]))
image.save("kuzov.png", "PNG")
del draw
