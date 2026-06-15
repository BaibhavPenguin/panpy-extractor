# **Panpy Extractor &mdash; The Python based automation tool for PAN Data Extraction**  
**Panpy Extractor** is a python based utility for automatically extracting crucial data fields namely, PAN (Permanent Account Number) , Date-of-Birth , Name of Card Holder and Father's Name from an image and generate a spreadsheet with the extracted data. It is made sepcifically to be used with hundreds of images at once and uses Pytesseract and OpenCV for OCR functionality.

**Panpy Extractor** is completely local and offline hence , all your data is safe and highly secure on your computer. Panpy Extractor has very high accuracy given that it is working with clear and bright images. It is exceptionally well when used along with scanned images obtained from CamScanner or DocScanner.

## **Dependencies**
- **Python3**
- **Tesseract 5.5.0**
- **OpenCV cv2 4.10.0**
- **openpyxl**

## **Usage**
**Panpy Extractor** will be released as a complete docker image so that users wont have to download dependencies in the near future.
## Docker
Not released yet.  
## GitHub Clone
*Clone the repository*  
`git clone https://github.com/BaibhavPenguin/panpy-extractor`  

*Download tesseract ocr*  
`sudo apt install tesseract `  

*Download Dependencies*  
`pip3 install openpxyl opencv pytesseract `  
*or*  
`sudo apt install python3-openpxyl`  
`sudo apt install python3-opencv`   
`sudo pip3 install python3-pytesseract --break-system-packages ` 

*Run the Script*  
`cd panpy-extractor `  
`python3 panpy-extractor`  

# **Other Important information**  
## **User Guide**
**Panpy Extractor** works best when used with clear and sharp images taken in a bright room.  
- Use images taken against a flat surface.    

- Make sure to confirm that critical details are visible in the image.  

- Make sure to use straight images, if they are too tilted or are of different 
    orientations, the script will not extract the data.

- In case for extracting PAN Letters or EPAN Documents, Please crop the image 
    to only include the flash-card part of the document.

- **Panpy Extractor** has not been tested with a very large amount of data so please make sure that you're confirming the output as it may be inaccurate for unlisted edge cases.

## **Interface**
**Panpy Extractor** takes a Directory as an input and outputs am xlsx file named **panpy-extract.xlsx** , if the directory is invalid or the images are corrupt, panpy extractor will raise errors and abort processing.  
In case if any images are invalid or data extraction of all required fields (Name,Father's Name,DOB,Pan Number) isn't possible, that specific file will be skipped and the user will be notified.  

**Panpy Extractor** is completely free and open-source for anyone to use and modify. it is Licenced under the <a href="LICENSE">Apache 2.0 License</a> 

## **Credits**
*Panpy extractor* is developed by **Baibhav Bhattacharya** <a href="https//:github,com/BaibhavPenguin">BaibhavPenguin</a> on GitHub.