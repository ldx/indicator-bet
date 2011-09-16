#!/usr/bin/env python

'''indicator-bet setup script'''

from distutils.core import setup

setup(
    name                = 'indicator-bet',
    version             = '0.0.1',
    description         = 'Ubuntu desktop indicator for the Budapest Stock Exchange',
    author              = 'Nilvec',
    author_email        = 'nilvec@nilvec.com',
    url                 = 'http://nilvec.com/',
    license             = 'Apache License, Version 2.0',
    scripts             = ['bin/indicator-bet'],
    data_files          = [('/etc/xdg/autostart', ['indicator-bet.desktop'])],
)
