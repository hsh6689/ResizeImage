import os
import sys
import time
from PIL import Image

def main():
	#please input your invoice number next to RM
	print('Enter your size %')
	k = int(input())

	for filename in os.listdir():	
		if filename.endswith('.jpg'):
			im = Image.open(filename)
			width, height = im.size
			newsize = (int(width*(k/100)),int(height*(k/100)))
			im = im.resize(newsize)
			im.save(filename)
	
	print('\nJob completed....Chnaged image successfully.')

if __name__=='__main__':
	main()
