from PIL import Image

def intMappedToChar(num):
    if num >= 1 and num < 30: return "@"
    elif num >= 30 and num < 40: return "#"
    elif num >= 40 and num < 50: return "&"
    elif num >= 50 and num < 60: return "%"
    elif num >= 60 and num < 70: return "$"
    elif num >= 70 and num < 80: return "h"
    elif num >= 80 and num < 90: return "i"
    elif num >= 90 and num < 100: return "j"
    elif num >= 100 and num < 110: return "k"
    elif num >= 110 and num < 120: return "l"
    elif num >= 120 and num < 130: return "m"
    elif num >= 130 and num < 140: return "n"
    elif num >= 140 and num < 150: return "o"
    elif num >= 150 and num < 160: return "p"
    elif num >= 160 and num < 170: return "~"
    elif num >= 170 and num < 180: return "_"
    elif num >= 180 and num < 190: return ";"
    elif num >= 190 and num < 200: return ","
    elif num >= 200 and num < 210: return "."
    elif num >= 210 and num < 220: return "'"
    elif num >= 220 and num < 230: return "´"
    elif num >= 230: return " "
    else: return " "

def grayscale(pixelValues):
    red = int(pixelValues[0])
    green = int(pixelValues[1])
    blue = int(pixelValues[2])
    grayValue = int((red+green+blue)/3)
    return grayValue

image = Image.open('images/loewe.jpg')
pixels = image.load()
tuple_size = image.size;
print (pixels[1,1])

height = int(tuple_size[0])
width = int(tuple_size[1])

print (type(pixels[1,1]))

print(tuple_size)

print(intMappedToChar(1))

output_string = str("")

for y in range(0, width):
    for x in range(0, height):
        output_string += intMappedToChar(grayscale(pixels[x,y])) + ' '
    output_string += '\n'
print (output_string)

data = open('file.txt', 'a')
data.write(output_string)
data.close()
