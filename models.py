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
    def __init__(self, id, filename, origin_filename):
        self.id = id
        self.filename = filename
        self.origin_filename = origin_filename

    def to_json_obj(self):
        return {
            "id": self.id,
            "filename": self.filename,
            "origin_filename": self.origin_filename
        }

    @staticmethod
    def from_dict(data_dict):
        return Image(
            id = data_dict['id'],
            filename = data_dict['filename'],
            origin_filename = data_dict['origin_filename']
        )

def get_type_list():
    dump_list = []
    for key in types.keys():
        dump_list.append(types[key].to_json_obj())
    return json.dumps(dump_list)

def get_good_list():
    dump_list = []
    for key in goods.keys():
        dump_list.append(goods[key].to_json_obj())
    return json.dumps(dump_list)

def get_image_list():
    dump_list = []
    for key in images.keys():
        dump_list.append(images[key].to_json_obj())
    return json.dumps(dump_list)

def load():
    file_name = config['data_file']
    data_file = open(file_name, 'r')
    data = json.load(data_file)
    data_file.close()

    for good_dict in data['goods']:
        g = Good.from_dict(good_dict)
        goods[g.id] = g

    for type_dict in data['types']:
        g = GoodType.from_dict(type_dict)
        types[g.id] = g

    for image_dict in data['images']:
        g = Image.from_dict(image_dict)
        images[g.id] = g

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


# 初始化保证路径的存在
if not os.path.exists(config['image_path']):
    os.makedirs(config['image_path'])

if not os.path.exists(config['data_file']):
    save()

load()
