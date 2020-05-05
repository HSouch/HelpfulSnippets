# HelpfulSnippets
Small tools to make working with astronomical data a little bit easier.


## Simple Image Tester
Sometimes, running batch downloads of FITS files leads to some strange or corrupted files. Run this tool on a directory containing fits images (extension .fits or .fit) to see if any are corrupted.

`python simple_image_tester.py top_level_dir`

It will print out the filenames of any files that won't open, and will tell you how many need to be dealt with (if any).


## FITS Compiler
Sometimes you want to compile a bunch of files in a directory into one big file for easier processing. This script does just that! Please note that the method requires all consistutent input FITS files to remain open until after saving the compiled file, until after when they are all closed. This might require high RAM usage forlarge files, but it runs very well on small to medium sized directories. 

`python FitsCompiler.py input_directory/ output_filename.fits`


## Coverage Getter
This script will obtain RA and DEC points of FITS images, running on a directory and finding all FITS files within nested subdirectories. For each file, it will obtain a WCS and image, and return RA and DEC points at the top left and bottom right corners of the image. 

`python coverage_getter.py top_level_dir -o output_filename.fits`

It will save as an output table (the name can be customized by the user). Each row contains the filename, and 4 points to reconstruct a coverage map.

## Command Line Args Template
This script serves as a template for getting some software running that needs to take in command line arguments from the user. It includes a few examples to get you on your way.
To test that things are working, you can run the following:

`python CLArgsTemplate.py` and
`python CLArgsTemplate.py -h`
