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

  ./init_dev.sh

You can log in with user ``staff``, password ``letmein``...

To test the password reset, use web@pkimber.net

Release
=======

https://www.kbsoftware.co.uk/docs/
