============
Installation
============

Requirements
============

Required dependencies
---------------------

    * `Python`_ >= 2.4 (not compatible 3.x)
    * `Django`_ >= 1.2
    * `South`_
    * `httplib2`_
    * `python-dateutil`_
    * `mock`_
    * `PrettyTable`_ (svn)

The viking way
--------------

You are a crazy system administrator? You can do almost everything with a 
command line interface, even programming a Linux printer driver in less than 
ten seconds with only two fingers? You don't have to deal with 
different versions of Python dependencies? This is the viking way to go::

    easy_install -U Django South httplib2 python-dateutil mock

Then::

    svn co http://prettytable.googlecode.com/svn/trunk/ prettytable
    cd prettytable/src
    python setup.py install

Of course, you should have Python 2.4, 2.5 or 2.6 and Subversion already 
installed on your system.

The safe way
------------

To avoid conflicts and keep your Python environment safe, you should install 
and use `Pip`_ with `virtualenv`_ and `virtualenvwrapper`_::

    easy_install -U pip
    pip install virtualenv
    pip install virtualenvwrapper

Create a directory which will store your virtual environments::

    mkdir $HOME/virtualenvs

In your ``$HOME/.bashrc_profile``, ``$HOME/.bashrc`` or ``$HOME/.profile`` 
file, exports the ``WORKON_HOME`` and ``PIP_VIRTUALENV_BASE`` variables. 

So, add these lines in the file::

    export WORKON_HOME=$HOME/virtualenvs
    export PIP_VIRTUALENV_BASE=$WORKON_HOME

Then, don't forget to load modifications with the ``source`` command::

    source $HOME/your-dot-file
    
Or, re-open a user session.
    
Now, you can install all requirements in one step with `Pip`_ using the
included ``requirements.txt`` file::

    pip install -E flickrsets -r requirements.txt

Easy as pie. 

As you have created the ``flickrsets`` environment via ``-E`` option, you just 
have to enable it with the ``workon`` command::

    workon flickrsets

That's all. You are ready to install `Django Flickrsets`_.

Stable version
==============

The viking way
--------------

Use this command::

    easy_install -U django-flickrsets

The safe way
------------

Use this command::

    pip install -E flickrsets django-flickrsets

Development version
===================

The viking way
--------------

Grab the latest version on `GitHub`_::

    git clone git://github.com/gillesfabio/django-flickrsets.git

Copy or symlink ``flickrsets`` directory somewhere in your ``PYTHONPATH``. 

You can also add the ``django-flickrsets`` directory to your ``PYTHONPATH``::

    export PYTHONPATH=$PYTHONPATH:$HOME/path/to/django-flickrsets

The safe way
------------

Grab the latest version on `GitHub`_::

    git clone git://github.com/gillesfabio/django-flickrsets.git

Then enable your virtual environment and add the directory::

    cd django-flickrsets
    workon flickrsets
    add2virtualenv .


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
