import concurrent.futures
import multiprocessing
import time
from PIL import Image

def multi():
    # time =  10.212 sec
    start_time = time.perf_counter()
    img = Image.open("img1.jpg")
    img = img.convert('RGB')
    width, height = img.size
    new_image = Image.new(mode="RGB", size=(width, height))
    print(width, height)
    width_chunk = width//3
    height_chunk = height//2

    processes = []
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for i in range(3):
            for j in range(2):
                start_width = i * width_chunk
                end_width = start_width + width_chunk
                start_height = j * height_chunk
                end_height = start_height + height_chunk
                processes.append(
                    executor.submit(reverse_pixels, start_width, end_width, start_height, end_height, img))

    for future in concurrent.futures.as_completed(processes):
        result = future.result()
        x_start, x_end, y_start, y_end, chunk = result
        new_image.paste(chunk, (x_start, y_start, x_end, y_end))

    end_time = time.perf_counter()
    total_time = end_time - start_time
    print('time: ', total_time)
    new_image.save('multi-processing.jpg',format="JPEG")
    new_image.show()

def reverse_pixels(start_width, end_width, start_height, end_height, img):
    width = end_width - start_width
    height = end_height - start_height
    chunk = Image.new(mode="RGB", size=(width, height))

    for x in range(width):  # Adjust x and y relative to the slice
        for y in range(height):
            r, g, b = img.getpixel((start_width + x, start_height + y))  # Adjust coordinates
            chunk.putpixel(( x,  y), (255 - r, 255 - g, 255 - b))

    return start_width, end_width, start_height, end_height, chunk

if __name__ == "__main__":
    multi()
