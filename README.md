This repo is a fork of the original YOLOP project created for the final project of ROB 535 - Self Driving Cars: Perception and Control at the University of Michigan during the Fall 2024 semester. This project was worked on by Andre Mixan, Adithya Ramakrishnan, and Tyler Smithline. In this project, we evaluate the YOLOP network on the following datasets: Cityscapes, CULane, and Curvelanes. We evaluate the tasks of the network (Object Detection, Drivable Area Segmentation, and Lane Line Segmentation) separately. 

Our changes to the original repo lie in the files: helpers.ipynb, Convert_CULane_Data.py, and lib/config/default.py. 

To reproduce the results of this repo, it will require downloading parts or all of the Cityscapes, CULane, and Curvelanes datasets and running the data pre-processing functions in helpers.ipynb and Convert_CULane_Data.py. The file helpers.ipynb contains functions to process the Cityscapes dataset for driviable area segmentation inference and the CurveLanes dataset for lane line segmentation. Convert_CULane_Data.py contains functions to prepare the CULane dataset for lane line segmentation. Once the data has been processed, it needs to be placed in the same file structure as the original BDD dataset with a folder for each set of images or labels, which is referenced in lib/config/default.py.

You can find the datasets we used here: 
Cityscapes: https://www.cityscapes-dataset.com/
CurveLanes: https://github.com/SoulmateB/CurveLanes
CULane: https://xingangpan.github.io/projects/CULane.html
