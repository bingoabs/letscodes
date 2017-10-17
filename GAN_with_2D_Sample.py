from functools import partial
import numpy
from skimage import transform

EPs = 1e-6
RESOLUTION = 0.001
num_grids = int(1/RESOLUTION + 0.5)

def generate_lut(img):
    """
    linear approximation of CDF & marginal
    :param density_img
    :return: lut_y, lut_x
    """
    density_img = transform.resize(img, (num_grids, num_grids))
    x_acculation = numpy.sum(density_img, axis=1)
    # find lack math knowledge, so left out.
    pass


if __name__ == "__main__":
    pass 
    
    
