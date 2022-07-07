from PIL import Image
import cv2 as cv2
import os
def size_images(original_source):
    x = []
    y = []
    avereage = [0,0]
    images = os.listdir(original_source)
    for image in images:
        source = original_source + image
        img = Image.open(source) 
        width, height = img.size
        x.append(width)
        y.append(height)

    for width in x:
        avereage[0] += width / len(x)

    for height in y:
        avereage[1] += height / len(y)

    avereage[0] = int(avereage[0])
    avereage[1] = int(avereage[1])
    return avereage

def resize_images(original_source, avereage, final_source):
    images = os.listdir(original_source)
    for image in images:
        img = Image.open(original_source + image)
        img = img.resize((avereage[0], avereage[1]))
        img.save(final_source + image)
        
if __name__ == '__main__':
    ruta = './res/Globulos/promedio/'
    result = size_images(ruta)
    ruta2 = input('Ingrese la ruta inicial: ')
    ruta3 = input('Ingrese la ruta final: ')
    resize_images(ruta2, result, ruta3)
    print(result)

