
from PIL import Image

import binascii


def extract_message(filename: str) -> str:

    im = Image.open(filename,'r')

    pix_val = list(im.getdata())

    pixval_rgbt = []
    pixval_binary = []
    templist = ''
    secretText = ''


    i = 0
    b = 0
    c = 0
    l = 0

    #transform to rgbt
    while i < len(pix_val):

        pixval_rgbt.append(pix_val[i]+pix_val[i+1])

        i = i + 2

    #transform to binary
    while b < len(pixval_rgbt):
        while c < len(pixval_rgbt[b]):
            templist = templist + str(pixval_rgbt[b][c] & 1)
            c = c + 1
        pixval_binary.append(templist)
        templist = ""
        c = 0
        b = b + 1

    # get the word
    while l < len(pixval_binary):
        if pixval_binary[l] != '11111111':
            secretText = secretText + pixval_binary[l]

        l = l + 1

    return pixval_binary



# funtion to transform binary to text
def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return int2bytes(n).decode(encoding, errors)

# support function
def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))


print(extract_message('C:\\Users\\stani\\OneDrive\\Documents\\white-small.bmp'))

print(254 & 1)