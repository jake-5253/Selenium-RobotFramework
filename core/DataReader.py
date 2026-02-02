import xml.etree.ElementTree as ET


class DataReader(object):

    def __init__(self, datafile):
        self.tree = ET.parse(datafile)
        self.root = self.tree.getroot()

    def type(self, data):
        for data_type in self.root.getiterator(data):
            self.get_data_type = data_type
            return self.get_data_type
 
    def first_name(self, type):
        for data in DataReader.type(self, type).getiterator('FIRST_NAME'):
            return data.text
        
    def last_name(self, type):
        for data in DataReader.type(self, type).getiterator('LAST_NAME'):
            return data.text
        
    def email(self, type):
        for data in DataReader.type(self, type).getiterator('EMAIL'):
            return data.text   
        
    def mobile_number(self, type):
        for data in DataReader.type(self, type).getiterator('MOBILE_NUMBER'):
            return data.text
        
    def run_keyword(self):
        return self