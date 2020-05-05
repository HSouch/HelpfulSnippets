"""
Compiles all FITS files in an input directory into one.
"""

import argparse

required_input = ""
example_value = 10.
example_flag = False


def process_arguments():
    """ Gather all user arguments, and set global variables if necessary. """
    global required_input
    global example_value
    global example_flag

    parser = argparse.ArgumentParser(description="This is the description of the software.",
                                     epilog="Include a final message (for -h) here.")

    parser.add_argument("required_value", type=str,
                        help="This is a required value. The code will not run if this is not included. The remaining" +
                        " flags are optional flags.")

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

    required_input = args.required_value

    return args


arguments = process_arguments()

print(required_input, example_value, example_flag)