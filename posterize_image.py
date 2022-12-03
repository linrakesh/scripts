# Importing Image and ImageOps module from PIL package
from PIL import Image, ImageOps
from tkinter import filedialog

# creating a image1 object
file_name = filedialog.askopenfilename()
# print(file_name)
im1 = Image.open(file_name)
# applying posterize method 1-8 bit to keep in each frame
im2 = ImageOps.posterize(im1, 3)
output_path = filedialog.askdirectory()
output_file = output_path+"/" + \
    file_name.split('/')[-1].split('.')[0]+'_poster.jpg'
print(output_file)
im2.show()
im2.save(output_file)
print(f'Check final result {output_file}')
