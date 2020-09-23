import time
import models
import errcode
import os
from settings import config
import random

def get_id(collison=[]):
    while True:
        id = int(time.time()) * 100 + random.randrange(0, 100)
        if id not in collison:
            return id

def add_type(type_name, show_index=1):
    t = models.GoodType(get_id(list(models.types.keys)), type_name, show_index)
    models.types[t.id] = t
    models.save()
    return errcode.OK

def rm_type(type_id):
    if type_id not in models.types:
        return errcode.TYPE_NOT_EXISTS

    keys = list(models.goods.keys())

    for key in keys:
        g = models.goods[key]
        if g.type_id == type_id:
            print("del ", g.id)
            del models.goods[key]

    del models.types[type_id]
    models.save()
    return errcode.OK

def add_good(good_name, type_id, show_index=1):
    g = models.Good(get_id(), type_id, good_name, show_index)
    models.goods[g.id] = g
    return errcode.OK

def rm_good(good_id):
    if good_id not in models.goods:
        return errcode.GOOD_NOT_EXISTS

    del models.goods[good_id]
    models.save()
    return errcode.OK

def get_img_list():
    return models.get_image_list()

def add_image(req_file):
    origin_filename, file_ext = os.path.splitext(req_file.filename)
    g_id = get_id(list(models.images.keys()))
    g_filename = str(g_id) + file_ext

    save_filename = os.path.join(config['image_path'], g_filename)
    req_file.save(save_filename)

    g = models.Image(g_id, g_filename, req_file.filename)
    models.images[g.id] = g
    models.save()
    return errcode.OK
