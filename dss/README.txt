Decision Support System | DSS
=============================

About
=====

DSS is an application that allows a system to be set up which allows an end user to answer questions and get results based on their answers.

This project is hosted on Google Code: http://code.google.com/p/dss-project

Developers
==========

Stephen Lowry

Stephen Murphy

Adrian Kwizera

Dependencies
===========

Python 2.7 (http://python.org/)

Django 1.3 (https://www.djangoproject.com/)

SQLite3 (http://www.sqlite.org/)

Apache 2.2.20 (http://httpd.apache.org/)

- mod_wsgi extension (http://code.google.com/p/modwsgi/)

Python Markdown (http://pypi.python.org/pypi/Markdown)

PyGraphviz (http://networkx.lanl.gov/pygraphiz/download.html)

Dependencies Configuration
========================

The project files can be retrieved by either using SVN, a version control system
or by downloading a archived file. We recommend downloading the archived file.

SVN Details
===========

SVN or Subversion is a version control system (http://subversion.apache.org/). It can be used to retrieve the files.

The following command will install SVN/Subversion

sudo apt-get install subversion

A guide to using subversion can be found at http://svnbook.red-bean.com/

To retrieve the files from the repository run the following commands

svn checkout http://dss-project.googlecode.com/svn/trunk/dss/

Python Details
==============

Ubuntu comes with python but you still might need to install the developer packages:

sudo apt-get install python-dev

Django Details
==============

We are using Django 1.3.1. The download and instructions to install can be found here

https://www.djangoproject.com/download/

Apache Details
==============

sudo apt-get install apache2

sudo apt-get install apache2-prefork-dev

(If you want a graphical interface to control the server, you can use https://launchpad.net/localhost-indicator)

Commands to control the apache2 server are:

sudo service apache2 restart

sudo service apache2 stop

mod_wsgi Details
================

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

Python Markdown
===============

Run the following command:

sudo apt-get install python-markdown

PyGraphviz Details
==================

Run the following:

sudo apt-get install python-pygraphviz
sudo apt-get install graphviz


Installation
===========

By default the project is installed into the Home directory and places content into two folders: data and public_html. You can change the intall location by changing the HOME variable in the Makefile.

To install,

1. Download the archive file
2. Extract the archive file

tar -xvf <archive_file_name>

3. Navigate into the project folder

cd <project_name>

4. Run 'make install'

5. On run, tests are first run and on successive build an installation is made

6. Any new project directories must be added first to the makefile before doing step 4


Help files
===============================

There are two help files (one for the guests and one for the maintainer/admin)

Guests help
===========
At the end of .wsgi/ add help to view the guest help file

Maintainer help
===============
Once logged into admin, click on the help link to view the guide


Frequently Encountered Problems
===============================

Problems you might encounter while setting up the website:

== “Unable to write read only database” or “Unable to open database file” ==

First, make sure a database file exists. If it does not, run the following command:

python manage.py syncdb

Make sure to make a superuser when prompted. This will allow you to access the admin interface.

Make sure you have permissions set right for the dss folder itself and the contents of the dss folder.

== Other Problems ==

If you encounter other problems it is good practice to try restart your server and try again. This may solve some issues.

Clearing your browsers cache or trying a different browser may also clear up problems.

Feature Description
===================

Admin Functions
==============
Default admin is username:admin, password:admin

1) Ability to create users and change their staff status

2) Ability to create questions with answers
 - Click questions
 - Click add Question
 - Type question
 - Click "Add another question"
  - Click blue Answer bar and observe text box dropping down
  - Type in Answer
  - Repeat for as many answers as you like
  - Click save
