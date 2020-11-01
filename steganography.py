# Authors: Jaxon Terrell, Denisha Pimentel-Sanchez, Talia Tomarchio
# Script that uses the RSA Algorithm to encrypt a message, then altering an image files's
# individual RGB values of certain pixels to hide the data from the message. This change to the image is generally
# not easily visible to the human eye
# This program also allows for decryption of an image, as long as it is of the .tiff format. Once the image
# is decrypted, it prints out the message

import random
from decimal import Decimal 
from PIL import Image

def gcd(a,b): 
    if b==0: 
        return a 
    else: 
        return gcd(b,a%b)

# Implement the RSA algorithm dependent on user entered p and q values
def RSA_Algorithm():
    p = int(input('Enter the value of p = ')) 
    q = int(input('Enter the value of q = ')) 
    no = int(ascii_text)
    n = p*q 
    t = (p-1)*(q-1) 
  
    for e in range(2,t): 
        if gcd(e,t)== 1: 
            break
    for i in range(1,10): 
        x = 1 + i*t 
        if x % e == 0: 
            d = int(x/e) 
            break
    ctt = Decimal(0) 
    ctt =pow(no,e) 
    ct = ctt % n 
  
    dtt = Decimal(0) 
    dtt = pow(ct,d) 
    dt = dtt % n 
    return str(ct)

# Convert each character string to ASCII value and concatenate them
# with parameters (string, bit size)
def stringToAscii(s, b):
    bit = "%0" + str(b) + "d"
    return "".join(bit % ord(i) for i in s)

# Split the ascii string dependening on bit size of character
def splitString(text, size):
    arr = []
    i = 0
    j = size 
    for x in range(0, (len(text)//size)):
        arr.append(int(text[i:j]))
        i = j 
        j = j + size   
    return arr

# Use random pseudo generator to get pixel's location
# parameters: range (a, b)
def randomGeneratePixels(password, text_size, a, b):
    arr = []
    random.seed(password)
    for i in range(0, text_size):
        randVal = random.randint(a, b)
        pixelRow = randVal//im.size[0]
        pixelColumn = randVal%im.size[1]
        arr.append((pixelRow, pixelColumn))
    return arr

#Return pixels' RGB value
def randomGenerateRGB(p_arr):
    arr=[]
    im.convert("RGB")    
    for i in range(0, (len(p_arr))):
        curr_pixel = p_arr[i]
        rgbValue = im.getpixel((curr_pixel[0], curr_pixel[1]))
        arr.append(rgbValue)
    return arr
    
#Change RGB values in sequence and substitute for the corresponding character's ascii value
#args(quantity, password, bits)
def replacePixels(rgb_arr, split_p):
    arr = []
    color = 'r'

    bin_c = 0
    for i in range(0, len(rgb_arr)):
        curr_pixel = list(rgb_arr[i])
        bin_p = format(split_p[i], '08b')
        
        if color == 'r': 
            bin_g = format(curr_pixel[1], '08b') #binary number for green
            bin_b = format(curr_pixel[2], '08b') #binary number for blue
            curr_pixel[1] = int(bin_g[:4] + bin_p[:4], 2)  #change last 4 bits in green
            curr_pixel[2] = int(bin_b[:4] + bin_p[4:], 2)  #change last 4 bits in blue
            color = 'g'
        elif color == 'g': 
            bin_r = format(curr_pixel[0], '08b') #binary number for red
            bin_b = format(curr_pixel[2], '08b') #binary number for blue
            curr_pixel[0] = int(bin_r[:4] + bin_p[:4], 2)  #change last 4 bits in red
            curr_pixel[2] = int(bin_b[:4] + bin_p[4:], 2)  #change last 4 bits in blue  
            color = 'b'
        elif color == 'b':
            bin_r = format(curr_pixel[0], '08b') #binary number for blue
            bin_g = format(curr_pixel[1], '08b') #binary number for green
            curr_pixel[0] = int(bin_r[:4] + bin_p[:4], 2)  #change last 4 bits in red
            curr_pixel[1] = int(bin_g[:4] + bin_p[4:], 2)  #change last 4 bits in green   
            color = 'r'
            
        arr.append(curr_pixel)
      
    return arr;

# Save the modified image
def modimagetest(im, rgb_arr, p_arr): 
    px = im.load()  # Get the pixels in the image
 
    for i in range(0, len(p_arr)):
        val = p_arr[i]
        px[val[0], val[1]] = tuple(rgb_arr[i])
    im.show()
    save_file = "encrypted_image.tiff"
    im.save(save_file)
    return save_file


# Decrypts the hidden message in picture
def getHiddenMessage(d_arr):
    px = im2.load() 
    im2.convert("RGB")   
    p_arr = []
    color = 'r'
    curr_pixel = ()
    hidden_c = 0
    for i in range(0, len(d_arr)):
        curr_pixel = list(d_arr[i])
        rgbValue = im2.getpixel((curr_pixel[0], curr_pixel[1]))
        if color == 'r':
            bin_g = format(rgbValue[1], '08b') #binary number for red
            bin_b = format(rgbValue[2], '08b') #binary number for blue
            hidden_c = int(bin_g[4:] + bin_b[4:], 2)  #change last 4 bits in blue
            color = 'g'
        elif color == 'g': 
            bin_r = format(rgbValue[0], '08b') #binary number for red
            bin_b = format(rgbValue[2], '08b') #binary number for blue
            hidden_c = int(bin_r[4:] + bin_b[4:], 2)  #change last 4 bits in blue
            color = 'b'
        elif color == 'b':
            bin_r = format(rgbValue[0], '08b') #binary number for red
            bin_g = format(rgbValue[1], '08b') #binary number for blue
            hidden_c = int(bin_r[4:] + bin_g[4:], 2)  #change last 4 bits in blue
            color = 'r'   
        p_arr.append(hidden_c)        
    s = ""
    for i in range(0, len(p_arr)):
         s += chr(p_arr[i])
    
    return s

if __name__ == "__main__":        
    plaintext = input("Please enter a message to encrypt: ")
    bits = 16
    bitSize = 4 
    password = "abc"
    ascii_text = stringToAscii(plaintext, 4)
    print("Enter values for RSA Algorithm:")
    cipherText = RSA_Algorithm()
    split_plaintext = splitString(ascii_text, bitSize)
    IMAGE_FILE = str(input("Please enter the filepath of your image: "))
    if IMAGE_FILE == "":
        print("Invalid entry. Image will default to picutre of a cute dog...")
        IMAGE_FILE="doggy_image.jpg"
    else:
        print("We will hide text in " + IMAGE_FILE)
    im = Image.open(IMAGE_FILE)
    print(im.format, im.size, im.mode)
    pixel_Arr = randomGeneratePixels(password, len(split_plaintext), 0, 133333)
    RGB_Arr = randomGenerateRGB(pixel_Arr)
    #Setting the array with the new RGB values to the variable
    replaced_RGB_Arr = replacePixels(RGB_Arr, split_plaintext)
    modimagetest(Image.open(IMAGE_FILE), replaced_RGB_Arr, pixel_Arr)
    # Decrypt updated image
    IMAGE_FILE2 = "encrypted_image.tiff"
    im2 = Image.open(IMAGE_FILE2)
    dec_Arr = randomGeneratePixels(password, len(split_plaintext), 0, 133333)
    print(f'The decrypted message is: {getHiddenMessage(dec_Arr)}')