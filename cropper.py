# Improting Image class from PIL module 
from PIL import Image
# Importing argparse for adding argument parser
import argparse
# Impoting os module for creating folder
import os 

# Cropper function
def cropper(croppedHeight, croppedWidth):
   # Giving first value to the counters
   nameCounter  = 1
   # i is counting x axis column of image
   for i in range(int(height/croppedHeight)):
      # j is counting y axis row of image
      for j in range(int(width/croppedWidth)):
         # Set the cropping area with box=(left, upper, right, lower).
         croppedImage = img.crop((croppedWidth*j, croppedWidth*i, croppedHeight*(j+1), croppedHeight*(i+1)))
         # Saving image to folder which created name as cropped_images   
         croppedImage.save(os.getcwd() + "/cropped_images/image" + str(nameCounter) + ".png")
         print(str(nameCounter) + ".png" + " created")
         # Adding one xAxisCounter and nameCounter after take a photo
         nameCounter  = nameCounter  + 1

if __name__ == "__main__":
   # Construct the argument parse and parse the arguments
   parser = argparse.ArgumentParser(description='Process command line arguments.')
   parser.add_argument('-path', "--path", required=True, help="path to file contain image which will crop")
   parser.add_argument('-cW', "--cw", required=True, help='cropped image width value', type=int)
   parser.add_argument('-cH', "--ch", required=True, help='cropped image Height value', type=int)
   args = parser.parse_args()

   # Height and width value that we want to crop
   croppedWidth = args.cw
   croppedHeight = args.ch

   # Open a image 
   img = Image.open(args.path) 
   
   # Size of the image in pixels (size of orginal image)
   width, height = img.size 

   # Creating file for cropped images where is cropper.py file
   os.mkdir("cropped_images")

   # Function calling 
   cropper(croppedHeight, croppedWidth)
