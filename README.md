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

Start by forking this repo, be sure you fork the entire repo and not just main.

<image src="screenshot02.png">

<br>

Next clone the 'clone' branch, all code should be contained here as this is what will be submitted.

```
git clone --branch clone git@github.com:YOUR_GIT_USER/Interview-Project.git
```

If you don't have a ssh key setup with git hub on your machine use this command.

```
git clone --branch clone https://github.com/YOUR_GIT_USER/Interview-Project.git
```

<br>

<p align="center" style="font-size: 24px;"><strong>Please develop your code in a python virtual environment to help maintain consistency across all projects.</strong><br></p>
Assuming Python is installed on your PC, the following command should create a Python virtual environment in your current directory.

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

Using python, create a program that can take two images as an input then creates a disparity map. <br>
We recommend using one of the [Middlebury 2014 Stereo Datasets](https://vision.middlebury.edu/stereo/data/scenes2014/) for the images and camera calibration data.

<br>

## Task 2 

After generating the disparity map from the two images, convert it into a 3D point cloud. <br>
Once you're finished with the point cloud code, create a bash script that automatically runs your Python code. Executing this script should:
  1. Generate a disparity map from two images
  2. Use that disparity map to create a point cloud
  3. Save the resulting point cloud file

<a href="https://asciinema.org/a/Bsi8wNmPKFnsUkxOD90YPHVdv" target="_blank"><img src="https://asciinema.org/a/Bsi8wNmPKFnsUkxOD90YPHVdv.svg" /></a>

<br>

## Submition ✅

Once Task 2 is completed, read and complete the README.md included in the clone repo. <br>
Finally, you need to submit your work as a pull request to this repo.

<br>

Make sure your in the clone branch, then stage all your updates. (if you haven't already)
```
git checkout clone
```
```
git add .
```
Now commit then push your work back to git hub.
```
git commit -m "YOUR NAME"
```
```
git push origin clone
```

<br>

Now that your project has been pushed to clone branch click on the `Compare & pull request` button.

<image src="screenshot04.png">

The last thing you need to do is create a pull request to the clone branch. <br>

**YOUR PULL REQUEST MUST HAVE THE FOLLOWING**

  1. `base repository:` is set to **Ph-Dos/Interview-Project**
  2. `base:` is set to **clone**
  3. `head repository:` is set to **YOUR FORK** of the repo
  4. `compare:` is set to **clone**
  5. **title** is set to your name

<image src="screenshot05.png">

Watch this [Video](https://www.youtube.com/watch?v=jRLGobWwA3Y) if you are confused.
