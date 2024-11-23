# Define all extensions first
def gif():
    print("image/gif")

def jpeg():
    print("image/jpeg")

def png():
    print("image/png")

def pdf():
    print("application/pdf")

def txt():
    print("text/plain")

def zip():
    print("application/zip")

def octet():
    print("application/octet-stream")

# Then ask for the file's name
file = str.lower(input("Insert file's name: ")).strip()

# From here we start decomposing to reach the conditionals
gifv = file.endswith(".gif")

jpegv = file.endswith(".jpeg")

jpgv = file.endswith(".jpg")

pngv = file.endswith(".png")

pdfv = file.endswith(".pdf")

txtv = file.endswith(".txt")

zipv = file.endswith(".zip")

# And we start with the conditionals
if gifv == True:
    gif()

elif jpegv == True or jpgv == True:
    jpeg()

elif pngv == True:
    png()

elif pdfv == True:
    pdf()

elif txtv == True:
    txt()

elif zipv == True:
    zip()

else:
    octet()