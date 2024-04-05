import time
from PIL import Image

def single_thread():
    # time = 28.281 sec
    start = time.perf_counter()
    img = Image.open("img1.jpg")
    img.convert('RGB')
    width, height = img.size
    new_image = Image.new(mode="RGB", size=(width, height))

    reverse_pixels(width, height, img, new_image)
    end = time.perf_counter()
    print('time: ', end - start)
    new_image.save('reversed_image11',format="JPEG")
    new_image.show()

def reverse_pixels(width, height, img, new_image):
    for x in range(0, width):
        for y in range(0, height):
            r, g, b = img.getpixel((x,y))
            new_image.putpixel((x,y),(255 - r, 255 - g, 255 - b))

single_thread()





