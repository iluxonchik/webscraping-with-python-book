from PIL import Image
import subprocess

def cleanFile(filePath, newFilePath):
    image = Image.open(filePath)

    # Set a threshold value for image and save
    image = image.point(lambda x: 0 if x < 143 else 255)
    image.save(newFilePath)

    # do OCR on the newly created image
    subprocess.call(["tesseract", newFilePath, "output"])

    outputFile = open("output.txt", "r")
    print(outputFile.read())
    outputFile.close()

cleanFile("tesseract_gradient.png", "processed_gradient.png")