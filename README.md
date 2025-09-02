<p align="center">
  <h2 align="center">Data Team Take Home</h2>
</p>
<p>
Configurations, you made it to the secound round of the interview process. For this project you will be creating a disparity map then generating a point cloud from the disparity map.
<br>
<br>
<br>
</p>

## Setup ⚠️

Start by cloning the 'clone' branch. All code should be contained here, as this is what will be submitted.

```
git  clone --branch clone https://github.com/Ph-Dos/Interview-Project.git
```

<br>

<p>
<strong>Please develop your code in a python virtual environment to help maintain consistency across all projects.</strong> <br>
Assuming Python is installed on your PC, the following command should create a Python virtual environment in your current directory.
</p>

```
python3 -m venv env
```

To start the Python virtual environment run the following command in the same directory.

```
source ./env/bin/activate
```

Please keep track of the packages you install in the virtual environment so you can include them in your submission.

```
pip install ...
```

<br>

## Task 1

Create a program that can take two images as an input, then creates a disparity map. <br>
We recommend using one of the [Middlebury 2014 Stereo Datasets](https://vision.middlebury.edu/stereo/data/scenes2014/) for the images.

<br>

## Task 2 

After generating the disparity map from the two images, convert it into a 3D point cloud.
When you are done make a bash script that creates the disparity map from the two images then generates the point cloud from the disparity map.

<br>

## Submition ✅
