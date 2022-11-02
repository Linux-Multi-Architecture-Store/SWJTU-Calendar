import ddddocr


def captcha(img_dir):
    with open(img_dir, 'rb') as f:
        img = f.read()
    ocr = ddddocr.DdddOcr()
    text = ocr.classification(img)
    return str(text)
