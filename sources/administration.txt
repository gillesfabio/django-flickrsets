==============
Administration
==============

django.contrib.admin
====================

Go in the admin and add Flickr sets you want to synchronize by adding new
*registered set* objects.

For each set, two required fields:

    * ``flickr_id``: The Flickr set ID
    * ``title``: The Flickr set Title (just to identify the set, not displayed)
    * ``enabled``: enable or disable the set for synchronization

Never ever add/delete/change *Person*, *Photoset*, *Photo* and *Tag* objects.
They are managed by the application.

Application's CLI
=================

`Django Flickrsets`_ adds ``fsets`` command to Django command list.

Command syntax::

    python manage.py fsets [command]

This command provides commands to help you managing your Flickr sets:

    * ``add``: registers a new Flickr set for synchronization
    * ``remove``: removes (deletes) a registered Flickr set
    * ``list``: lists all registered Flickr sets
    * ``disable``: disables an enabled Flickr set
    * ``enable``: enables a disabled Flickr set
    * ``sync``: synchronizes registered Flickr sets with Flickr
    * ``flush``: flushes existing tables
    
``fsets add``
-------------

The ``fsets add`` command lists all public sets of the Flickr User previously
defined in ``settings.FLICKRSETS_FLICKR_USER_ID``.

Example::

    python manage.py fsets add
    +----+--------------------------------------+-------------------+--------+
    | ID | Title                                |         Flickr ID | Status |
    +----+--------------------------------------+-------------------+--------+
    |  0 | Misc                                 | 72157623007721343 | REMOTE |
    |  1 | Flowers                              | 72157622950744561 | REMOTE |
    |  2 | Neige 2009                           | 72157622911766549 | REMOTE |
    |  3 | Monaco (2009-08)                     | 72157622035597150 | REMOTE |
    |  4 | Ladybug                              | 72157621969558560 | REMOTE |
    |  5 | Piscine Saint-Paul (2009-07)         | 72157621969224974 | REMOTE |
    |  6 | Parc Phoenix (2009-05)               | 72157621965519776 | REMOTE |
    |  7 | Huguette's Garden                    | 72157621840015339 | REMOTE |
    |  8 | Jardin Exotique de Monaco (2009-06)  | 72157621961569334 | REMOTE |
    |  9 | Fête des mères 2009                  | 72157621961447878 | REMOTE |
    | 10 | Sainte-Pétronille 2009               | 72157621961311960 | REMOTE |
    | 11 | Titouille                            | 72157617166890176 | REMOTE |
    | 12 | Colors                               | 72157617075048293 | REMOTE |
    | 13 | Black and White                      | 72157617166578442 | REMOTE |
    | 14 | Clouds                               | 72157617074848637 | REMOTE |
    | 15 | Saint-Laurent-du-Var                 | 72157617166199280 | REMOTE |
    | 16 | Nice #4 (2009-02)                    | 72157614259114644 | REMOTE |
    | 17 | Nice #3 (2009-02)                    | 72157614181081167 | REMOTE |
    | 18 | Nice #2 (2009-02)                    | 72157613842687348 | REMOTE |
    | 19 | Noël 2008                            | 72157611579724263 | REMOTE |
    | 20 | Sushi #1 (2008-07)                   | 72157606328118682 | REMOTE |
    | 21 | 2008-07-14                           | 72157606331530077 | REMOTE |
    | 22 | Airbus A320, Nice                    | 72157606176606116 | REMOTE |
    | 23 | Sainte-Pétronille 2008               | 72157606180078995 | REMOTE |
    | 24 | Cannes #1 (2008-07)                  | 72157606328349386 | REMOTE |
    | 25 | Gourdon (2008-03)                    | 72157606171366781 | REMOTE |
    | 26 | Grotte de Baume Obscure (2008-07)    | 72157606167343310 | REMOTE |
    | 27 | Screenshots                          | 72157604610567630 | REMOTE |
    | 28 | Saint-Jean-Cap-Ferrat (2008-03)      | 72157604162678938 | REMOTE |
    | 29 | Marineland (2008-02)                 | 72157604164536775 | REMOTE |
    | 30 | Nice #1 (2008-03)                    | 72157604159570014 | REMOTE |
    | 31 | Zoo, Saint-Jean-Cap-Ferrat (2008-02) | 72157604162849705 | REMOTE |
    | 32 | Crèche 2007                          | 72157604151543645 | REMOTE |
    | 33 | Juan-les-Pins (2007-11)              | 72157603084586221 | REMOTE |
    | 34 | 25 ans                               | 72157602826143640 | REMOTE |
    | 35 | Eze (2007-10)                        | 72157602821813034 | REMOTE |
    | 36 | Parc Phoenix (2007-10)               | 72157602454948487 | REMOTE |
    | 37 | Boréon (2007-09)                     | 72157602453309541 | REMOTE |
    | 38 | Animals                              | 72157600572928124 | REMOTE |
    | 39 | Arrière-pays (2007-05)               | 72157600572655571 | REMOTE |
    | 40 | La Garoupe (2007-01)                 | 72157600572355520 | REMOTE |
    +----+--------------------------------------+-------------------+--------+

    Which Flickr set(s) you want to add? 1 12 38
    Added set "Flowers" (72157622950744561).
    Added set "Colors" (72157617075048293).
    Added set "Animals" (72157600572928124).

``fsets remove``
----------------

The ``fsets remove`` command removes given registered Flickr sets.

Example::

    python manage.py fsets remove
    +----+---------+-------------------+---------+
    | ID | Title   |         Flickr ID |  Status |
    +----+---------+-------------------+---------+
    |  0 | Misc    | 72157623007721343 | ENABLED |
    |  1 | Clouds  | 72157617074848637 | ENABLED |
    |  2 | Flowers | 72157622950744561 | ENABLED |
    |  3 | Colors  | 72157617075048293 | ENABLED |
    |  4 | Animals | 72157600572928124 | ENABLED |
    +----+---------+-------------------+---------+

    Which Flickr set(s) you want to remove? 3
    Removed set Colors (72157617075048293).

``fsets list``
--------------

The ``fsets list`` command lists all registered Flickr sets.

Example::

    python manage.py fsets list
    +----+---------+-------------------+---------+
    | ID | Title   |         Flickr ID |  Status |
    +----+---------+-------------------+---------+
    |  0 | Misc    | 72157623007721343 | ENABLED |
    |  1 | Clouds  | 72157617074848637 | ENABLED |
    |  2 | Flowers | 72157622950744561 | ENABLED |
    |  3 | Animals | 72157600572928124 | ENABLED |
    +----+---------+-------------------+---------+

``fsets disable``
-----------------

The ``fsets disable`` disables synchronization for given Flickr sets.

Example::

    python manage.py fsets disable
    +----+---------+-------------------+---------+
    | ID | Title   |         Flickr ID |  Status |
    +----+---------+-------------------+---------+
    |  0 | Misc    | 72157623007721343 | ENABLED |
    |  1 | Clouds  | 72157617074848637 | ENABLED |
    |  2 | Flowers | 72157622950744561 | ENABLED |
    |  3 | Animals | 72157600572928124 | ENABLED |
    +----+---------+-------------------+---------+

    Which Flickr set(s) you want to disable? 3
    Set Animals (72157600572928124) is disabled.
    
    python manage.py fsets list
    +----+---------+-------------------+----------+
    | ID | Title   |         Flickr ID |  Status  |
    +----+---------+-------------------+----------+
    |  0 | Misc    | 72157623007721343 | ENABLED  |
    |  1 | Clouds  | 72157617074848637 | ENABLED  |
    |  2 | Flowers | 72157622950744561 | ENABLED  |
    |  3 | Animals | 72157600572928124 | DISABLED |
    +----+---------+-------------------+----------+

``fsets enable``
----------------

The ``fsets enable`` command enables synchronization for given Flickr sets.

Example::

    python manage.py fsets enable
    +----+---------+-------------------+----------+
    | ID | Title   |         Flickr ID |  Status  |
    +----+---------+-------------------+----------+
    |  0 | Animals | 72157600572928124 | DISABLED |
    +----+---------+-------------------+----------+

    Which Flickr set(s) you want to enable? 0
    Set Animals (72157600572928124) is enabled.
    
    python manage.py fsets list
    +----+---------+-------------------+---------+
    | ID | Title   |         Flickr ID |  Status |
    +----+---------+-------------------+---------+
    |  0 | Misc    | 72157623007721343 | ENABLED |
    |  1 | Clouds  | 72157617074848637 | ENABLED |
    |  2 | Flowers | 72157622950744561 | ENABLED |
    |  3 | Animals | 72157600572928124 | ENABLED |
    +----+---------+-------------------+---------+

``fsets sync``
--------------

The ``fsets sync`` command runs synchronization for enabled Flickr sets.

Example::

    python manage.py fsets sync

``fsets flush``
---------------

The ``fsets flush`` command flushes (resets) existing tables (but does not 
touch to registered sets).

Example::

    python manage.py fsets flush
    2010-06-23 09:15:25,195 [INFO] -- Django Flickrsets -- Flushed table: flickrsets_person
    2010-06-23 09:15:25,197 [INFO] -- Django Flickrsets -- Flushed table: flickrsets_photo
    2010-06-23 09:15:25,198 [INFO] -- Django Flickrsets -- Flushed table: flickrsets_photoset
    2010-06-23 09:15:25,198 [INFO] -- Django Flickrsets -- Flushed table: flickrsets_photo_tag


.. _Django Flickrsets: http://github.com/gillesfabio/django-flickrsets
