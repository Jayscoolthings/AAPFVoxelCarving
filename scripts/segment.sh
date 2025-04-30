#!/bin/bash

TF_DISTRIBUTED_WHITEBOARD=false

# File containing the list of plant folders to process
input="plants.txt" 
[ ! -f "$input" ] && { echo "$0 - File $input not found."; exit 1; }

while IFS= read -r folder; do
    # Concatenate the name of the plant folder and the path to the dataset
    dir="$1/$folder"
    outputDir="$2/$folder"
    # If it is indeed a folder
    if test -d "$dir"; then
        echo "Processing $dir"

        mkdir $outputDir

        python ../Segmentation/segment.py --input $dir --output $outputDir --model ../Segmentation/working_models/sorghum_segmentation_model_cnn715_2000_epochs.h5
    fi
done < "$input"
