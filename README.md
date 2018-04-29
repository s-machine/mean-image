# mean-image

[Link to Live Site](https://s-machine.github.io/mean-image/)
### Introduction
A “mean” image is a generated image based on the average value for corresponsding pixels in several images.  

Our goal is to analyze mean images within topics that illustrate modern culture and politics. Topics include beauty (magazine covers), politics (magazine covers), entertainment (YouTube thumbnails), and more.  

Through the process of finding a mean image, the generality and universality of trends and moments in time becomes evident. Work inspired by the art of [Jason Salavon](www.salavon.com).

![Time](./images/small_time.png =100x) 
![Womens Health](./images/small_womens.jpg)

### Code
Mean images are rendered using a Python scripts in the `/data` folder of this repo.
Website is rendered using basic HTML, CSS, JavaScript, and d3.js. Mean image processing does not happen live, rather static mean images were pre-computed and can be found in the `/images` folder

### Data
Raw data is unstructured images saved to this [Google Drive](https://drive.google.com/open?id=1_I0gd4cSSTXhy7uLtpLDc88qD6Tr0SacrVnuTAztWE4). Cleaned and processed images are in the `/images` folder in this repo. 

### Dependencies
- jQuery
- d3.js 
- Python
	- re
	- requests
	- urllib.request
	- urllib.error
	- os
	- path
	- numpy
	- PIL


### Screencast
[Link](www.youtube.com)
