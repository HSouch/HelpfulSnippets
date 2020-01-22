# HelpfulSnippets
Small tools to make working with astronomical data a little bit easier.


## Simple Image Tester
Sometimes, running batch downloads of FITS files leads to some strange or corrupted files. Run this tool on a directory containing fits images (extension .fits or .fit) to see if any are corrupted.

`python simple_image_tester.py top_level_dir`

It will print out the filenames of any files that won't open, and will tell you how many need to be dealt with (if any).


## Coverage Getter
This script will obtain RA and DEC points of FITS images, running on a directory and finding all FITS files within nested subdirectories. For each file, it will obtain a WCS and image, and return RA and DEC points at the top left and bottom right corners of the image. 

`python coverage_getter.py top_level_dir -o output_filename.fits`

It will save as an output table (the name can be customized by the user). Each row contains the filename, and 4 points to reconstruct a coverage map.
