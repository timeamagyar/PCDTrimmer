## PCD Trimmer

Small python library to modify .pcd annotation files produces by the Hitachi 3D semantic segmentation tool available under: https://github.com/Hitachi-Automotive-And-Industry-Lab/semantic-segmentation-editor.
Modfied .pcd files are used in the performance evaluation of the adapted LDLS algorithm forked from: https://github.com/brian-h-wang/ldls_ros.

## Installation

Requires/tested on:

1. Ubuntu 18.4 
4. Python 2.7

Installing dependencies with pip is recommended. A requirements.txt file is included in the project folder. To install the required dependencies inside a virtual environment run:

```
python -m virtualenv <name_of_the_virtualenv>
source <name_of_the_virtualenv>/bin/activate
pip install -r requirements.txt
```


## Usage

To modify a sample .pcd file produced by the Hitachi annotation tool run: 

```
python __main__.py -pcd_path <path_to_pcd_file> -gt_path <path_to_transformed_pcd_file>
```
