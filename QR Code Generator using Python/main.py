# import qrcode
# url=input("Enter the URL: ")
# filename=input("Enter File Name you want to save as: ")
# if not(filename.endswith(".png")):
#     filename=filename+".png"

# img = qrcode.make(url)
# img.save(filename)

# import qrcode

# url = input("Enter the URL: ")
# filename = input("Enter File Name you want to save as: ")

# if not filename.endswith(".png"):
#     filename += ".png"

# img = qrcode.make(url)
# img.save(filename)

# print(f"QR Code saved as {filename}")

import qrcode
img = qrcode.make('www.linkedin.com/in/gauravdatir')
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")