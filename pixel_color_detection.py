from PIL import Image
img = Image.open('Heatmap.png')

# all colors to detect set to 0
dark_red = 0
red = 0
orange = 0
yellow = 0
green = 0
cyan = 0
blue = 0
dark_blue = 0
white = 0

# get all pixels
all_pixels = img.load()

for x in range(0, 1920):
  for y in range(0, 1080):
    # rgb values
    r_value = all_pixels[x,y][0]
    g_value = all_pixels[x,y][1]
    b_value = all_pixels[x,y][2]

    # dark red buffer
    if ((r_value in range(138, 226)) and (g_value in range(66, 88)) and (b_value in range(66, 88))):
      dark_red += 1

    # red buffer
    elif ((r_value in range(225, 255)) and (g_value in range(66, 88)) and (b_value in range(66, 88))):
      red += 1

    # orange buffer
    elif ((r_value in range(245, 255)) and (g_value in range(193, 230)) and (b_value in range(66, 88))):
      orange += 1

    # yellow buffer
    elif ((r_value in range(245, 255)) and (g_value in range(200, 231)) and (b_value in range(66, 88))):
      yellow += 1

    # green buffer
    elif ((r_value in range(144, 213)) and (g_value in range(245, 255)) and (b_value in range(120, 189))):
      green += 1

    # cyan buffer
    elif ((r_value in range(55, 109)) and (g_value in range(195, 255)) and (b_value in range(228, 255))):
      cyan += 1

    # blue buffer
    elif ((r_value in range(66, 88)) and (g_value in range(115, 151)) and (b_value in range(245, 255))):
      blue += 1

    # dark blue buffer
    elif ((r_value in range(66, 88)) and (g_value in range(66, 88)) and (b_value in range(165, 226))):
      dark_blue += 1

    # white buffer
    elif (r_value == g_value == b_valie == 255):
      white += 1

# Accomodate for overlapping of colors
dark_blue = dark_blue + blue + cyan + green + yellow + orange + red + dark_red
blue = blue + cyan + green + yellow + orange + red + dark_red
cyan =  cyan + green + yellow + orange + red + dark_red
green = green + yellow + orange + red + dark_red
yellow = yellow + orange + red + dark_red
orange = orange + red + dark_red
red = red + dark_red
