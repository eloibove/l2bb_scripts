# l2bb_scripts
The extract_cones.py file uses *darknet* labels to extract cone subimages from the original image.
The number corresponding to each class may change between different teams, and has to be changed
in the script. 

The extract_cones_rand.py extracts the cone specified by the label (as in extract_cones.py) but
introduces random noise to the image coordinates to simulate miscalibration or synchronization issues.

Check the paths inside the scripts and change them according to your setup.
