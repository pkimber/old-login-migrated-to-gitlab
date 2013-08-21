User Login
**********

Django Application for User login/logout/registration etc

Install
=======

Virtual Environment
-------------------

Note: replace ``patrick`` with your name (checking in the ``example`` folder to make sure a file
has been created for you).

::

  mkvirtualenv dev_login
  pip install -r requirements/local.txt

  echo "export DJANGO_SETTINGS_MODULE=example.dev_patrick" >> $VIRTUAL_ENV/bin/postactivate
  echo "unset DJANGO_SETTINGS_MODULE" >> $VIRTUAL_ENV/bin/postdeactivate

  add2virtualenv ../base
  add2virtualenv .
  deactivate

To check the order of the imports:

::

  workon dev_login
  cdsitepackages
  cat _virtualenv_path_extensions.pth

Check the imports are in the correct order e.g:

::

  /home/patrick/repo/dev/app/login
  /home/patrick/repo/dev/app/base

Testing
=======

We use ``pytest-django``:

::

  workon dev_login
  find . -name '*.pyc' -delete
  py.test

To stop on first failure:

::

  py.test -x

Usage
=====

::

  workon dev_login
  django-admin.py syncdb --noinput
  django-admin.py demo_data_login
  django-admin.py runserver

You can log in with user ``staff``, password ``staff``...
