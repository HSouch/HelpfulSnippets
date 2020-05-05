"""
Compiles all FITS files in an input directory into one.
"""

import time
import argparse
from astropy.io import fits
from pathlib import Path


input_directory = ""
output_filename = "output.fits"


def process_arguments():
    """ Gather all user arguments, and set global variables if necessary. """
    global input_directory
    global output_filename

    parser = argparse.ArgumentParser(description="A simple tool to compile FITS files together." +
                                                 " Definitely can be improved, but works okay for small->medium dirs.",
                                     epilog="Please email hsouchereau@outlook.com for bug reports.")

    parser.add_argument("input_dir", type=str,
                        help="Input directory containing the FITS files to be compiled.")
    parser.add_argument("output_filename", type=str,
                        help="Name of file to save the output file as.")

    # Get all input arguments
    args = parser.parse_args()

    input_directory = args.input_dir
    output_filename = args.output_filename

    return args


arguments = process_arguments()


def compile_files(directory, compiled_filename):
    compiled_HDUList = fits.HDUList()
    open_hdulists = []

    input_files = []
    for n in Path(directory).rglob("*.fits"):
        input_files.append(str(n))

    print("Compiling all HDULists in " + directory)

    for filename in input_files[:]:
        HDUList = fits.open(filename)

        for hdu in HDUList.copy():
            compiled_HDUList.append(hdu)

        open_hdulists.append(HDUList)

    #         print("Adding\t", len(HDUList), "\thdus ", "\tNew Length:", len(compiled_HDUList))
    #         os.system('cls')

    print("Saving compiled HDUList.")

    if not compiled_filename.endswith(".fits"):
        compiled_filename += ".fits"

    compiled_HDUList.writeto(compiled_filename, overwrite=True)

    print("Closing open constituent HDULists.")

    for open_HDUlist in open_hdulists:
        open_HDUlist.close()


# ACTIVE CODE
time_init = time.time()
compile_files(input_directory, output_filename)
final_time = time.time() - time_init

print("Finished. Time elapsed:", int(final_time), "seconds.")
