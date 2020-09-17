# image_comparison_maker
Combines 2 images side by side and scales them appropriately

Change the file as appropriate (see below):

'''
for identifier in range(1,7):

	image1 = Image.open('in_{}.png'.format(str(identifier)))
	image2 = Image.open('out_{}.png'.format(str(identifier)))
'''

The range(1,7) indicates that it is iterating over the numbers {1,2,3,4,5,6}
The filenames it is looking for are 'in_{}.png' and 'out_{}.png' where the '{}' is replaced with the formatted number given in the list above.

If you only wanted one image, you could change range(1,7) to range(1,2) and just name your image files 'in_1' and 'out_1'.

You can also change the 'in_{}.png' and 'out_{}.png' to whatever you want to name your images.

'''
new_image.save("comparison_{}.png".format(str(identifier)),"PNG")
'''

This line is what the file saves the combined output as. It again replaces the '{}' with the number from the list at the top (range(1,7)). You could make it whatever you want as well.
