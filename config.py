#!/bin/env python

import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'inv.db') #'postgres://postgres:postgres@localhost/Inv'
# SQLALCHEMY_DATABASE_URI = 'postgres://postgres:postgres@localhost/Inv'
SQLALCHEMY_RECORD_QUERIES = True