# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 12:19:05 2021

@author: Amitesh_Chaurasia
"""

import csv
import os
from PIL import Image

if __name__ == '__main__':
	
	#Input Folder Path
	inputfolder = "./Input"
	#Size of images in the Input folder (40X25 = 1000 pixels)
    
	with open('./Output/output.csv', mode='a') as file:
		writer = csv.writer(file)
		frame = 0
		for filename in os.listdir(inputfolder):
			img = Image.open(os.path.join(inputfolder,filename))	#Open Image
			width, height = img.size
			img = img.convert('RGB')
			img = img.transpose(Image.FLIP_TOP_BOTTOM)				#To compensate (0,0) Data Read
			z=0
			
			# For all pixels in images
			for x in range(width):
				for y in range(height):
					z+=1						#Unique Dimension for QlikModel
					r,g,b = img.getpixel((x,y))	#RGB Color Values of Pixel
					data = [x,y,z,r,g,b,frame]	# X--> Measure 1 , Y--> Measure 2, Frame--> Used in Animator
					writer.writerow(data)
			frame +=1
    #print('Completed')