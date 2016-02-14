User Login
**********

Django Application for user login and logout etc.

Install
=======

Virtual Environment
-------------------

::

  virtualenv --python=python3.4 venv-login
  source venv-login/bin/activate
  pip install --upgrade pip

  pip install -r requirements/local.txt

Testing
=======

::

  find . -name '*.pyc' -delete
  py.test -x

Usage
=====

::

  py.test -x && \
      touch temp.db && rm temp.db && \
      django-admin.py migrate --noinput && \
      django-admin.py demo_data_login && \
      django-admin.py runserver

You can log in with user ``staff``, password ``staff``...

To test the password reset, use web@pkimber.net

Release
=======

https://www.pkimber.net/open/
