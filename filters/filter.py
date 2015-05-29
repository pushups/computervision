import cv2
import sys
from matplotlib import pyplot as plt
import numpy as np

def load_image(image_file):
    image = cv2.imread(image_file)
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

def image_value_at_index(index, image, image_size):

    index_x = index[0]
    index_y = index[1]

    max_x = image_size[0] - 1
    max_y = image_size[1] - 1
    # Handle 4 edges and 4 corners
    # Top left corner
    if index_x < 0 and index_y < 0:
        return image[0, 0]

    # Top edge
    if index_x >= 0 and index_x <= max_x and index_y < 0:
        return image[index_x, 0]

    # Top right corner
    if index_x > max_x and index_y < 0:
        return image[max_x, 0]

    # Right edge
    if index_x > max_x and index_y >= 0 and index_y <= max_y:
        return image[max_x, index_y]

    # Bottom right corner
    if index_x > max_x and index_y > max_y:
        return image[max_x, max_y]

    # Bottom edge
    if index_x >= 0 and index_x <= max_x and index_y > max_y:
        return image[index_x, max_y]

    # Bottom left corner
    if index_x < 0 and index_y > max_y:
        return image[0, max_y]

    # Left edge
    if index_x < 0 and index_y >= 0 and index_y <= max_y:
        return image[0, index_y]

    # Otherwise just return the pixel, we're not off the edge
    return image[index_x, index_y]

def filter(image, kernel):
    new_image = image
    kernel_offset = (len(kernel) - 1) / 2
    for index, val in np.ndenumerate(image):
        new_value = 0
        for kernel_index, kernel_value in np.ndenumerate(kernel):
            target_index = (index[0] + kernel_index[1] - kernel_offset,
                            index[1] + kernel_index[0] - kernel_offset)
            new_value += image_value_at_index(target_index, image, image.shape)*kernel_value

        new_image[index] = new_value

    return new_image

def plot(image_list):
    subplot = 222
    for image, name in image_list:
        plt.subplot(subplot)
        plt.imshow(image, 'gray')
        plt.title(name)
        subplot += 1
    plt.show()

image_file = sys.argv[1]

image = load_image(image_file)

gray_scale = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

kernel = [[1, 1, 1],
          [1, 1, 1],
          [1, 1, 1]]

filtered = filter(gray_scale, kernel)

plot([(image, image_file), (filtered, 'gray')])
