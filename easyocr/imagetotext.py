import easyocr



def imagetotext():
    reader=easyocr.Reader(['en'])
    results= reader.readtext('frame.png')
    data=''
    for (bbox,text,conf) in results:
        data+=(text+' ')

    return data





