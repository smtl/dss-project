== Decision Support System | DSS ===
DSS is an application to allow users to answer questions and get software development process recommendations to use for their own projects.


This project is hosted on Google Code: http://code.google.com/p/dss-project

An online version of this information can be found on the project's wiki page:

http://code.google.com/p/dss-project/w/list

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

=== First Run ===

You can download the files to any location that you have create/write permissions in if you want to use the development server included with Django. If you want to run the application on a production server such as Apache, you will need to place the files in a location that works with your Apache installation.

Note: Make sure you have create/write permissions wherever you put the files.

If you wish to use a new database, you will need to delete the database that was with the files and run the following command:

python manage.py syncdb

To test quickly, you can use the development server that comes with Django. Run the following command to turn on the development server:

python manage.py runserver

To run the unit tests included with the files, run the following command:

python manage.py test

=== Functions ===

Guests can answer questions

Guests answers are logged

User registration

User log in

User can change profiles

User can answer questions

User answers are stored

User can see a list of questions

Questions are presented to users based on their profile

Admin/Maintenance can add, edit, delete questions

Admin/Maintenance can add, edit, delete answers

Admin/Maintenance can add, edit, delete profiles

Admin/Maintenance can add, edit, delete question paths (which are assigned to profiles)

Admin/Maintenance can add, edit, delete recommendations

Admin/Maintenance can add, edit, delete links from answers to recommendations

Registered User count can be displayed


=== Known Issues ===

If a user is created in the admin interface, they are not assigned a profile upon creation and will run into an error screen when they try access the homepage.

It is possible to attempt to answer the same question twice if you access the questions through the full list of questions. Answering the same question twice will give an error screen.

=== User count ===

To view how many users are currently logged in or registered on the site, point to the below URL
http://localhost:8000/record_view/

This gives the total count of users.


