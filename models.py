import json
import os
from settings import config

goods = {} # good_id -> good_class
types = {} # type_id -> type_class
images = {} # image_id -> image_class

class Good():
    def __init__(self, id, type_id, good_name, show_index):
        self.id = id
        self.type_id = type_id
        self.good_name = good_name
        self.show_index = show_index

    def to_json_obj(self):
        return {
            "id": self.id,
            "good_name": self.good_name,
            "type_id": self.type_id,
            "show_index": self.show_index,
        }

    @staticmethod
    def from_dict(data_dict):
        return Good(
            id = data_dict['id'],
            good_name = data_dict['good_name'],
            type_id = data_dict['type_id'],
            show_index = data_dict['show_index'],
        )

class GoodType():
    def __init__(self, id, type_name, show_index):
        self.id = id
        self.type_name = type_name
        self.show_index = show_index

    def to_json_obj(self):
        return {
            "id": self.id,
            "type_name": self.type_name,
            "show_index": self.show_index,
        }

    @staticmethod
    def from_dict(data_dict):
        return GoodType(
            id = data_dict['id'],
            type_name = data_dict['type_name'],
            show_index = data_dict['show_index'],
        )

class Image():
    def __init__(self, id, filename):
        self.id = 1
        self.filename = ""

    def to_json_obj(self):
        return {
            "id": self.id,
            "filename": self.filename,
        }

    @staticmethod
    def from_dict(data_dict):
        return Image(
            id = data_dict['id'],
            filename = data_dict['filename']
        )


def load():
    file_name = config['data_file']
    if os.path.exists(file_name):
        data_file = open(file_name, 'r')
        data = json.load(data_file)
        data_file.close()

        for good_dict in data['goods']:
            g = Good.from_dict(good_dict)
            goods[g.id] = g

        for type_dict in data['types']:
            g = GoodType.from_dict(type_dict)
            types[g.id] = g
    else:
        goods = {}
        types = {}

def save():
    dump_dict = {'types': [], 'goods': [], 'images': []}
    for key in goods.keys():
        dump_dict['goods'].append(goods[key].to_json_obj())
    for key in types.keys():
        dump_dict['types'].append(types[key].to_json_obj())
    for key in images.keys():
        dump_dict['images'].append(images[key].to_json_obj())

    file_name = config['data_file']
    data_file = open(file_name, 'w')
    json.dump(dump_dict, data_file)
    data_file.close()
