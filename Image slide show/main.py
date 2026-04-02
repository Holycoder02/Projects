from itertools import cycle
from PIL import Image, ImageTk
import time
import tkinter as tk

root = tk.Tk()
root.title("Image Slideshow Viewer")

#List of image Path 
image_paths = [
    r"C:\Users\gaura\Downloads\images\-473Wx593H-460327042-blue-MODEL.avif",
    r"C:\Users\gaura\Downloads\images\31aOma+odGL.jpg",
    r"C:\Users\gaura\Downloads\images\71OL17Fv1-L._SY342_.jpg",
    r"C:\Users\gaura\Pictures\josephs-well-system.jpg",
    r"C:\Users\gaura\Pictures\miyamoto musashi.jpeg",

]

#Resize the image to 1080x1080
image_size = (1080, 1080)
images=[Image.open(path).resize(image_size) for path in image_paths]
photo_images=[ImageTk.PhotoImage(image) for image in images]

#Create a label to display the images
label = tk.Label(root)
label.pack()

#Function to update the image in the label
image_index = 0

def update_image():  # This function will be called to update the image in the label
    global image_index   #We need to use global keyword to modify the image_index variable defined outside the function
    label.config(image=photo_images[image_index])  #Update the label with the current image
    image_index = (image_index + 1) % len(photo_images)  #This will ensure that the image index wraps around to the beginning of the list when it reaches the end
    root.after(3000, update_image)  #Delay between images (in milliseconds)

play_button = tk.Button(root, text="Start Slideshow", command=update_image)
play_button.pack()

root.mainloop()