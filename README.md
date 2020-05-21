# Soundcloud (Headless)
Automatically play songs from soundcloud.com using Python and selenium without using API.
## Instructions for Windows (For beginners)
- **Install Git:** Visit https://gitforwindows.org/. Download and install the latest version of git.
- **Install Python and pip:**  Visit - https://www.python.org/downloads/ or watch my video here on how to install Python on your machine - https://youtu.be/0TKybIFnNaA
- **Clone the project** Clone this project from github to your local machine by executing the git command `git clone https://github.com/anoop1409/soundcloud.git`. This will clone the project to your current directory.
- **Download chromedriver:** Visit this link and download the latest chromedriver for your os. Link: https://chromedriver.chromium.org/downloads
- **Copy chromedriver to correct location:** Extract the zip file and copy the chromedriver file to your project folder's `/bin` directory
- **Update Google Chrome:** Make sure your google chrome is up to date and is compatible with the downloaded chromedriver.
- **Setup and activate virtual environment:** You can watch this simple tutorial on how to setup and activate virtual environment here - https://youtu.be/RJ0fWQrX0fY
- **Install requirements:** Watch the tutorial here - https://youtu.be/oyPXugL9dPg to install the requirements for this project
- **Execute the project:** Execute the command `python main.py` and it should start playing the latest songs from soundcloud within a minute.
- **Turn off the songs:** Press `Ctrl+C` in the command prompt and it should terminate the background chrome which is playing the songs.

## Instructions for Linux and Raspberry Pi (For beginners)
#### Setup Python 3.6 on Raspberry Pi
On a regular linux machine, you should be already having Python3.6 or above installed.  
For installing it on a Raspberry Pi, you can execute the steps mentioned in this very nice medium article: https://medium.com/@isma3il/install-python-3-6-or-3-7-and-pip-on-raspberry-pi-85e657aadb1e

#### Setup Virtual env
1. `sudo nano ~/.profile`  
2. Add the following code towards the end of the file  
`VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3.6`
3. Save and exit Nano `Ctrl+X` followed by `Y`
4. `source ~/.profile`
5. `sudo pip3 install virtualenvwrapper`
6. `sudo nano ~/.profile`
7. Add the following code towards the end of the file  
`export WORKON_HOME=$HOME/.virtualenvs`  
`source /usr/local/bin/virtualenvwrapper.sh`
8. Save and exit Nano `Ctrl+X` followed by `Y`
9. `sudo pip install virtualenv`
10. `virtualenv env` - This creates the virtual environment with Python and pip.


#### Install chromedriver
- `sudo apt-get install chromium-chromedriver`
- Then use the command - `dpkg -L chromium-chromedriver` to search for the path of the installed chromedriver. Once you find the path of `chromedriver`, execute the following command to move the file to the bin directory of your project.
- `mv <path of chromedriver> <path of bin folder of your project>`  
For me, the paths are as: `mv /usr/bin/chromedriver /home/pi/soundcloud/bin`

#### Play the top 50 trending songs on soundcloud
Activate the virtual environment  
Create the virtual environment first (See the steps above). Then execute the following commands:  
- `cd env`  
- `source bin/activate` - This activates the virtual environment.  
- `cd ..`
- `python main.py` - This should start your headless chrome and should log the execution steps to the console and finally play the songs.


#### Turn off the songs / Kill the headless browser
`pkill chromium`
#### Deactivate the virtual env
Use the command - `deactivate`