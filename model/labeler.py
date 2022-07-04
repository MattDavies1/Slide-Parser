# Dependencies
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import image
from skimage.filters import threshold_otsu
from skimage.measure import label, regionprops
from skimage.morphology import closing, square
from skimage.color import rgb2gray
import io
from PIL import Image

def preview_labling(file_location_input: str):
    """
    Take path to file to be previewed as a string and return an image with drawn boxes denoting detected objects
    """
    # load image from path
    image_start = image.imread(file_location_input)

    # get area of image for region size threshold
    threshold_percent_size = 0.005 # tunable parameter in the future
    height, width, _ = image_start.shape
    image_area = height * width
    region_min_size_threshold = image_area*threshold_percent_size
    region_max_size_threshold = image_area*0.9

    # apply threshold
    image_bw = rgb2gray(image_start)
    thresh = threshold_otsu(image_bw)
    bw = closing(image_bw > thresh, square(3))

    # add image labels to identify slides
    label_image = label(bw)

    # create image 
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.imshow(image_start)

    # draw boxes on image
    for region in regionprops(label_image):
        if (region.area >= region_min_size_threshold) & (region.area <= region_max_size_threshold):
            minr, minc, maxr, maxc = region.bbox
            rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                                    fill=False, edgecolor='red', linewidth=2)
            ax.add_patch(rect)

    # format image
    ax.set_axis_off()
    plt.tight_layout()

    # collect image to be returned
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    labelled_preview_image = Image.open(buf)

    return labelled_preview_image
