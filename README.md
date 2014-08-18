# AustinDev.me
This is my personal portfolio website.  I've taken this opportunity to play with a lot of new technology that I've been wanting to explore.  Feel free to look at the code!  It should work perfectly on any modern device, sans the Web Dev page (howtotable.png).  Please let me know if you have any issues with it.  Thanks!

## Setup Python/Pip - Linux
```bash
todo apt-get stuff  
```

## Setup Python/Pip - Mac
```bash
brew install python  
brew install python3  
```

## Installation
```bash
cd /path/to/web/root  
git clone git@github.com:JediSange/austindev.git austindev.me  
virtualenv austindev.me  
cd austindev.me  
source bin/activate  
pip install -r config/pip.requirements  
cd website  
python manage.py runserver  
```

## Production - Linux
```bash
sudo apt-get install nginx  
sudo cp /path/to/web/root/austindev.me/config/nginx.develop.conf /etc/nginx/sites-enabled/austindev.me  
sudo service nginx restart  
```

## Built With
- [Breakpoint](http://breakpoint-sass.com/)
- [Bundler](http://bundler.io/)
- [Compass](http://compass-style.org/)
- [Django](https://www.djangoproject.com/)
- [Django Markdown Deux](https://github.com/trentm/django-markdown-deux)
- [HTML5 Boilerplate](http://html5boilerplate.com/) via [Initializr](http://www.initializr.com/)
- [SASS](http://sass-lang.com/)
- [South](http://south.aeracode.org/)

## Runs on
- [Nginx](http://nginx.com/)
- [Gunicorn](http://gunicorn.org/)

## To-Do List
- Google Analytics
- Settings for Gunicorn
- Prod vs Dev
- Change all tabs to spaces #converted
- Robots.txt?
- Make install text - Finalize deploy steps
- New headshot?
- Fix table on webdev page (stop being lazy!)