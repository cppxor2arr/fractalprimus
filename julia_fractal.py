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
    help_msg = ("Format: [command] [width] [height] [zoom] [cX] [cY] [moveX] [moveY] [max iteration]\n"
                "Use: --help or -h for help")
    error_msg = "Invalid argument(s)"
    if len(sys.argv) == 2 and (sys.argv[1] == "--help" or sys.argv[1] == "-h"):
        print(help_msg)
        sys.exit()
    elif len(sys.argv) < 9:
        print("{}\n{}".format(error_msg, help_msg))
        sys.exit()

    # Setting image width, height, zoom, cX, cY, moveX, moveY
    try:
        w, h, zoom = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])
        cX, cY = float(sys.argv[4]), float(sys.argv[5])
        moveX, moveY = float(sys.argv[6]), float(sys.argv[7])
        maxIter = int(sys.argv[8])
    except ValueError:
        print("{}\n{}".format(error_msg, help_msg))
        sys.exit()
    if w < 1 or h < 1 or zoom <= 0 or maxIter < 1:
        print("{}\n{}".format(error_msg, help_msg))
        sys.exit()

    # Creating the new image in RGB mode
    bitmap = Image.new("RGB", (w, h), "white")

    # Set storage for the image and load pixel data
    pix = bitmap.load()

    # Print message that process is running
    print("Process running...")

    # Set values for progress bar
    p25, p50, p75 = float( 1.0 / 4 * w), float( 1.0 / 2 * w), float( 3.0 / 4 * w)

    # Setting up the variables according to 
    # Equation to create the fractal
    for x in range(w):
        for y in range(h):
            zx = 1.5*(x - w/2)/(0.5*zoom*w) + moveX
            zy = 1.0*(y - h/2)/(0.5*zoom*h) + moveY
            i = maxIter
            while zx*zx + zy*zy < 4 and i > 1:
                tmp = zx*zx - zy*zy + cX
                zy,zx = 2.0*zx*zy + cY, tmp
                i -= 1

            # Convert byte to RGB (3 bytes) 
            pix[x,y] = (i << 21) + (i << 10) + i*8
        
        # Print progress and flush immediately if x is true
        if x == p25:
            sys.stdout.write(("25% [######..............]\r").encode("utf-8")); sys.stdout.flush()
        elif x == p50:
            sys.stdout.write(("50% [##########..........]\r").encode("utf-8")); sys.stdout.flush()
        elif x == p75:
            sys.stdout.write(("75% [##############......]\r").encode("utf-8")); sys.stdout.flush()
    

    sys.stdout.write(("100% [####################]").encode("utf-8"))
    sys.stdout.write(("\n" + "DONE!").encode("utf-8"))
    

    # Save the created bitmap as png or only display it without saving
    # Show it with default_image_viewer
    decision = raw_input("\nSave image as .png? [Y/N] ").lower()
    if decision == "y":
        directory, extension = "pictures", "png"
        if not os.path.isdir(directory):
            os.makedirs(directory)
        image_name = raw_input("Filename: ")
        while os.path.exists(directory + "/" + image_name + "." + extension):
            print("Choose another filename..." + image_name + "." + extension + " already exists!")
            image_name = raw_input("Filename: ")
        else:
            try:
                bitmap.save("{}/{}.{}".format(directory, image_name, extension), extension)
                print("Image as " + image_name + "." + extension + " saved!")
            except:
                print("Could not save image: invalid file name?")
                sys.exit()
    else:
        print("Nothing saved!")
        bitmap.show()
