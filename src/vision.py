import easyocr

reader = easyocr.Reader(['en'])
result = reader.readtext('testpicture.png')


for detection in result:
    print(detection)

