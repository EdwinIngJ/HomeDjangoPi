# HomeDjangoPi
A home webserver with numerous functionalities powered by Django.

**`Documentation`** |
------------------- |

## Install
```
$ git clone https://github.com/EdwinIngJ/HomeDjangoPi.git
```

#### Setting up Environment in Program Directory
```bash
$ cd HomeDjangoPi
$ pip install -r requirements.txt
```
*Note that this project is only compatible with python3

#### Running For the First Time
Setup IP address in the settings.py within the djangopi/ directory and set DEBUG to False
```bash
$ cd HomeDjangoPi
$ sudo python manage.py migrate
$ sudo python manage.py makemigrations
$ sudo python manage.py runserver
```
Additionally, the Homeinfo app won't work unless there is one entry of ToggleWatering within the database. 
To create an entry, first create a superuser and then manually add a new entry with the admin panel. Login as a superuser to access the Homeinfo app.

# Raspberry Pi Setup
This section explains how to setup a Raspberry Pi, specifically its OS and system settings. 

For those interested in headless (without a monitor) Raspberry Pi setup, the information found [here](https://www.raspberrypi.org/documentation/configuration/wireless/headless.md) may be useful.

## Setup
This section addresses how to use [RaspbianOS](https://www.raspberrypi.org/downloads/raspberry-pi-os/) to setup your Raspberry Pi.

### Requirements
- A computer with
  - microSD card comptability
  - Imaging software (e.g., [Balena Etcher](https://www.balena.io/etcher/))
- microSD card
- Monitor
- Keyboard
- Mouse

### Deploying Preconfigured OS Image
1. Download the [RaspbianOS](https://www.raspberrypi.org/downloads/raspberry-pi-os/) onto your computer.
2. Flash the image onto the microSD card using your imaging software. It's suggested you "validate" your image if your software provides such an option.

### Booting up Raspberry Pi
1. Connect your monitor, keyboard, and mouse to the Raspberry Pi.
2. Insert the microSD card into the Raspberry Pi.
3. Apply power to the Raspberry Pi.

### Changing Username/Password
1. Follow these [instructions](https://www.maketecheasier.com/change-raspberry-pi-password/) to create a new username and password.
2. Make sure the new user is in the same groups as `pi`.
3. It is recommended you disable the default `pi` account in order to secure your Raspberry Pi.

### Connect to WiFi
1. Follow these [instructions](https://www.raspberrypi.org/documentation/configuration/wireless/desktop.md) to connect your Raspberry Pi to your wireless network of choice. Be sure it is one you trust.

### Update Wireless Settings
1. Follow these [instructions](https://pimylifeup.com/raspberry-pi-static-ip-address/) to assign a static IP to your Raspberry Pi. We have prepopulated the `dhcpcd.conf` file with a commented out template of the static IP wireless configuration. You can either update this template and uncomment it or write your own according to the linked to instructions.
   
   Be sure to assign **unique** `<STATIC_IP>` amongst all the devices on your wireless network including other Raspberry Pis that you set up with static IPs.
   ```
   # piPACT wireless static IP configuration template
   interface wlan0
   static ip_address=<STATIC_IP>/24
   static routers=<ROUTER_IP>
   static domain_name_server=<DNS_IP>
   ```
2. If you didn't do so in the previous step, reboot your Pi for the wireless setting to take effect.

### Testing Wireless Access
1. From a computer with SSH capability and using the static IP you assigned previously, perform step 4 of these [instructions](https://www.raspberrypi.org/documentation/remote-access/ssh/).
2. If you have properly configured your Raspberry Pi for SSH via a static IP then you should be able to execute commands on the Raspberry Pi remotely.
