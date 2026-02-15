from PIL import Image

img = Image.open("450aba14db99201a77de4458ac152673.jpg")
img.save("icono.ico", format="ICO", sizes=[(64, 64)])
print("Ícono criado!")