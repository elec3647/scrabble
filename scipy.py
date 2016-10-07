from matplotlib.pyplot import imread
from matplotlib.testing.compare import compare_images
from numpy import average
import numpy
from numpy.ma import subtract
import matplotlib.pyplot as plt
__author__ = 'kreitzem'


def to_grayscale(arr):
    "If arr is a color image (3D array), convert it to grayscale (2D array)."
    if len(arr.shape) == 3:
        return average(arr, -1)  # average over the last axis (color channels)
    else:
        return arr


def main():
    #file1, file2 = sys.argv[1:1 + 2]
    file1 = "/Users/kreitzem/Desktop/scrabble/WWF_layout.png"
    file2 = "/Users/kreitzem/Desktop/scrabble/WWF_tiles.png"
    # read images as 2D arrays (convert to grayscale for simplicity)
    #img1 = imread(file1)
    img1 = (imread(file1).astype(float))
    img2 = (imread(file2).astype(float))
    print img1.shape, img2.shape
    print img1.dtype, img2.dtype

    #x = (img2.shape[0]-img1.shape[0])/2
    #y = (img2.shape[1]-img1.shape[1])/2
    #img2 = img2[x:-x, y:-y]
    print img1.shape, img2.shape
    img3 = subtract(img2, img1)
    #plt.imshow(img3)
    plt.imsave('boo.png',img3)
    #a = raw_input("boo")
    # compare
    #n_m, n_0 = compare_images(img1, img2,0)
    #print "Manhattan norm:", n_m, "/ per pixel:", n_m / img1.size
    #print "Zero norm:", n_0, "/ per pixel:", n_0 * 1.0 / img1.size



main()