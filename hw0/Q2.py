from PIL import Image

image = Image.open("hw0_data/westbrook.jpg")
pixel = image.load()

width, heigh = image.size
result = Image.new("RGB", (width, heigh))

for i in range(width):
    for j in range(heigh):
        r, g, b = pixel[i, j]
        result.putpixel((i, j), (r // 2, g // 2, b // 2))
result.save("Q2.jpg", "JPEG")