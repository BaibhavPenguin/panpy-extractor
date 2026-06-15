from pathlib import Path

def return_file_name(Directory):
    valid_extentions = (".jpg",".png",".jpeg")
    images = Path(Directory)
    
    image_list = []
    try:
        for image in images.iterdir():
            if image.is_file() and image.suffix.lower()  in valid_extentions:
                image_list.append(image)
    except FileNotFoundError:
        print("\033[31mError! The directory provided is Empty or Invalid\033[0m")
        exit(-1)

    if len(image_list) > 0:
        return image_list
    else:
        return None