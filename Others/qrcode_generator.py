import qrcode

data = input("Enter data:")
file_name = input("Enter file name and press ENTER:")

img = qrcode.make(data)
type(img)
img.save(f"{file_name}.png")
