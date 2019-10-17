<h3 align="center"><b>Smart-Home-Project</b></h3>
Anything smart home related that I can accomplish with a Raspberry Pi 3, coffee, and any of what's left of my free time.

Cheers!

# Setup
##I. Installating an environment for development. 

1. Install miniconda

wget http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-armv7l.sh
md5sum Miniconda3-latest-Linux-armv7l.sh
bash Miniconda3-latest-Linux-armv7l.sh

2. Install python 3.6 for conda
conda install python=3.6

3. Create an environment: myenv
conda create --name myenv python=3.6

4. To activate the environment:
source activate myenv

NOTE: To automatically activate your environment everytime you open a terminal:

On terminal:
sudo vim ~/.bashrc

Then at the bottom of the file just apppend the line:
source activate myenv

##II. Installing RPi.GPIO for connecting peripherals to RPi3
1. Update your Raspberry Pi
sudo apt-get update
sudo apt-get upgrade 

2. Install RPi.GPIO
pip3 install RPi.GPIO

3. To verify that the RPI.GPIO is working for your raspberry pi:
