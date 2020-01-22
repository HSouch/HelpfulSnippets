from astropy.io import fits
from astropy.utils.exceptions import AstropyUserWarning

import warnings
from pathlib import Path

from astropy.wcs import wcs
from astropy.table import Table

from numpy import ndarray

import argparse


def get_wcs(fits_filename):
    """ Finds and returns the WCS for an image. If Primary Header WCS no good, searches each index until a good one
        is found. If none found, raises a ValueError
    """
    # Try just opening the initial header
    wcs_init = wcs.WCS(fits_filename)
    ra, dec = wcs_init.axis_type_names
    if ra.upper() == "RA" and dec.upper() == "DEC":
        return wcs_init

    else:
        hdu_list = fits.open(fits_filename)
        for n in hdu_list:
            try:
                wcs_slice = wcs.WCS(n.header)
                ra, dec = wcs_slice.axis_type_names
                if ra.upper() == "RA" and dec.upper() == "DEC":
                    return wcs_slice
            except:
                continue
        hdu_list.close()

    raise ValueError


output_table_filename = "coverage.fits"


parser = argparse.ArgumentParser(description="Simple tool to check for corrupted fits file images.",
                                     epilog="Please email hsouchereau@outlook.com for help inquiries or bug reports.")

parser.add_argument("image_directory", type=str,
                        help="Top-level directory containing FITS files or subdirectories. The program will recursively" +
                    " search for files in subdirectories using rglob.")

parser.add_argument("-o", "--output", type=str,
                    help="Name of output table. Defaults to 'coverage.fits' if not specified.")

args = parser.parse_args()

top_level_dir = args.image_directory

if type(args.output) == str:
    output_table_filename = args.output


# Ignore all warnings (since corrupted images tend to generate infinte loops)
warnings.filterwarnings("ignore")


rows = []

# Get all filenames
image_filenames = []
for filename in Path(top_level_dir).rglob('*.fits'):
    image_filenames.append(str(filename))

for filename in Path(top_level_dir).rglob('*.fit'):
    image_filenames.append(str(filename))


for fits_filename in image_filenames:
    try:
        # print("Trying to Open: ", fits_filename)
        with fits.open(fits_filename) as HDUList:
            w, img = None, None
            try:
                w = get_wcs(fits_filename)
                for n in range(0, len(HDUList)):
                    img = HDUList[n].data
                    if type(img) == ndarray:
                        break

            except ValueError:
                print("Error with getting WCS or image for:\t" + fits_filename)
                continue

            ra_1, dec_1 = w.wcs_pix2world(0, 0, 0)
            ra_2, dec_2 = w.wcs_pix2world(img.shape[0], img.shape[1], 0)

            print(fits_filename, ra_1, ra_2, dec_1, dec_2)

            rows.append((fits_filename, ra_1, ra_2, dec_1, dec_2))

            # print(fits_filename + "\t\topened successfully:\t" + str(len(HDUList)) + " hdus")
            pass
    except AstropyUserWarning:
        print("ERROR OPENING" + fits_filename)
    except OSError:
        print("ERROR OPENING" + fits_filename)
        continue


t = Table(rows=rows, names=("Image Filename", "ra_1", "ra_2", "dec_1", "dec_2"))
t.write(output_table_filename)

