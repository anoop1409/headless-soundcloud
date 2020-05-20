# soundcloud
Automatically play songs from soundcloud.com using Python and selenium

##Setup Python 3.7 on Raspberry Pi
- `sudo apt-get update` (Update your Pi)
- `cd /tmp` (Go to the tmp directory)
- `wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz`
- `sudo tar zxf Python-3.7.0.tgz`
- `cd Python-3.7.0`
- `sudo ./configure`
- `sudo make -j 4`
- `sudo make altinstall`

#### Make Python3.7 default version
- `nano ~/.bashrc`

Add these lines to the file:

- `which python3.7`  
- `/usr/local/bin/python3.7`  
- `alias python='/usr/local/bin/python3.7'`

Execute command
- `source ~/.bashrc`