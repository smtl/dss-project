== Decision Support System | DSS ===
This project is hosted on Google Code: http://code.google.com/p/dss-project

An online version of this information can be found on the project's wiki page: http://code.google.com/p/dss-project/w/list

Developers:
Stephen Lowry
Stephen Murphy
Adrian Kwizera

This project is developed using the following technologies:

Python 2.7 (http://python.org/)
Django 1.3 (https://www.djangoproject.com/)
SQLite3 (http://www.sqlite.org/)
Apache 2.2.20 (http://httpd.apache.org/)
 - mod_wsgi extension (http://code.google.com/p/modwsgi/)


=== Set up and Configuration ===

The project files can be retrieved by either using SVN, a version control system
or by downloading a packaged file.

== SVN Details ==

SVN or Subversion is a version control system (http://subversion.apache.org/). It can be used to retrieve the files.

The following command will install SVN/Subversion

sudo apt-get install subversion

A guide to using subversion can be found at http://svnbook.red-bean.com/

To retrieve the files from the repository run the following commands

svn checkout http://dss-project.googlecode.com/svn/trunk/dss/

== Python Details ==

Ubuntu comes with python but you still might need to install the developer packages:
sudo apt-get install python-dev

== Django Details ==

We are using Django 1.3.1. The download and instructions to install can be found here:
https://www.djangoproject.com/download/

After installing the database, make sure to set the dbb path in settings.py as an 
absolute path in order to support global installations and database permissions

python manage.py syncdb //syncs the database
python manage.py test //runs unit tests
python manage.py runserver //runs the django development server

== Apache Details ==

sudo apt-get install apache2
sudo apt-get install apache2-prefork-dev
(If you want a graphical interface to control the server, you can use https://launchpad.net/localhost-indicator)
Commands to control the apache2 server are:
sudo service apache2 start sudo service apache2 stop

== mod_wsgi Details ==

Download mod_wsgi from:
http://code.google.com/p/modwsgi/downloads/detail?name=mod_wsgi-3.3.tar.gz&can=2&q=
tar xvfz mod_wsgi-3.3.tar.gz
cd into the new mod_wsgi folder
./configure
make
Edit /etc/apache2/httpd.conf to include this line:
LoadModule wsgi_module modules/mod_wsgi.so
sudo make install
(Note: After doing this you must stop the server and then start it again)
For a more detailed guide to using mod_wsgi of for troubleshooting help, see: http://code.google.com/p/modwsgi/wiki/QuickInstallationGuide

=== Finally ===

Go to localhost to view the website
