# HomeDjangoPi
A home webserver powered by Django with numerous functionalities.

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
*note that this project is only compatible with python3

#### Running For the First Time
Setup IP address in the settings.py within the djangopi/ directory and set DEBUG to False
```bash
$ cd HomeDjangoPi
$ sudo python manage.py migrate
$ sudo python manage.py makemigrations
$ sudo python manage.py runserver
```
Additionally the Homeinfo app won't work unless there is an entry of ToggleWatering within the db. 
To create an entry, create a superuser and manually add it with the admin panel.
