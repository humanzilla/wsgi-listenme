# coding=utf-8

from setuptools import setup, find_packages


setup(
    name="wsgi-listenme",
    description="WSGI middleware for capture and browse requests and responses",
    version='1.0',
    author='Mario César Señoranis Ayala',
    author_email='mariocesar.c50@gmail.com',
    url='https://github.com/humanzilla/wsgi-listenme',
    packages=find_packages('wsgi_listenme'),
    license="MIT license",
    install_requires=[''],
    tests_require=["tox"],
    zip_safe=False,
    include_package_data=True
)