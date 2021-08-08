import barcode

imagefilename = "N:/test/202003/014-be17e58a-41a2-11ea-9102-0025902b0603-1.pdf_1.png"
results = barcode.decode_ean13(imagefilename)
print(results)