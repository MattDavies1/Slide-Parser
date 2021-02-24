# Dependancies
import matplotlib.pyplot as plt
from matplotlib import image

from skimage.filters import threshold_otsu
from skimage.measure import label, regionprops
from skimage.morphology import closing, square
from skimage.color import label2rgb
from skimage.color import rgb2gray

image = image.imread("IMG_1452.jpg")
cropped_img = image[0:-100, 350:-100]

# apply threshold
image = rgb2gray(cropped_img) 
thresh = threshold_otsu(image)
bw = closing(image > thresh, square(3))

# add image labels to identify slides
label_image = label(bw)

# iterate through objects to output desired selections
for region in regionprops(label_image):
    # take regions with large enough areas
    if region.area >= 75000:
        # draw rectangle around segmented coins
        minr, minc, maxr, maxc = region.bbox
        # create output figure
        fig, ax = plt.subplots(figsize=(12, 4))
        plt.imshow(cropped_img[minr:maxr,minc:maxc])
        ax.set_axis_off()
        plt.tight_layout()
        # save to outputs
        fig.savefig(f'outputs/slide{regionprops(label_image).index(region)}.png')
