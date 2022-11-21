from typing import List
from typing import Tuple
from typing import Dict
from typing import Optional
from datetime import datetime
import json

import cv2


def cartoon_effect() -> Tuple[str, Dict]:
    """
    This method gives the input image cartoon effect.

    What do the parameters sigma_s and sigma_r mean ?

    Most smoothing filters (e.g. a Gaussian or a Box filter) in image processing and computer vision have a parameter
    called sigma_s (for Sigma_Spatial) that determines the amount of smoothing. A typical smoothing filter replaces
    the value of a pixel by the weighted sum of its neighbors. The bigger the neighborhood, the smoother the filtered
    image looks. The size of the neighborhood is directly proportional to the parameter sigma_s.

    In edge preserving filters there are two competing objectives — a) smooth the image b) don’t smooth the edges /
    color boundaries. In other words we cannot simply replace the color of a pixel by the weighted sum of its
    neighbors. Instead, we want to replace the color value at a pixel by the average of pixels in the neighborhood
    which also have color similar to the pixel. So we have two parameters : sigma_s and sigma_r. Just like other
    smoothing filters sigma_s controls the size of the neighborhood, and sigma_r (for sigma_range) controls the how
    dissimilar colors within the neighborhood will be averaged. A larger sigma_r results in large regions of constant
    color.

    :parameter: None

    :return: A Tuple which consists of
    filename
    {"effect": effect, "sigma_r": sigma_r, "sigma_s": sigma_s, "shade_factor": shade_factor}
    """

    effect = input("Which effect do you want?(cartoon, sketch, detail): ")
    path = input("Input the path of image(A path can be Absolute or Relative path): ")
    sigma_s = int(input("How many smooth? 0<=sigma_s<=200 (int type): "))
    sigma_r = float(input("How many smooth? 0.0<=sigma_r<=1.0 (float type): "))
    file = path.split(".")
    addition_name = None
    which_sketch = None
    effect_img = None
    shade_factor = None

    img = cv2.imread(path, cv2.IMREAD_COLOR)
    cv2.imshow('original', img)

    if effect == "cartoon":
        addition_name = "_cartoon_effect."
        effect_img = cv2.stylization(img, sigma_s=sigma_s, sigma_r=sigma_r)
        cv2.imshow('cartoon', effect_img)
    elif effect == "sketch":
        which_sketch = input("Which sketch do you want?(gray/color): ")
        shade_factor = float(input("Input Shade_factor(0.0<=float<=1.0): "))
        dst_gray, dst_color = cv2.pencilSketch(img, sigma_s=sigma_s, sigma_r=sigma_r, shade_factor=shade_factor)
        if which_sketch == "gray":
            cv2.imshow('pencil_gray', dst_gray)
            effect_img = dst_gray
            addition_name = "_gray_sketch_effect."
            effect = "sketch_pencil_gray"
        else:
            cv2.imshow('pencil_color', dst_color)
            effect_img = dst_color
            addition_name = "_color_sketch_effect."
            effect = "sketch_pencil_color"
    else:
        effect_img = cv2.detailEnhance(img, sigma_s=sigma_s, sigma_r=sigma_r)
        cv2.imshow('enhancement', effect_img)
        addition_name = "_detail_enhancement_effect."

    filename = file[0] + addition_name + file[1]
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imwrite(filename, effect_img)

    return filename, {"effect": effect, "sigma_r": sigma_r, "sigma_s": sigma_s, "shade_factor": shade_factor}


def create_metadata(ipfs_uri: str, filename: str, attribute: Dict) -> None:
    """
    This method makes a metadata about the input image cartoon effect.

    :param: description, ipfs_uri, image_name, attribute

    :return: None
    """
    today = datetime.today()
    description = input("Describe about your NFT item: ")

    metadata = {
        "description": description,
        "external_url": "This is the URL that will appear below the assets's\
                         image on OpenSea and will allow users to leave OpenSea and view the item on your site.",
        "image": "ipfs URI",
        "name": filename,
        "create_date": f"{today.year}-{today.month}-{today.day},{today.hour}:{today.minute}:{today.second}",
        "token_id": "if token_id, put it",
        "attribute": attribute,
    }
    with open(f'{filename}.json', 'w') as f:
        json.dump(metadata, f, indent=2)


if __name__ == "__main__":
    # In below the code, we can create the image with a certain effect.
    filename, attribute = cartoon_effect()

    # In this part, We can use JS API to upload the image file and create ipfs URI.
    ipfs_uri = "Through JS API, We also can get ipfs URI"

    # We can create metadata about the image.
    create_metadata(ipfs_uri, filename, attribute)
