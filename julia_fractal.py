#!/usr/bin/env python2.7

                    ##########################
                    #    julia_fractal.py    #
                    #        v_1.2.0         #
                    ##########################


import os, sys
from PIL import Image


# Driver function
if __name__ == "__main__":

    # Parse command line arguments
    help_msg = ("Format: [command] [width] [height] [zoom factor] [cX] [cY] [moveX] [moveY]\n"
                "Use: --help or -h for help")
    error_msg = "Invalid argument(s)"
    if len(sys.argv) == 2 and (sys.argv[1] == "--help" or sys.argv[1] == "-h"):
        print(help_msg)
        sys.exit()
    elif len(sys.argv) < 8:
        print("{}\n{}".format(error_msg, help_msg))
        sys.exit()

    # Setting image width, height, zoom factor, cX, cY, moveX, moveY
    try:
        w, h, zoom = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])
        cX, cY = float(sys.argv[4]), float(sys.argv[5])
        moveX, moveY = float(sys.argv[6]), float(sys.argv[7])
    except ValueError:
        print("{}\n{}".format(error_msg, help_msg))
        sys.exit()
    if w < 1 or h < 1 or zoom <= 0:
        print("{}\n{}".format(error_msg, help_msg))
        sys.exit()

    # Creating the new image in RGB mode
    bitmap = Image.new("RGB", (w, h), "white")

    # Set storage for the image and load pixel data
    pix = bitmap.load()

    # Setting up the variables according to 
    # The equation to create the fractal
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

    # To save the created bitmap into png or just display it
    decision = raw_input("Save image as .png? [Y/N] ").lower()
    if decision == "y":
      image_name = raw_input("Filename: ")
      while os.path.exists(image_name):
        print("Choose another filename..." + image_name + ".png already exists!")
        image_name = raw_input("Filename: ")
      else:
        extension = "png"
        try:
            bitmap.save("pictures/{}.{}".format(image_name, extension), extension)
            print("Image as " + image_name + ".png saved!")
        except:
            print("Could not save image: invalid file name?")
            sys.exit()
    else:
      print("Nothing saved!")
      bitmap.show()

