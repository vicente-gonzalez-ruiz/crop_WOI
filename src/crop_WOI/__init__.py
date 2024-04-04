'''Crop an object in a black and white image.'''

import numpy as np

import logging
logger = logging.getLogger(__name__)
logging.basicConfig(format="[%(filename)s:%(lineno)s %(funcName)s()] %(message)s")
#logger.setLevel(logging.CRITICAL)
#logger.setLevel(logging.ERROR)
#logger.setLevel(logging.WARNING)
logger.setLevel(logging.INFO)
#logger.setLevel(logging.DEBUG)

try:
    IN_COLAB = True
except:
    IN_COLAB = False
logger.info(f"Running in Google Colab: {IN_COLAB}")

def crop_WOI(img, x, y, xx, yy):
    info = "crop_WOI\t"
    info += f"x_coordinate={x}\t"
    info += f"y_coordinate={y}\t"
    info += f"xx_coordinate={xx}\t"
    info += f"yy_coordinate={yy}"
    WOI = img[y:yy, x:xx]
    #print(np.max(WOI))
    return WOI, info

if __name__ == "__main__":

    def int_or_str(text):
        '''Helper function for argument parsing.'''
        try:
            return int(text)
        except ValueError:
            return text

    import argparse
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.description = __doc__

    parser.add_argument("-i", "--input", type=int_or_str,
                        help="Prefix of the input image sequence",
                        default="/tmp/input")
    
    parser.add_argument("-o", "--output", type=int_or_str,
                        help="Prefix of the output image sequence",
                        default="/tmp/output")

    parser.add_argument("-e", "--extension", type=int_or_str,
                        help="Image extension",
                        default=".png")

    args = parser.parse_args()

    import sequence_iterator

    class CropWOI(sequence_iterator.ImageSequenceIterator):
        def process(self, image):
            return crop_WOI(image, x, y, xx, yy)

    iterator = WarpSequence(
        input_sequence_prefix="/tmp/input",
        output_sequence_prefix="/tmp/output",
        image_extension="png")

    iterator.process_sequence()

    logger.info(f"Your files should be in {args.output}")

