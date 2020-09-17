# combined two images side by side and scales the larger to match the smaller

from PIL import Image


for identifier in range(1,7):

	image1 = Image.open('in_{}.png'.format(str(identifier)))
	image2 = Image.open('out_{}.png'.format(str(identifier)))

	image1_size = image1.size
	image2_size = image2.size

	if(image2_size[1]>image1_size[1]):
		Yscalar = image1.size[1]/image2.size[1]
		image2 = image2.resize((int(image2.size[0]*Yscalar), int(image2.size[1]*Yscalar)))
		image2_size = image2.size
		
	else:
		Yscalar = image2.size[1]/image1.size[1]
		image1 = image1.resize((int(image1.size[0]*Yscalar), int(image1.size[1]*Yscalar)))
		image1_size = image1.size
		

	new_image = Image.new('RGB',(image1_size[0]+image2_size[0], image1_size[1]), (250,250,250))
		
	new_image.paste(image1,(0,0))
	new_image.paste(image2,(image1_size[0],0))
	new_image.save("comparison_{}.png".format(str(identifier)),"PNG")
	#new_image.show()

