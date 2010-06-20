============
Installation
============

Requirements
============

In order to install `Django Flickrsets`_, you need to install these 
requirements:

    * `Python`_ >= 2.4 (not compatible 3.x)
    * `Django`_ >= 1.2
    * `South`_
    * `httplib2`_
    * `python-dateutil`_
    * `mock`_
    * `PrettyTable`_ (svn)

You can install all these requirements in one step with `Pip`_ using the
included ``requirements.txt`` file::

    pip install -r requirements.txt

To avoid conflicts and keep your Python environment safe, you should use
`Pip`_ with `virtualenv`_ and `virtualenvwrapper`_::

    pip install -E flickrsets -r requirements.txt
    workon flickrsets
    
Stable version
==============

To install the stable version of `Django Flickrsets`_, simply run::

    pip install django-flickrsets

You can also use `easy_install`_::

    easy_install django-flickrsets

Development version
===================

Grab the latest version on `GitHub`_::

    git clone git@github.com:gillesfabio/django-flickrsets.git
    
Copy or symlink ``flickrsets`` directory somewhere in your ``PYTHONPATH``.

Or use `Pip`_ with `virtualenv`_ and `virtualenvwrapper`_::

    cd django-flickrsets
    pip install -E flickrsets -r requirements.txt

.. _Django Flickrsets: http://github.com/gillesfabio/django-flickrsets
.. _Python: http://python.org/
.. _Django: http://www.djangoproject.com/
.. _South: http://south.aeracode.org/
.. _httplib2: http://code.google.com/p/httplib2/
.. _python-dateutil: http://labix.org/python-dateutil/
.. _mock: http://www.voidspace.org.uk/python/mock/
.. _PrettyTable: http://code.google.com/p/prettytable/
.. _Pip: http://pip.openplans.org/
.. _virtualenv: http://pypi.python.org/pypi/virtualenv/
.. _virtualenvwrapper: http://pypi.python.org/pypi/virtualenvwrapper
.. _easy_install: http://pypi.python.org/pypi/setuptools
.. _GitHub: http://github.com/gillesfabio/django-flickrsets
