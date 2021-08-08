from pyzbar.pyzbar import decode, ZBarSymbol
from PIL import Image

def decode_ean13(filename):
    image = Image.open(filename)
    temp_results = decode(image, symbols=[ZBarSymbol.EAN13])
    results = []
    for temp_result in temp_results:
        results.append(temp_result.data.decode())
    return results
