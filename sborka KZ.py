from PIL import Image
from PIL.ImageChops import difference


layer1 = Image.open("shassi.png")
layer2 = Image.open("stekla.png")
layer3 = Image.open("kuzov.png")
layer4 = Image.open("bamper.png")
layer5 = Image.open("teni.png")

layer1.paste(layer2,(0,0),layer2)
layer1.paste(layer3,(0,0),layer3)
layer1.paste(layer4,(0,0),layer4)

layer1 = Image.alpha_composite(layer1, layer5)
#layer1 = Image.alpha_composite(layer1, layer5)
layer1.save("kz.png", "PNG")
