from PIL import Image
f1 = Image.open("new_image.png")
f1_pixels = f1.load()

width, height = f1.size

f2 = Image.open("key.png")
f2_pixels = f2.load()

for i in range(width):
    for j in range(height):
        a = f1_pixels[i,j]
        b = f2_pixels[i,j]

        r = a[0] ^ b[0]
        g = a[1] ^ b[1]
        b = a[2] ^ b[2] 

        f2_pixels[i,j] = (r,g,b)
f2.save("solution.png")
