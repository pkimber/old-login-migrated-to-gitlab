User Login
**********

Django Application for user login and logout etc.

Install
=======

Virtual Environment
-------------------

::

  pyvenv-3.4 --without-pip venv-login
  source venv-login/bin/activate
  wget https://raw.githubusercontent.com/pypa/pip/master/contrib/get-pip.py
  python get-pip.py

  deactivate
  source venv-login/bin/activate

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
