#!/bin/env python

from app import db
from app.models import Base


class Logical(db.Model, Base):
    __tablename__ = "logical"

    name = db.Column(db.TEXT, primary_key=True)
    admin = db.Column(db.TEXT)
    status = db.Column(db.TEXT)
    parent_physical = db.Column(db.INTEGER, db.ForeignKey('physical.asset'))

    def key(self):
        return self.name


class Physical(db.Model, Base):
    __tablename__ = "physical"
    
    asset = db.Column(db.INTEGER, primary_key=True)
    owner = db.Column(db.TEXT)
    model = db.Column(db.TEXT)

    def __repr__(self):
        return '<Physical (%d)>' % self.key()

    def key(self):
        return self.asset
    
