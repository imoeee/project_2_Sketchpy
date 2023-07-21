# from sketchpy import library as lib
# obj =  lib.rdj()
# obj.draw()

# from sketchpy import library as lib
# myObject =  lib.tom_holland()
# myObject.draw()

from sketchpy import canvas
obj = canvas.sketch_from_image(r"C:\Users\imo\Downloads\venom.jpg")
obj.draw(threshold=100)

