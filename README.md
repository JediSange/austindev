# AustinDev.me
This is my personal portfolio website.  I've taken this opportunity to play with a lot of new technology that I've been wanting to explore.  Feel free to look at the code!  It should work perfectly on any modern device, sans the Web Dev page (howtotable.png).  Please let me know if you have any issues with it.  Thanks!

## Install TODO: add apt-get installs
cd /path/to/web/root
git clone git@github.com:JediSange/austindev.git austindev.me
virtualenv austindev.me
sudo cp /path/to/web/root/austindev.me/config/nginx.develop.conf /etc/nginx/sites-enabled/austindev.me
sudo service nginx restart
cd austindev.me
screen -S austindev.me
source bin/activate
pip install -r config/pip.requirements
cd website
python manage.py runserver **TODO: change to gunicorn**

## Built With
- [Django](https://www.djangoproject.com/)
- [Django Markdown Deux](https://github.com/trentm/django-markdown-deux)
- [HTML5 Boilerplate](http://html5boilerplate.com/) via [Initializr](http://www.initializr.com/)
- [SASS](http://sass-lang.com/)

## Runs on
- [Nginx](http://nginx.com/)
- [Gunicorn](http://gunicorn.org/)

## To-Do List
- Roll out Blog
- Break up SASS files -- Variables, Layout, Helper, Queries
- Settings for Gunicorn
- Setup hidden secret_key.py
- Use Nginx to serve static files with microcaching
- Update Nginx to server certain folders from different directories IE: status
- Finalize deploy steps
- Prod vs Dev
- Change all tabs to spaces #converted
- Robots.txt
- Google Analytics?  Do I care?
- Make install text
- New headshot?
