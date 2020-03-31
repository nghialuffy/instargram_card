from PIL import Image, ImageDraw
from PIL import ImageFilter, ImageFont
import sys, getopt
#Define
POST = "62" 
FOLLOWING = "105" 
FOLLOWED = "201"


def print_usage():
    print("instargram_card.py -p $PATH -n $NAME")

NAME = ""
PATH = ""

try:
    opts, args = getopt.getopt(sys.argv[1:], 'hp:n:', ['path=', 'name='])
except getopt.GetoptError:
    print_usage()
    sys.exit(2)
# print(opts)   Debut

for opt, arg in opts:
    if opt == '-h':
        print(help)
        sys.exit(2)
    elif opt in ("-p", "--path"):
        PATH = arg
    elif opt in ("-n", "--name"):
        NAME = arg

if (PATH==""):
    print("Error: not found the path")
    print("Please add -p argument")
    print("-h to display help")
    sys.exit(2)

if (NAME==""):
    print("Error: not found the name")
    print("Please add -n argument")
    print("-h to display help")
    sys.exit(2)


image = Image.open(PATH)
image = image.resize((1080, 1080), Image.ANTIALIAS)
h = image.size[0]
w = image.size[1]

background = image.crop((0, int(int(w-h)/2), int(h), int(int(w)-int(w-h)/2)))


card  = image.crop((270,50,860,1050))

#shadow module
sh1 = background
sh2 = Image.open('./materials/shadow.jpg')
sh3 = Image.open('./materials/solid_shadow.jpg')
mask_sh = Image.new("L", sh2.size, 0)
draw_sh = ImageDraw.Draw(mask_sh)
mask_sh = sh3.resize(sh2.size).convert('L')
back_sh = sh1.copy()
back_sh.paste(sh2, (270, 100), mask_sh)
sh = back_sh.filter(ImageFilter.GaussianBlur(radius=10))

#insert card
background_shadow = sh
is1 = background_shadow.resize((1200, 1200), Image.ANTIALIAS)
is2 = card
is3 = Image.open('./materials/solid.jpg')
mask_is = Image.new("L", is2.size, 0)
draw_is = ImageDraw.Draw(mask_is)
mask_is = is3.resize(is2.size).convert('L')
back_is = is1.copy()
back_is.paste(is2, (298, 115), mask_is)

#insert_avatar
av1 = back_is
av2_1 = Image.open('./materials/avatar.jpg')
av2 = av2_1.resize((100, 100), Image.ANTIALIAS)
av3 = Image.open('./materials/solid_avatar.jpg')
mask_av = Image.new("L", av2.size, 0)
draw_av = ImageDraw.Draw(mask_av)
mask_av = av3.resize(av2.size).convert('L')
av = av1.copy()
av.paste(av2, (345, 170), mask_av)

#text
text = av
draw_text = ImageDraw.Draw(text)
font_01 = ImageFont.truetype(r'./fonts/TCCEB.ttf', 28)
font_02 = ImageFont.truetype(r'./fonts/TCCEB.ttf', 40)
draw_text.text((530, 160),NAME,(255,255,255),font=font_01)
draw_text.text((502, 220),POST,(255,255,255),font=font_02)
draw_text.text((615, 220),FOLLOWING,(255,255,255),font=font_02)
draw_text.text((775, 220),FOLLOWED,(255,255,255),font=font_02)


#insert theme
in1 = text
in2 = Image.open('./materials/white.jpg')
in3 = Image.open('./materials/info.jpg')
mask_info = Image.new("L", in2.size, 0)
draw_in = ImageDraw.Draw(mask_info)
mask_info = in3.resize(in2.size).convert('L')
info = in1.copy()
info.paste(in2, (298, 115), mask_info)
info.save('result.jpg', quality=95)