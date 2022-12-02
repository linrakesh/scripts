from rembg import remove
from PIL import Image
from tkinter import filedialog 

input_path=filedialog.askopenfilename()
file_name= input_path.split('/')[-1]
file_name = file_name.split('.')[0]+"_remove_bg.png"
#print(file_name)
#print(input_path)
#input_path = 'e:/banner.jpg'
output_path=filedialog.askdirectory()
output_path= output_path+"/"+file_name
#output_path = 'e:/output.png'

input = Image.open(input_path)
output = remove(input)
output.save(output_path)

print('Check your file in {}'.format(output_path))
