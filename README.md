# Setting up RPi Zero W for touchscreen device development with a HyperPixel screen

## Prerequisites:

- [Etcher](https://etcher.io/)
- [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)
- [Python 3 for Windows](https://www.python.org/downloads/)

## Step by step:

### Set up a headless RPi Zero W

Throughout this process, Windows may occasionally pop up warning dialogs saying you have to format the disk before you can use it - *always* ignore these (click Cancel or close)

- Download [Raspbian Jessie (or later) *Lite* image](https://downloads.raspberrypi.org/raspbian_lite_latest) 
- Mount the RPi SD card in your PC
- Open Etcher, select the downloaded Raspbian image and click Flash
- Once the card is flashed and validated, Etcher will automatically eject it
- Remove and re-insert the card
- Open the `boot` partition of the SD card in Explorer
- Create an empty text file called `ssh` (no extension) at the root of the SD card partition
- Create another empty text file called `wpa_supplicant.conf` at the root of the SD card partition
- Open `wpa_supplicant.conf`, add the following (substituting your own Wifi SSID and password) and save the file:

      network={
          ssid="MyWiFiNetwork"
          psk="password123"
      }

- Eject the SD card, remove it and reinsert into the RPi
- Power up the RPi and wait for it to boot (LED will flicker until it is up and running)
- Find out which IP address your network has assigned to the RPi - easiest way is to look at your router's connection status page, but you can use AngryIP or Fing on a mobile device
- Open PuTTY and enter `pi@192.168.0.123` as the hostname, replacing the IP address with that or your RPi
- Make sure the connection type is set to SSH, then click **Open**
- You should see a password prompt: enter `raspberry` (the default RPi password)
- That's it: you're now logged in to your RPi

### Update the RPi firmware and system packages

- Run `sudo apt-get install rpi-update`
- Run `sudo rpi-update` to update the firmware, then `sudo reboot`
- Run `sudo apt-get update` and `sudo apt-get upgrade` to upgrade all packages to the latest versions (`dist-upgrade`?)
- Run `sudo reboot` again
- Run `sudo raspi-config`
- Select **7 - Advanced Options**, then **A1 - Expand Filesystem**
- Run `sudo reboot` again

### Install the HyperPixel touch screen

- If the HyperPixel screen isn't already attached to the RPi, shut down the system with `sudo shutdown -h now` and remove the power, then attach the screen and power the RPi back up
- Run `curl https://get.pimoroni.com/hyperpixel | bash` to install the HyperPixel drivers
- When the installer completes, it will ask you to reboot: accept
- After a few seconds you should see the boot sequence displayed on the HyperPixel

### Install the experimental HyperPixel multitouch driver?

<!-- TODO: Is this actually required, or does the above driver do everything I need? -->

- Clone https://github.com/pimoroni/python-multitouch
- Run `cd python-multitouch/library`
- Edit `ft5406.py`: change `TOUCHSCREEN_EVDEV_NAME` value to `Touchscreen`
- Run `sudo python3 setup.py install`
- Copy up `touch.py` and run to capture screen events

### Install Python and Kivy on Windows

- Download Python, install (TODO: screenshot options)
- Run `pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew`
- Run `pip install kivy.deps.gstreamer`
- Run `pip install kivy`
- Optionally run `pip install kivy_examples` to get the examples

### Install Kivy on the RPi

#### Install dependencies

- Run `sudo apt-get install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev pkg-config libgl1-mesa-dev libgles2-mesa-dev libgstreamer1.0-dev git-core gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-omx gstreamer1.0-alsa libmtdev-dev xclip`

#### Python 2.X

- Run `sudo apt-get install python-pip python-dev python-setuptools`
- Run `sudo pip install --ignore-installed cython` (this takes AGES)
- Run `sudo pip install git+https://github.com/kivy/kivy.git@master` (also takes AGES)`

#### Python 3.X

- Run `sudo apt-get install python3`
- Run `sudo apt-get install python3-pip python3-dev python3-setuptools`
- Run `sudo pip3 install --ignore-installed cython` (this takes AGES)
- Run `sudo pip3 install git+https://github.com/kivy/kivy.git@master` (also takes AGES)

#### Configure Kivy inputs

- Open `~/.kivy/config.ini`
- Find the `[input]` section
- Replace the existing contents with:

      mouse = mouse
      mtdev_%(name)s = probesysfs,provider=mtdev
      hid_%(name)s = probesysfs,provider=hidinput

## References:

http://angryip.org/  
https://learn.pimoroni.com/tutorial/sandyj/setting-up-a-headless-pi  
https://play.google.com/store/apps/details?id=com.overlook.android.fing&hl=en_GB&rdid=com.overlook.android.fing  
https://kivy.org/docs/installation/installation-rpi.html  
https://kivy.org/docs/installation/installation-windows.html  