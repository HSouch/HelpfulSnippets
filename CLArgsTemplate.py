"""
Compiles all FITS files in an input directory into one.
"""

import argparse


example_value = 10.
example_flag = False


def process_arguments():
    """ Gather all user arguments, and set global variables if necessary. """
    global example_value

    parser = argparse.ArgumentParser(description="This is the description of the software.",
                                     epilog="Include a final message (for -h) here.")

    parser.add_argument("-t", "--test_value", type=float,
                        help="This is a test value for an input float")
    parser.add_argument("-f", "--test_flag", action="store_true",
                        help="This is an example flag that can be set to true")

    # Get all input arguments
    args = parser.parse_args()

    if args.test_value is not None:
        example_value = args.test_value
    # You could also probably do example_flag = args.test_flag, but I personally prefer this consistent approach
    if args.test_flag:
        example_flag = True

    return args


arguments = process_arguments()
