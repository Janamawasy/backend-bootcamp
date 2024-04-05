import concurrent.futures
import threading
import time
from PIL import Image
from multiprocessing import Process, Queue

def multi():
    # time = 28.461 sec
    start_time = time.perf_counter()
    img = Image.open("img1.jpg")
    img = img.convert('RGB')
    width, height = img.size
    new_image = Image.new(mode="RGB", size=(width, height))
    print(width, height)
    width_chunk = width//3
    height_chunk = height//2
    threads = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for i in range(3):
            for j in range(2):
                start_width = i * width_chunk
                end_width = start_width + width_chunk
                start_height = j * height_chunk
                end_height = start_height + height_chunk
                threads.append(executor.submit(reverse_pixels(start_width, end_width, start_height, end_height, img, new_image)))

    end_time = time.perf_counter()
    total_time = end_time - start_time
    print('time: ', total_time)
    new_image.save('multi-threading.jpg',format="JPEG")
    new_image.show()

def reverse_pixels(start_width, end_width, start_height, end_height, img, new_image):
    width = end_width - start_width
    height = end_height - start_height
    for x in range(width):  # Adjust x and y relative to the slice
        for y in range(height):
            r, g, b = img.getpixel((start_width + x, start_height + y))  # Adjust coordinates
            new_image.putpixel((start_width + x, start_height + y), (255 - r, 255 - g, 255 - b))


if __name__ == "__main__":
    multi()
