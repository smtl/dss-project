# First Run #

Please follow the set up guide before trying to run.

You can download the files to any location that you have create/write permissions in if you want to use the development server included with Django. If you want to run the application on a production server such as Apache, you will need to place the files in a location that works with your Apache installation.

Note: Make sure you have create/write permissions wherever you put the files.

If you wish to use a new database, you will need to delete the database that was with the files and run the following command:

python manage.py syncdb

To test quickly, you can use the development server that comes with Django. Run the following command to turn on the development server:

python manage.py runserver

Navigate to localhost in your browser of choice to view the website.

To run the unit tests included with the files, run the following command:

python manage.py test