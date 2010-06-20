# -*- coding: utf-8 -*-
"""
Setup of Django Flickrsets application.
"""
import os
from setuptools import setup
from setuptools import find_packages

from flickrsets import VERSION


README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

setup(
    name='django-flickrsets',
    version='.'.join([str(n) for n in VERSION]),
    description='Reusable Django application to synchronize Flickr sets.',
    long_description=README,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    keywords='django,flickr,flickrsets,photo',
    author='Gilles Fabio',
    author_email='gilles.fabio@gmail.com',
    url='http://github.com/gillesfabio/django-flickrsets',
    license='BSD',
    packages=find_packages(exclude=['flickrsets_example']),
    package_data={
        'flickrsets': [
            'fixtures/*/*.json',
            'templates/*.html',
            'templates/*/*.html',
            'locale/*/LC_MESSAGES/*',
        ],
    },
    zip_safe=False,
)
