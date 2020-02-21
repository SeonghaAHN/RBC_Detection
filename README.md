## Utility code for YOLOv3 Keras implementation of qqwweee
This repository is inspired by YOLO keras implementation of qqwweee  
[Keras implementation original repository](https://github.com/qqwweee/keras-yolo3)  
For details, please refer the original repo linked above.

## convert.py  
- convert .xml format label file into the format used in original repository.
  ### How to use
  save `convert.py` in dataset directory and run it.  
  .txt format label will be generated in the same directory. 
  
## yolo_video.py  
- predict on all test image by using command `python yolo_video.py --image`  
- The final weight file must be renamed as `yolo.h5` and saved in `model_data` directory before run  

## train_via_notebook.ipynb  
- Notebook for training

## generate_gt_image.ipynb  
- Generate GroundTruth images
