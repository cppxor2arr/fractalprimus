#!/usr/bin/python3
 
                    ##########################
                    #  JuliaFractal Creator  #
                    #        v_1.2.0         #
                    ##########################

import os, sys

# Python code for Julia Fractal
from PIL import Image
  
# Driver function
if __name__ == "__main__":
   
    # Setting the width, height and zoom 
    # Of the image to be created
    w, h, zoom = 1920,1080,1
  
    # Creating the new image in RGB mode
    bitmap = Image.new("RGB", (w, h), "white")
 
    # Allocating the storage for the image and
    # Loading the pixel data.
    pix = bitmap.load()
    
    # Setting up the variables according to 
    # The equation to  create the fractal
    cX, cY = -0.7, 0.27015
    moveX, moveY = 0.7, 0.27015
    maxIter = 255
  
    for x in range(w):
        for y in range(h):
            zx = 1.5*(x - w/2)/(0.5*zoom*w) + moveX
            zy = 1.0*(y - h/2)/(0.5*zoom*h) + moveY
            i = maxIter
            while zx*zx + zy*zy < 4 and i > 1:
                tmp = zx*zx - zy*zy + cX
                zy,zx = 2.0*zx*zy + cY, tmp
                i -= 1
 
            # Convert byte to RGB (3 bytes), kinda 
            # Magic to get nice colors
            pix[x,y] = (i << 21) + (i << 10) + i*8
     
    #    <-- OUTPUT -->    #
    # To display the created fractal in firefox browser uncomment
    # The following pattern
    #import webbrowser
    #firefox_path="/usr/bin/firefox"
    #webbrowser.register('firefox', None,webbrowser.BackgroundBrowser(firefox_path),1)
    #browser = webbrowser.get("firefox")
    #browser.open(bitmap.show())

    # To display the created fractal in chromium browser uncomment
    # The following pattern
    #import webbrowser
    #chromium_path="/usr/bin/chromium"
    #webbrowser.register('chromium', None,webbrowser.BackgroundBrowser(chromium_path),1)
    #browser = webbrowser.get("chromium")
    #browser.open(bitmap.show())

    # To display the created fractal in qupzilla browser uncomment
    # The following pattern
    #import webbrowser
    #qupzilla_path="/usr/bin/qupzilla"
    #webbrowser.register('qupzilla', None,webbrowser.BackgroundBrowser(qupzilla_path),1)
    #browser = webbrowser.get("qupzilla")
    #browser.open(bitmap.show())
    
    # To display the created fractal in opera browser uncomment
    # The following pattern
    #import webbrowser
    #opera_path="/usr/bin/opera"
    #webbrowser.register('opera', None,webbrowser.BackgroundBrowser(opera_path),1)
    #browser = webbrowser.get("opera")
    #browser.open(bitmap.show())

    # To display the picture with built-in imageviewer [by-default]
    bitmap.save("julia_fractal.png")
