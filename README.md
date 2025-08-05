# Background-Remover
This is a python scrip to remove background from images. It can keep track of images that has been processed, process images from folder, output files with same file name as original. It is based on python library rembg.

    """
    This file contains functions for data processing, originally developed by @github_username.
    See: [https://github.com/danielgatis]
    """
 
## Requirements

```
python: >=3.10, <3.14
rembg image remove library
```
rembg can be installed and guide is provided on the following link:

```
https://github.com/danielgatis/rembg
```

## Use Case

1.) Add path to folder containing images to be processed 'dataset_folder' variable.  
2.) Select 'sample_size'. This variable takes number of images to process. from all the images in a folder. I have used random sampling so that I can process certain number randomly selected files for immediate use. This way I can save storage space.  
3.) Select model for processing images. Different models can have different quality output. Please refer to list of all available models below.  

## Model

All models are downloaded and saved in the user home folder in the .u2net directory.

The available models are:

    u2net (download, source): A pre-trained model for general use cases.
    u2netp (download, source): A lightweight version of u2net model.
    u2net_human_seg (download, source): A pre-trained model for human segmentation.
    u2net_cloth_seg (download, source): A pre-trained model for Cloths Parsing from human portrait. Here clothes are parsed into 3 category: Upper body, Lower body and Full body.
    silueta (download, source): Same as u2net but the size is reduced to 43Mb.
    isnet-general-use (download, source): A new pre-trained model for general use cases.
    isnet-anime (download, source): A high-accuracy segmentation for anime character.
    sam (download encoder, download decoder, source): A pre-trained model for any use cases.
    birefnet-general (download, source): A pre-trained model for general use cases.
    birefnet-general-lite (download, source): A light pre-trained model for general use cases.
    birefnet-portrait (download, source): A pre-trained model for human portraits.
    birefnet-dis (download, source): A pre-trained model for dichotomous image segmentation (DIS).
    birefnet-hrsod (download, source): A pre-trained model for high-resolution salient object detection (HRSOD).
    birefnet-cod (download, source): A pre-trained model for concealed object detection (COD).
    birefnet-massive (download, source): A pre-trained model with massive dataset.
    ben2-base (download, source): Introduces a novel approach to foreground segmentation through its innovative Confidence Guided Matting (CGM) pipeline.
