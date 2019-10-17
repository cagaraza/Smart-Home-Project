
<p align="center">
<img width="150" height="150" src="https://raw.githubusercontent.com/cagaraza/Smart-Home-Project/master/Assets/SmartHome.png">
</p>
<font size="+2"><h1 align="center"><b>Smart-Home-Project</b></h1><font>
<h4 align="center">Anything smart home related that I can accomplish with a Raspberry Pi 3, coffee, and any of what's left of my free time.</h4>

<h4 align="center">Cheers!</h4>

## Setup
I. Installing an environment for development. 

1. Install miniconda
```bash
wget http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-armv7l.sh
md5sum Miniconda3-latest-Linux-armv7l.sh
bash Miniconda3-latest-Linux-armv7l.sh
```
2. Install python 3.6 for conda
```bash
conda install python=3.6
``` 
3. Create an environment: myenv
```bash
conda create --name myenv python=3.6
```

4. To activate the environment:
```bash
source activate myenv
```
NOTE: To automatically activate your environment everytime you open a terminal:

On terminal:
```bash
sudo vim ~/.bashrc
```

Then at the bottom of the file just apppend the line:
```bash
source activate myenv
```

II. Installing RPi.GPIO for connecting peripherals to RPi3
1. Update your Raspberry Pi
```bash
sudo apt-get update
sudo apt-get upgrade 
```

2. Install RPi.GPIO
```bash
pip install RPi.GPIO
```

3. To verify that the RPI.GPIO is working for your raspberry pi:
inside python, type in:
```python
import RPi.GPIO as GPIO
```
## TO DO
1. Verify working GPIO interface using hardware
2. Choose first sensor and actuator integrate and test. 
  Temp Sensor: OMRON Thermal Array Sensor
  Actuator: AC Infrared Controller
3. Switching relays for emergency turn off.
