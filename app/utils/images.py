from PIL import Image


def get_new_width_and_height(img, new_width=500,):
    img = Image.open(img)
    if img.width <= 500:
        return img.size
    new_height = (img.height * new_width) / img.width
    img.close()
    return (new_width, new_height)
