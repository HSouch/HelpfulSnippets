# HelpfulSnippets
Small tools to make working with astronomical data a little bit easier.


## Simple Image Tester
Sometimes, running batch downloads of FITS files leads to some strange or corrupted files. Run this tool on a directory containing fits images (extension .fits or .fit) to see if any are corrupted.

`python simple_image_tester.py top_level_dir`

It will print out the filenames of any files that won't open, and will tell you how many need to be dealt with (if any).
