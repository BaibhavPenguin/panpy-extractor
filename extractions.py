import arguments as Args
import re


def DataExtractor(ExtractionPattern :str,ImageText :str):
    match = re.search(ExtractionPattern,ImageText)
    if match:
        return match.group()
    #Only Return if Match Was Found
    return None

def ExtractCardHolderName(RawText :str):
    FormattedLines = RawText.splitlines()
    
    for index , line in enumerate(FormattedLines):
        if "name" in line.lower() and "father" not in line.lower():
            temp_index = index;
            while FormattedLines[temp_index + 1] == " ":
                temp_index += 1
            
            pattern = r'^([a-zA-Z\s]+)'
            match = re.search(pattern,FormattedLines[temp_index + 1])
            if match:
                return match.group(1)
    
    return None

def ExtractFatherName(RawText :str):
    FormattedLines = RawText.splitlines()
    
    for index , line in enumerate(FormattedLines):
        if "father" in line.lower() and "name" in line.lower():
            temp_index = index;
            while FormattedLines[temp_index + 1] == " ":
                temp_index += 1
            
            pattern = r'^([a-zA-Z\s]+)'
            match = re.search(pattern , FormattedLines[temp_index + 1])
            if match:
                return match.group(1)
           
        
    return None
 
def ExtractPanData(ImageText :str):
    pan_number = DataExtractor(Args.ArgumentPatterns['PanNumberArg'],ImageText)
    birth_date = DataExtractor(Args.ArgumentPatterns['BirthParsingArg'],ImageText)
    card_holder_name = ExtractCardHolderName(ImageText)
    father_name = ExtractFatherName(ImageText)
    PanData = [card_holder_name,father_name,pan_number,birth_date]
    return PanData

