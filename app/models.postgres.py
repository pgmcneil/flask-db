#!/bin/env python

from app import db
from sqlalchemy import types
from sqlalchemy.dialects import postgres


class Base(object):
    def __init__(self, *kargs, **kwargs):
        for d in kargs:
            for k in d:
                setattr(self, k, d[k])
        for k, v in kwargs:
            setattr(self, k, v)

    @property
    def serialize(self):
        n = self.__dict__
        del n['_sa_instance_state']
        return n


class Logical(db.Model, Base):
    __tablename__ = "logical"

    class status_enum(types.TypeDecorator, types.SchemaType):
        impl = postgres.ENUM

        def _set_parent(self, column):
            self.impl._set_parent(column)

    name = db.Column(db.VARCHAR(15), primary_key=True)
    admin = db.Column(db.VARCHAR(15))
    status = db.Column(status_enum('active', 'offline', 'staging', name="status_enum"))
    parent_physical = db.Column(db.INTEGER, db.ForeignKey('physical.asset'))

    def __repr__(self):
        return '<Logical (%s)>' % self.key()

    def key(self):
        return self.name


class Physical(db.Model, Base):
    __tablename__ = "physical"
    
    asset = db.Column(db.INTEGER, primary_key=True)
    owner = db.Column(db.VARCHAR(10))
    model = db.Column(db.VARCHAR(25))

    def __repr__(self):
        return '<Physical (%d)>' % self.key()

    def key(self):
        return self.asset
    
