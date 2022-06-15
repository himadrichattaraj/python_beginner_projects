from tkinter import *
import time

widthVar = 800
heightVar = 450
speedX = 3
speedY = 2

fullview = Tk()

canvas = Canvas(fullview, width=widthVar, height=heightVar)
canvas.pack()

earthimage = PhotoImage(file="erth2.png")
back_image = canvas.create_image(0, 0, image=earthimage, anchor=NW)

alienimage = PhotoImage(file="alien2.png")
canvasimage = canvas.create_image(0, 0, image=alienimage, anchor=NW)

image_width = alienimage.width()
image_height = alienimage.height()

while True:
    coordinates = canvas.coords(canvasimage)
    if (coordinates[0]>=(widthVar-image_width) or coordinates[0]<0):
        speedX = -speedX
    elif (coordinates[1]>=(heightVar-image_height) or coordinates[1]<0):
        speedY = -speedY
    canvas.move(canvasimage, speedX, speedY)
    fullview.update()
    time.sleep(0.01)

fullview.mainloop()
