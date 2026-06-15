import image_data_extraction as ImgExt
import extractions as Extract
import file_manager as Files
import openpyxl as Excel

try:
    print("panpy-extractor v1 , tesseract 5.5.0 , opencv cv2 4.10.0 ")
    directory = str(input("Enter input directory which contains images to be processed : "))
    Folder = Files.return_file_name(directory)


    wb = Excel.Workbook()
    ws = wb.active
    ws.title = "Extracted PAN Details"
    headers = ["Name","Father's Name","PAN Number","DOB"]
    ws.append(headers)



    for index in Folder:
        print(f"Starting extraction of {index}")
        ExtractedText = ImgExt.ImageTextExtractor(index)
        PanData = Extract.ExtractPanData(ExtractedText)
        if all(PanData):
            ws.append(PanData)
            print(f"\033[32mSuccess! , Extracted data from {index}\033[0m")
        else:
            print(f"\033[31mAborted extration of {index}, Reason : Invalid Detection!\033[0m")
            print(f"\033[33mPlease try again and make sure that the image is clear and shot in a bright enviornment!\033[0m")
            continue
    
    wb.save("panpy-extract.xlsx")
    print("\033[32mData extraction completed successfully!\033[0m")
except TypeError as Err:
    print("\033[31mError! No images found!\033[0m")
    exit(-1)
except KeyboardInterrupt:
    print("\033[31mInterrupted By User\033[0m")
    exit(-1)



