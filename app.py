# Dependancies
import matplotlib.pyplot as plt
from matplotlib import image
from skimage.filters import threshold_otsu
from skimage.measure import label, regionprops
from skimage.morphology import closing, square
from skimage.color import label2rgb
from skimage.color import rgb2gray
import os
import glob




# Smarter Image read-in functioinality
path = os.path.join('inputs', '*.jpg')

filepath = glob.glob(path)
filepath

image = image.imread(filepath[0])
start_image = image
print("Image loaded")

# apply threshold
image = rgb2gray(image)
thresh = threshold_otsu(image)
bw = closing(image > thresh, square(3))

# add image labels to identify slides
label_image = label(bw)

counter = 0

for region in regionprops(label_image):
    # take regions with large enough areas
    if region.area >= 75000:
        # draw rectangle around segmented coins
        minr, minc, maxr, maxc = region.bbox
        fig, ax = plt.subplots(figsize=(12, 4))
        plt.imshow(start_image[minr:maxr,minc:maxc])
        ax.set_axis_off()
        plt.tight_layout()
        # plt.show()
        fig.savefig(f'outputs/output{counter + 1}.png')
        print(f'Parsing slide {counter + 1} ...')
        counter += 1

print(f'Parser identified {counter} slides')
