# Dependencies
import matplotlib.pyplot as plt
from matplotlib import image
from skimage.filters import threshold_otsu
from skimage.measure import label, regionprops
from skimage.morphology import closing, square
from skimage.color import rgb2gray

def slide_parsing_routine(file_location_input: str, folder_location_output: str, input_sample_name: str):
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

    counter = 1

    for region in regionprops(label_image):
        # take regions with large enough areas
        if (region.area >= region_min_size_threshold) & (region.area <= region_max_size_threshold):
            # draw rectangle around segmented coins
            minr, minc, maxr, maxc = region.bbox
            fig, ax = plt.subplots(figsize=(12, 4))
            plt.imshow(image_start[minr:maxr,minc:maxc])
            ax.set_axis_off()
            plt.tight_layout()
            # plt.show()
            fig.savefig(f'{folder_location_output}/{input_sample_name}_{counter}.png')
            # increment counter
            counter += 1

    return f'Parse Completed: {counter - 1} slides identified'
