#!/bin/env python

from app import db


class Base(object):
    def __init__(self, *kargs, **kwargs):
        for d in kargs:
            for k in d:
                setattr(self, k, d[k])
        for k, v in kwargs:
            setattr(self, k, v)

    @property
    def serialize(self):
        return dict((k, v) for (k, v) in self.__dict__.items() if k is not "_sa_instance_state")
    
    def __repr__(self):
        return "<{0} ({1})>".format(self.__class__.__name__, 
                                    ', '.join("{0}={1}".format(k, v) for (k, v) in self.serialize.items()))