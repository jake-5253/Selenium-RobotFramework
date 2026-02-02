import json


class JSONValidator(object):

    def __init__(self, entity, entity_section, filepath):
        with open(filepath, 'r') as f:
            data = json.load(f)
            self.entity = entity
            self.data = data
            self.entity_section = entity_section

    def entity_data_json(self):
        entity_data = self.data[self.entity][self.entity_section]
        return entity_data

    def new_entity_data_json(self):
        entity_data = self.data[self.entity]
        return entity_data
