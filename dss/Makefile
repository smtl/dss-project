## jhnoll@gmail.com
#####################################################################
# Installation environment.  
# You can set where you want to install the project. Default is in the home directory
# It does not need to be changed for the proisis server
#HOME=

# This directory is where stuff served by Apache (the WSGI script and
# static content) goes.  
WSGI.dir=${HOME}/public_html/${PROJECT}
# This directory is where the Django code & db goes.
DATA.dir=${HOME}/data/${PROJECT}
TEMPLATES.dir=${HOME}/data
# File creation mode.  Please do not modify this: it will work on
# proisis.
FILE_MODE=ug+rwX,o+rX
DIR_MODE=ug+rwXs,o+rX
# Need write permissions for data/${PROJECT} and db
MY_MODE=ug+rwX,o+rwX
#####################################################################
# Project-specific parameters that should not be modified by users.

#
# Values for creating the distribution.
#

# Set PROJECT to the name of your project.
PROJECT=dss
# The upcoming release.
RELEASE=1.2
# The tar archive will be identified by version.
RELEASE_CANDIDATE=$(shell [ -f .svn ] && svn version|grep RELEASE|awk '{print $2}')
RELEASE_NAME=${PROJECT}-${RELEASE}-rc${RELEASE_CANDIDATE}
# Python doesn't allow dots and dashes in module names.
ARCHIVE.dir=$(subst -,_,$(subst .,_,${RELEASE_NAME}))
# Things to be excluded from the tar archive, after the workspace is cleaned.
TAR_EXCLUDE=--exclude='.svn' --exclude='.git' --exclude=${RELEASE_NAME}.tar.gz

#
# Things that are part of the program itself.
#

DB=database.db

# This is the basename of your wsgi script.  You must have a file
# called ${WSGI_NAME}.wsgi.tmpl that has a string "_DATA_DIR_" to be
# replaced by the value of ${DATA.dir}.
WSGI_NAME=dss
WSGI.script=${WSGI_NAME}.wsgi

#####################################################################
# Some programs used by rules below.

# Use ${INSTALL} to ensure all files & dirs get created with the right
# permissions. 
INSTALL=install --mode=${FILE_MODE}
WRITE_INSTALL=install --mode=${MY_MODE}
#####################################################################
# The rules.

all: test

what:
	@echo "PROJECT: " ${PROJECT} 
	@echo "RELEASE: " ${RELEASE}
	@echo "RELEASE_CANDIDATE: " ${RELEASE_CANDIDATE}
	@echo "RELEASE_NAME: " ${RELEASE_NAME}

# The 'test' rule just runs the unit tests, but because it depends on
# 'build', it will build the system first.
test: build
	python manage.py test

# The 'build' rule should do things like compile the PML parser and
# create the database if necessary.
# CAUTION: if you need to ship a default populated database, it should
# be created and populated here.  DO NOT do this by hand else you
# won't have a repeatable, reliable build process.
build: ${WSGI.script}
	python manage.py syncdb

# Install the application for deployment by Apache.
# install -d creates a directory if necessary.
install: test ${WSGI.script}
	${INSTALL} -d ${WSGI.dir}
	${INSTALL} -d ${WSGI.dir}/static
	${INSTALL} -d ${WSGI.dir}/media
	${INSTALL} -d ${WSGI.dir}/media/static
	${INSTALL} -d ${WSGI.dir}/media/static/admin
	${INSTALL} -d ${WSGI.dir}/media/static/admin/css
	${INSTALL} -d ${WSGI.dir}/media/static/admin/css/datepicker
	${INSTALL} -d ${WSGI.dir}/media/static/admin/img
	${INSTALL} -d ${WSGI.dir}/media/static/admin/img/admin
	${INSTALL} -d ${WSGI.dir}/media/static/admin/img/backgrounds
	${INSTALL} -d ${WSGI.dir}/media/static/admin/img/icons
	${INSTALL} -d ${WSGI.dir}/media/static/admin/jquery
	${INSTALL} -d ${WSGI.dir}/media/static/admin/jquery/i18n
	${INSTALL} -d ${WSGI.dir}/media/static/admin/jquery/ui
	${INSTALL} -d ${WSGI.dir}/media/static/admin/jquery/ui/css
	${INSTALL} -d ${WSGI.dir}/media/static/admin/jquery/ui/css/custom-theme
	${INSTALL} -d ${WSGI.dir}/media/static/admin/jquery/ui/css/custom-theme/images
	${INSTALL} -d ${WSGI.dir}/media/static/admin/jquery/ui/css/ui-lightness
	${INSTALL} -d ${WSGI.dir}/media/static/admin/jquery/ui/css/ui-lightness/images
	${INSTALL} -d ${WSGI.dir}/media/static/admin/jquery/ui/js
	${INSTALL} -d ${WSGI.dir}/media/static/admin/tinymce
	${INSTALL} -d ${WSGI.dir}/media/static/admin/tinymce/examples
	${INSTALL} -d ${WSGI.dir}/media/static/admin/tinymce/examples/css
	${INSTALL} -d ${WSGI.dir}/media/static/admin/tinymce/examples/lists
	${INSTALL} -d ${WSGI.dir}/media/static/admin/tinymce/examples/media
	${INSTALL} -d ${WSGI.dir}/media/static/admin/tinymce/examples/templates
	${INSTALL} -d ${WSGI.dir}/media/static/admin/tinymce/examples
	${INSTALL} -d ${WSGI.dir}/media/static/admin/tinymce/jscripts
	${INSTALL} -d ${WSGI.dir}/media/static/admin/tinymce_setup
	${INSTALL} -d ${TEMPLATES.dir}
	${INSTALL} -d ${TEMPLATES.dir}/templates/admin
	${INSTALL} -d ${TEMPLATES.dir}/templates/admin/auth
	${INSTALL} -d ${TEMPLATES.dir}/templates/admin/auth/profile
	${INSTALL} -d ${TEMPLATES.dir}/templates/admin/questions/
	${INSTALL} -d ${TEMPLATES.dir}/templates/admin/questions/question
	${INSTALL} -d ${TEMPLATES.dir}/templates/admin/recommendations
	${INSTALL} -d ${TEMPLATES.dir}/templates/admin/recommendations/recommendation
	${INSTALL} -d ${TEMPLATES.dir}/templates/admin/recommendations/uploadedfile
	${INSTALL} -d ${TEMPLATES.dir}/templates/questions
	${INSTALL} -d ${TEMPLATES.dir}/templates/auth
	${INSTALL} -d ${TEMPLATES.dir}/templates/recommendations
	${INSTALL} -d ${TEMPLATES.dir}/templates/registration
	${INSTALL} -d ${DATA.dir}
	${INSTALL} -d ${DATA.dir}/grappelli
	${INSTALL} -d ${DATA.dir}/auth
	${INSTALL} -d ${DATA.dir}/recommendations
	${INSTALL} -d ${DATA.dir}/questions
	${INSTALL} -d ${DATA.dir}/questions/templatetags
	${INSTALL} -d ${DATA.dir}/graphviz
	${INSTALL} -d ${DATA.dir}/graphviz/graph
	${INSTALL} -d ${DATA.dir}/graphviz/graph/analysis
	${INSTALL} -d ${DATA.dir}/graphviz/expr
	${INSTALL} -d ${DATA.dir}/graphviz/check
	${INSTALL} -d ${DATA.dir}/graphviz/check/link
	${INSTALL} -d ${DATA.dir}/graphviz/pml
	${INSTALL} -d ${DATA.dir}/grappelli
	${INSTALL} -d ${DATA.dir}/grappelli/dashboard
	${INSTALL} -d ${DATA.dir}/grappelli/dashboard/management
	${INSTALL} -d ${DATA.dir}/grappelli/dashboard/management/commands
	${INSTALL} -d ${DATA.dir}/grappelli/dashboard/templates
	${INSTALL} -d ${DATA.dir}/grappelli/dashboard/templates/admin
	${INSTALL} -d ${DATA.dir}/grappelli/dashboard/templates/grappelli
	${INSTALL} -d ${DATA.dir}/grappelli/dashboard/templates/grappelli/dashboard
	${INSTALL} -d ${DATA.dir}/grappelli/dashboard/templates/grappelli/dashboard/modules
	${INSTALL} -d ${DATA.dir}/grappelli/dashboard/templatetags
	${INSTALL} -d ${DATA.dir}/grappelli/templates
	${INSTALL} -d ${DATA.dir}/grappelli/templates/admin_doc
	${INSTALL} -d ${DATA.dir}/grappelli/templates/registration
	${INSTALL} -d ${DATA.dir}/grappelli/templates/admin
	${INSTALL} -d ${DATA.dir}/grappelli/templates/admin/edit_inline
	${INSTALL} -d ${DATA.dir}/grappelli/templates/admin/includes
	${INSTALL} -d ${DATA.dir}/grappelli/templates/admin/includes_grappelli
	${INSTALL} -d ${DATA.dir}/grappelli/templates/admin/auth/
	${INSTALL} -d ${DATA.dir}/grappelli/templates/admin/auth/user
	${INSTALL} -d ${DATA.dir}/grappelli/templatetags
	${INSTALL} -d ${DATA.dir}/grappelli/views
	${INSTALL} grappelli/*.* ${DATA.dir}/grappelli
	${INSTALL} grappelli/dashboard/*.* ${DATA.dir}/grappelli/dashboard
	${INSTALL} grappelli/dashboard/management/*.* ${DATA.dir}/grappelli/dashboard/management
	${INSTALL} grappelli/dashboard/management/commands/*.* ${DATA.dir}/grappelli/dashboard/management/commands
	${INSTALL} grappelli/dashboard/templates/admin/*.* ${DATA.dir}/grappelli/dashboard/templates/admin
	${INSTALL} grappelli/dashboard/templates/grappelli/dashboard/*.* ${DATA.dir}/grappelli/dashboard/templates/grappelli/dashboard
	${INSTALL} grappelli/dashboard/templates/grappelli/dashboard/modules/*.* ${DATA.dir}/grappelli/dashboard/templates/grappelli/dashboard/modules
	${INSTALL} grappelli/dashboard/templatetags/*.* ${DATA.dir}/grappelli/dashboard/templatetags
	${INSTALL} grappelli/templatetags/*.* ${DATA.dir}/grappelli/templatetags
	${INSTALL} grappelli/views/*.* ${DATA.dir}/grappelli/views
	${INSTALL} grappelli/templates/admin/*.* ${DATA.dir}/grappelli/templates/admin
	${INSTALL} grappelli/templates/admin/auth/user/*.* ${DATA.dir}/grappelli/templates/admin/auth/user
	${INSTALL} grappelli/templates/admin/edit_inline/*.* ${DATA.dir}/grappelli/templates/admin/edit_inline
	${INSTALL} grappelli/templates/admin/includes/*.* ${DATA.dir}/grappelli/templates/admin/includes
	${INSTALL} grappelli/templates/admin/includes_grappelli/*.* ${DATA.dir}/grappelli/templates/admin/includes_grappelli
	${INSTALL} grappelli/templates/admin_doc/*.* ${DATA.dir}/grappelli/templates/admin_doc
	${INSTALL} grappelli/templates/registration/*.* ${DATA.dir}/grappelli/templates/registration
	cp -r grappelli/static/grappelli/* ${WSGI.dir}/media/static/admin
	${INSTALL} graphviz/*.* ${DATA.dir}/graphviz
	${INSTALL} graphviz/pml/*.* ${DATA.dir}/graphviz/pml
	${INSTALL} graphviz/check/*.* ${DATA.dir}/graphviz/check
	${INSTALL} graphviz/check/link/*.* ${DATA.dir}/graphviz/check/link
	${INSTALL} graphviz/expr/*.* ${DATA.dir}/graphviz/expr
	${INSTALL} graphviz/graph/*.* ${DATA.dir}/graphviz/graph
	cp graphviz/graph/traverse ${DATA.dir}/graphviz/graph
	cp graphviz/graph/graphit ${DATA.dir}/graphviz/graph
	cp graphviz/graph/color-pml.awk ${DATA.dir}/graphviz/graph
	${INSTALL} graphviz/graph/analysis/*.* ${DATA.dir}/graphviz/graph/analysis
	${INSTALL} ${WSGI.script} ${WSGI.dir}/${PROJECT}.wsgi
	${INSTALL} .htaccess ${WSGI.dir}/.htaccess
	${INSTALL} media/static/admin/css/*.* ${WSGI.dir}/media/static/admin/css
	${INSTALL} media/static/admin/css/datepicker/* ${WSGI.dir}/media/static/admin/css/datepicker
	${INSTALL} media/static/admin/img/*.* ${WSGI.dir}/media/static/admin/img/
	${INSTALL} media/static/admin/img/admin/* ${WSGI.dir}/media/static/admin/img/admin
	${INSTALL} media/static/admin/img/backgrounds/* ${WSGI.dir}/media/static/admin/img/backgrounds
	${INSTALL} media/static/admin/img/icons/* ${WSGI.dir}/media/static/admin/img/icons
	${INSTALL} media/static/admin/jquery/*.* ${WSGI.dir}/media/static/admin/jquery
	${INSTALL} media/static/admin/jquery/i18n/* ${WSGI.dir}/media/static/admin/jquery/i18n
	${INSTALL} media/static/admin/jquery/ui/css/custom-theme/*.* ${WSGI.dir}/media/static/admin/jquery/ui/css/custom-theme
	${INSTALL} media/static/admin/jquery/ui/css/custom-theme/images/* ${WSGI.dir}/media/static/admin/jquery/ui/css/custom-theme/images
	${INSTALL} media/static/admin/jquery/ui/css/ui-lightness/*.* ${WSGI.dir}/media/static/admin/jquery/ui/css/ui-lightness
	${INSTALL} media/static/admin/jquery/ui/css/ui-lightness/images/* ${WSGI.dir}/media/static/admin/jquery/ui/css/ui-lightness/images
	${INSTALL} media/static/admin/jquery/ui/js/* ${WSGI.dir}/media/static/admin/jquery/ui/js
	${INSTALL} media/static/admin/tinymce/examples/*.* ${WSGI.dir}/media/static/admin/tinymce/examples
	${INSTALL} media/static/admin/tinymce/examples/css/*.* ${WSGI.dir}/media/static/admin/tinymce/examples/css
	${INSTALL} media/static/admin/tinymce/examples/lists/*.* ${WSGI.dir}/media/static/admin/tinymce/examples/lists
	${INSTALL} media/static/admin/tinymce/examples/media/*.* ${WSGI.dir}/media/static/admin/tinymce/examples/media
	${INSTALL} media/static/admin/tinymce/examples/templates/*.* ${WSGI.dir}/media/static/admin/tinymce/examples/templates
	${INSTALL} media/static/admin/tinymce_setup/*.* ${WSGI.dir}/media/static/admin/tinymce_setup/*.*
	${INSTALL} media/*.* ${WSGI.dir}/media
	${INSTALL} -D templates/*.* ${TEMPLATES.dir}/templates/
	#${INSTALL} -D templates/admin/*.* ${TEMPLATES.dir}/templates/admin
	${INSTALL} -D templates/admin/auth/profile/* ${TEMPLATES.dir}/templates/admin/auth/profile
	${INSTALL} -D templates/admin/questions/question/* ${TEMPLATES.dir}/templates/admin/questions/question
	${INSTALL} -D templates/admin/recommendations/recommendation/* ${TEMPLATES.dir}/templates/admin/recommendations/recommendation
	${INSTALL} -D templates/admin/recommendations/uploadedfile/* ${TEMPLATES.dir}/templates/recommendations/uploadedfile
	${INSTALL} -D templates/auth/* ${TEMPLATES.dir}/templates/auth
	${INSTALL} -D templates/questions/* ${TEMPLATES.dir}/templates/questions
	${INSTALL} -D templates/registration/* ${TEMPLATES.dir}/templates/registration
	${INSTALL} -D templates/recommendations/* ${TEMPLATES.dir}/templates/recommendations
	${INSTALL} questions/*.* ${DATA.dir}/questions
	${INSTALL} recommendations/*.* ${DATA.dir}/recommendations
	${INSTALL} auth/*.* ${DATA.dir}/auth
	${INSTALL} questions/templatetags/* ${DATA.dir}/questions/templatetags
	${INSTALL} -D *.py ${DATA.dir}
	${INSTALL} -D *.db ${DATA.dir}


# This will make a .wsgi script from a .wsgi.tmpl file.  Adding
# 'Makefile' as a dependency for this rule means the script will be
# re-made every time you change, for example, DATA.dir.
%.wsgi: %.wsgi.tmpl Makefile
	sed 's,_DATA_DIR_,${DATA.dir},' $< > $@

# Make a distribution archive from the current svn workspace.
# the 'distclean' dependency insures that the distribution is 
# free of derived files and other cruft.  Make sure 'distclean' 
# actually cleans!
# The '--transform' switch to 'tar' prepends a directory name to 
# each path in the archive, so that the distribution unpacks 
# into its own sub-directory.  This is extremely important, as it 
# ensures your project won't interfere with something else when
# it is unpacked.
dist: distclean
	tar ${TAR_EXCLUDE} --transform='s,^./,${ARCHIVE.dir}/,' -cvzf ${RELEASE_NAME}.tar.gz . --ignore-failed-read

clean: 
	rm -f *~

distclean: clean
	rm -f *.pyc
