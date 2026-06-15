import pytesseract
import cv2


def ImageTextExtractor(ImagePath :str):
   try:
        Img = cv2.imread(ImagePath,cv2.IMREAD_GRAYSCALE)
        Img = cv2.resize(Img,None,fx=2.5,fy=2.5,interpolation=cv2.INTER_CUBIC)
        Img = cv2.bilateralFilter(Img,9,75,75)
        ImageText = pytesseract.image_to_string(Img)
        return ImageText
   except FileNotFoundError:
        print(f"\033[31m{ImagePath} is not a valid image, skipping file...\033[0m")
        return None
   except cv2.error:
        print(f"\033[31m{ImagePath} is not a valid image, skipping file...\033[0m")
        return None
    

   
   
