from graphics2 import*
from buttons import*

def main():
    win = GraphWin("Image Editor", 800, 600)
    B = Button(win, Point(600, 100), Point(700, 175), "sky blue", "Darken")
    M = Button(win, Point(600, 200), Point(700, 275), "tomato", "Lighten")
    Q = Button(win, Point(600, 300), Point(700, 375), "misty rose", "Quit")

    I = Image(Point(300, 300), "picture (1).png")
    I.draw(win)


    while True:
        
        m = win.getMouse()
        
        if B.isClicked(m):
            darken(I)
            

        if M.isClicked(m):
            lighten(I)
            

        if Q.isClicked(m):
            win.close()
            break
    


def darken(img):
    x = img.getWidth()
    y = img.getHeight()


    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            red = pix[0]
            green = pix[1]
            blue = pix[2]
            red = red - 20
            green = green - 20
            blue = blue - 20

            if red < 0:
                red = 0

            if blue < 0:
                blue = 0
                
            if green < 0:
                green = 0
                
            c = color_rgb(red, green, blue)
            img.setPixel(i, j, c)
            
           
            
def lighten(img):
    x = img.getWidth()
    y = img.getHeight()


    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            red = pix[0]
            green = pix[1]
            blue = pix[2]
            red = red + 20
            green = green + 20
            blue = blue + 20

            if red > 255:
                red = 255

            if blue > 255:
                blue = 255
                
            if green > 255:
                green = 255

            
            c = color_rgb(red, green, blue)
            img.setPixel(i, j, c)

    
    


    
if __name__ == "__main__":
     main()
