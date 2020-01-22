from astropy.io import fits
from astropy.utils.exceptions import AstropyUserWarning

import warnings
from pathlib import Path

import argparse


parser = argparse.ArgumentParser(description="Simple tool to check for corrupted fits file images.",
                                     epilog="Please email hsouchereau@outlook.com for help inquiries or bug reports.")

parser.add_argument("image_directory", type=str,
                        help="Top-level directory containing FITS files or subdirectories. The program will recursively" +
                    " search for files in subdirectories using rglob.")

args = parser.parse_args()

top_level_dir = args.image_directory


# Ignore all warnings (since corrupted images tend to generate infinte loops)
warnings.filterwarnings("ignore")


# Get all filenames
image_filenames = []
for filename in Path(top_level_dir).rglob('*.fits'):
    image_filenames.append(str(filename))

bad_counter = 0

for fits_filename in image_filenames:
    try:
        # print("Trying to Open: ", fits_filename)
        with fits.open(fits_filename) as HDUList:
            # print(fits_filename + "\t\topened successfully:\t" + str(len(HDUList)) + " hdus")
            pass
    except AstropyUserWarning:
        print("ERROR OPENING" + fits_filename)
        bad_counter += 1
    except OSError:
        print("ERROR OPENING" + fits_filename)
        bad_counter += 1
        continue

if bad_counter == 0:
    print("Image Directory has no bad or corrupted images!")
else:
    print("Image Directory potentially has", bad_counter,  "corrupted images.")
