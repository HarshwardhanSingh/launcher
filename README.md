# launcher
Launcher is a simple python script which can do wonders when it comes to save time at system bootup.
Currently it can launch sublime-text and firefox with three tabs which you can edit as per your needs.

# Requirements
  Python 2.7
  Linux Distribution
  
# How to get started
  `sudo -i`  
  `cd /etc/init`  
  `touch launcher.conf`  
  `nano launcher.conf`  
  
  Add the following to launcher.conf  
  `start on runlevel [2345]`  
  `stop on runlevel [!2345]`  

  `exec python /path/to/launcher.py`  
  
  Now reboot and test if it works
  
  `reboot`

