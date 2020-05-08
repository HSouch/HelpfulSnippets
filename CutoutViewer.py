"""
Compiles all FITS files in an input directory into one.
"""

import time
import argparse
from astropy.io import fits
from matplotlib import pyplot as plt

from numpy import sqrt, ceil

input_filename = ""
output_filename = ""
colormap = "inferno"
output_dpi = 100


def process_arguments():
    """ Gather all user arguments, and set global variables if necessary. """
    global input_filename
    global output_filename
    global colormap
    global output_dpipy

    parser = argparse.ArgumentParser(description="Simple tool to generate visualization based on a FITS file " +
                                                 "of cutouts. Requires input file and output filename.",
                                     epilog="Please email hsouchereau@outlook.com for help or bug reports.")

    parser.add_argument("input_filename", type=str,
                        help="The input filename to generate visualized cutouts for.")
    parser.add_argument("output_filename", type=str,
                        help="The output filename to save visualized cutouts as.")
    parser.add_argument("--cmap", type=str,
                        help="MatPlotLib friendly colormap. Default is " + colormap)
    parser.add_argument("--dpi", type=int,
                        help="DPI for saving figure. Default is 100")

    # Get all input arguments
    args = parser.parse_args()

    input_filename = args.input_filename
    output_filename = args.output_filename

    if args.cmap is not None:
        colormap = args.cmap
    if args.dpi is not None:
        output_dpi = args.dpi

    return args


def view_cutouts(filename, output="", cmap=colormap, dpi=output_dpi):
    """ Generate cutouts plot for input filename"""
    local_filename = filename.split("/")[len(filename.split("/")) - 1].split(".")[0]

    HDUList = fits.open(filename)

    width = int(ceil(sqrt(len(HDUList))))

    print(len(HDUList), "cutouts to visualize. Generating", str(width) + "x" + str(width), "figure.")

    fig, ax = plt.subplots(width, width)

    fig.set_figheight(width)
    fig.set_figwidth(width)

    index = 0
    for x in range(0, width):
        for y in range(0, width):
            ax[x][y].set_xticks([])
            ax[x][y].set_yticks([])
            try:
                data = HDUList[index].data
                head = HDUList[index].header
                ax[x][y].imshow(data, cmap=cmap)

                ax[x][y].text(2, 10, str(int(head["SNR"])), color="white")
                ax[x][y].text(2, 35, str(head["P_MASKED"])[:5], color="white")

            except:
                pass

            index += 1

    plt.tight_layout()
    plt.subplots_adjust(hspace=0, wspace=0)

    print("Saving figure to " + output)
    plt.savefig(output, dpi=dpi)

    HDUList.close()


time_init = time.time()
arguments = process_arguments()
view_cutouts(input_filename, output_filename)

print("Finished. Time Elapsed:", str(time.time() - time_init)[:8], "seconds.")
