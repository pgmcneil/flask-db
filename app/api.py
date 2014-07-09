#!/bin/env python

from app import app
from app import db
from app.models import models
from flask import request
from flask import jsonify
from flask import abort
import itertools


# Split up a path and return a dict
def pathsplit(path):
    if path is "":
        return dict()
    else:
        path = path.split("/")
        return dict(itertools.zip_longest(*[iter(path)] * 2, fillvalue=""))


def getmodels():
    classes = [cls for cls in models.Base.__subclasses__()]
    names = [c.__name__ for c in classes]
    return dict(zip(names, classes))


@app.route('/get/<obj>', methods=['GET'])
@app.route('/get/<obj>/<path:params>', methods=['GET'])
def getobject(obj, params=""):

    limit = request.args.get("limit", '')
    obj = obj.capitalize()
    params = pathsplit(params)
    objects = getmodels()
    if obj in objects.keys():
        newcls = objects[obj]
        query = db.session.query(newcls)
        for k, v in params.items():
            try:
                query = query.filter(getattr(newcls, k)
                                     .like("%{0}%".format(v)))
            except:
                abort(400)
        RESULT = [i.serialize for i in query.all()]
    else:
        abort(404)
    print(RESULT)
    return jsonify({"result": RESULT})


@app.route('/create/<obj>/<path:params>', methods=['GET'])
def create(obj, params):
    obj = obj.capitalize()
    params = pathsplit(params)
    objects = getmodels()
    if obj in objects.keys():
        newcls = objects[obj](**params)
    else:
        abort(400)
    try:
        db.session.add(newcls)
        db.session.commit()
        RESULT = newcls.serialize
    except:
        db.session.rollback()
        abort(500)
    return jsonify({"result": RESULT})
