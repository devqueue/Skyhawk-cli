# SKYHAWK
Skyhawk is a CLI application that uses face recognition to add attendance of registered users to a csv file.

### Motivation
My mum being a teacher at my school I noticed she had to wait in a queue in the morning to use her fingerprint to mark attendance. Which made me think the school must appoint a clerk who would look at people entering the building and mark their attendance and so skyhawk was born to replace the clerk I envisioned. Well AI is definitely going to take away jobs

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://github.com/devqueue/Skyhawk-cli)

#### Video Demo: https://youtu.be/1gWSH6qF8_s

### Installing the App:

#### 1. Using the repo:
   Follow the given steps to test the code:
    1. `git clone https://github.com/devqueue/Skyhawk-cli.git`
    2. `cd Skyhawk-cli`
    3. `pip install -r requirements.txt`
    4. `pip install -e . `

#### 2. Using pip:

   `pip install skyhawk`

### Testing the code:
You can initialize and register users and capture their faces.
Make sure to  hold the camera in front of your face in a good lighting condition.
1. `skyhawk init`
2. `skyhwak capture black` or `skyhawk capture color`
you will be prompted to enter your name and the number of images. I recommend 20-30 images both grey scale and color.
Once you have all the users registered you ca train the recognizer model.
3. `skyhawk train`
Now run the application.
4. `skyhawk run`
Now place a camera in at the entrance of the office or classroom
and let the registered folks walk past it. You can now view their attendance using the following command.
5. `skyhawk view attandance`

### Face Detection and Face Recognition:
The tool uses OpenCV at its core for recognition.
Human beings perform face recognition automatically every day and practically with no effort.
Although it sounds like a very simple task for us, it has proven to be a complex task for a computer,
as it has many variables that can impair the accuracy of the methods. For example, illumination variation,
low resolution, occlusion, amongst others.

Note that face recognition is different of face detection:

-   Face Detection: it has the objective of finding the faces (location and size) in an image and
    probably extract them to be used by the face recognition algorithm.

-   Face Recognition: with the facial images already extracted, cropped, resized and usually converted to grayscale,
    the face recognition algorithm is responsible for finding characteristics which best describe the image


The face recognition systems can operate basically in two modes:

-   Verification or authentication of a facial image: it basically compares the input facial image with the facial image related to the user
    which is requiring the authentication. It is basically a 1x1 comparison.

-   Identification or facial recognition: it basically compares the input facial image with all facial images from a dataset
    with the aim to find the user that matches that face. It is basically a 1xN comparison.

For our purposes we have used a LBPH classifier for recognition:
**Local Binary Pattern Histogram (LBP)** is a simple yet very efficient texture operator which labels the p
ixels of an image by thresholding the neighborhood of each pixel and considers the result as a binary number.


### How does it work?
Now that we know a little more about face recognition and the LBPH, let’s go further and
see the steps of the algorithm:
1.  Parameters: the LBPH uses 4 parameters:
-   Radius: the radius is used to build the circular local binary pattern and represents the radius around the central pixel. It is usually set to 1

-   Neighbors: the number of sample points to build the circular local binary pattern. Keep in mind: the more sample points you include, the higher the computational cost. It is usually set to 8.

-   Grid X: the number of cells in the horizontal direction. The more cells, the finer the grid, the higher the dimensionality of the resulting feature vector. It is usually set to 8.

-   Grid Y: the number of cells in the vertical direction. The more cells, the finer the grid, the higher the dimensionality of the resulting feature vector. It is usually set to 8.


2.  Training the Algorithm: First, we need to train the algorithm. To do so, we need to use a dataset with the facial images of the people we want to recognize. We need to also set an ID (it may be a number or the name of the person) for each image, so the algorithm will use this information to recognize an input image and give you an output. Images of the same person must have the same ID. With the training set already constructed, let’s see the LBPH computational steps.


3.  Applying the LBP operation: The first computational step of the LBPH is to create an intermediate image that describes the original image in a better way, by highlighting the facial characteristics. To do so, the algorithm uses a concept of a sliding window, based on the parameters radius and neighbors.

The image below shows this procedure:

![Image for post](https://lh5.googleusercontent.com/_5h5KasIU_Z_trkvt5lhCOzF3EhQp9YbVmAFHVPGWFKa777kB2GuRl6XsX_QQ9E-j5sPHuKfH-cjIcT1sJFlS8XxXoQI1puC8MKC0jf21801nxuuapxOI04khhWvPoHZO-OPZLxj)



Based on the image above, let’s break it into several small steps:

-   Suppose we have a facial image in grayscale.

-   We can get part of this image as a window of 3x3 pixels.

-   It can also be represented as a 3x3 matrix containing the intensity of each pixel (0~255).

-   Then, we need to take the central value of the matrix to be used as the threshold.

-   This value will be used to define the new values from the 8 neighbors.

-   For each neighbor of the central value (threshold), we set a new binary value. We set 1 for values equal or higher than the threshold and 0 for values lower than the threshold.

-   Now, the matrix will contain only binary values (ignoring the central value). We need to concatenate each binary value from each position from the matrix line by line into a new binary value (e.g. 10001101). Note: some authors use other approaches to concatenate the binary values (e.g. clockwise direction), but the final result will be the same.

-   Then, we convert this binary value to a decimal value and set it to the central value of the matrix, which is actually a pixel from the original image.

-   At the end of this procedure (LBP procedure), we have a new image which represents better the characteristics of the original image.

![Image for post](https://lh6.googleusercontent.com/Ac64WUwoHlTajGQbKi5ulHFcDN44w82UxlmtTW5Pwn2CrPKYbcjp3SQM1VhRAsJXgfZZwpbxRTeXXqsIFlj28v7W7XpUZFN8mnivVRYzqE2UmW8c1hgTOjliMb_v0hw2j2jjxw9a)

Note: The LBP procedure was expanded to use a different number of radius and neighbors, it is called Circular LBP.

4. Extracting the Histograms: Now, using the image generated in the last step, we can use the Grid X and Grid Y parameters to divide the image into multiple grids, as can be seen in the following image:

![Image for post](https://lh4.googleusercontent.com/0FbvfZN8SUtlK4-wGhH1OL8h_La94w4w58BBo_4MxTD3QMtLxdMz6AFVZoo26szzqYOxkHMwki6zjxeMupnMAmeIRef7JtKZTJtBr2-BBUEU2sV57hpp6cBLUzYcf2orQRbE2wPY)

Based on the image above, we can extract the histogram of each region as follows:

-   As we have an image in grayscale, each histogram (from each grid) will contain only 256 positions (0~255) representing the occurrences of each pixel intensity.

-   Then, we need to concatenate each histogram to create a new and bigger histogram. Supposing we have 8x8 grids, we will have 8x8x256=16.384 positions in the final histogram. The final histogram represents the characteristics of the original image.

5. Performing the face recognition: In this step, the algorithm is already trained. Each histogram created is used to represent each image from the training dataset. So, given an input image, we perform the steps again for this new image and create a histogram which represents the image.

-   So to find the image that matches the input image we just need to compare two histograms and return the image with the closest histogram.

-   We can use various approaches to compare the histograms (calculate the distance between two histograms), for example: euclidean distance, chi-square, absolute value, etc. In this example, we can use the known Euclidean distance based on the following formula:

![Image for post](https://lh5.googleusercontent.com/e_q_2eCX8-VDzSpdCSpXCB8qxcGpHT7gQtbvVyRXJ_sKG3oD4PUjk6tBnnW3cZ6-BXzbzgk4TRoOm8X1jKtDltdb3QDw5WfOE6605y-5oRkWpFSTpcjOcU9hoGOvTwdtG-A3iQjy)

-   So the algorithm output is the ID from the image with the closest histogram. The algorithm should also return the calculated distance, which can be used as a ‘confidence’ measurement. Note: don’t be fooled about the ‘confidence’ name, as lower confidences are better because it means the distance between the two histograms is closer.

-   We can then use a threshold and the ‘confidence’ to automatically estimate if the algorithm has correctly recognized the image. We can assume that the algorithm has successfully recognized if the confidence is lower than the threshold defined.



### Conclusions

1. LBPH is one of the easiest face recognition algorithms.
2. It can represent local features in the images.
3. It is possible to get great results (mainly in a controlled environment).
4. It is robust against monotonic gray scale transformations.
5. It is provided by the OpenCV library (Open Source Computer Vision Library).


### Further improvements

As of writing this report there are a few training data bugs that need to be fixed.
I am currently accepting open contributions to the [repo](https://github.com/devqueue/Skyhawk-cli)


Secondly the process of training and obtaining euclidean distances is a computationally expensive process.
In order to run this application on any single board computer with a python interpreter is not very feasible
as the application requires a lot of computational resources.


Thirdly in order to recognize a face with more than decent accuracy the model requires lots of images of the same face.
This might consume more memory and hence make the process slower if adequate processes aren’t given.
My plan for the future of this project is to train a deep neural network on millions of face images and train it to recognize
differences between faces and not faces themselves.
This will solve both the above mentioned issues.


### Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

### License
[MLP 2.0](https://www.mozilla.org/en-US/MPL/2.0/)
