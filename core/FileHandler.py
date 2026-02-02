import logging
import string
import os
import shutil
import sys
from tempfile import NamedTemporaryFile
sys.path.insert(0, './setpath/')
from ElementHandler import *

class FileHandler(object):

    def save_text_to_file(self, filename, filepath, text):
        with open(filepath + filename, 'w') as f:  
            f.write(text)
            
    def compare_two_files(self, filename1, filename2, filepath):
        if (FileHandler.count_lines(self, filepath, filename1) == FileHandler.count_lines(self, filepath, filename2)):
            logging.info('Same line count: ' + str(FileHandler.count_lines(self, filepath, filename1)))
        else:
            logging.warning('Not the same line count: \"' + str(FileHandler.count_lines(self, filepath, filename1))
                            + '\" and \"' + str(FileHandler.count_lines(self, filepath, filename2)) + '\"')
            ElementHandler.warning_switch()
        f1=open(filepath + filename1,"r")
        f2=open(filepath + filename2,"r")
        for line1 in f1:
            for line2 in f2:
                if line1==line2:
                    logging.info('Same line contents (' + line1 + ')')
                else:
                    logging.warning('Not the same line content: \"' + line1 + '\" and \"' + line2 + '\"')
                    ElementHandler.warning_switch()
                break
        f1.close()
        f2.close()
    
    def count_lines(self, filepath, filename):
        total_lines = sum(1 for line in open(filepath + filename))
        return total_lines
        
    def replace_text_in_the_file(self, filename, filepath, basetext, newtext):
        s = open(filepath + filename).read()
        s = s.replace(basetext, newtext)
        f = open(filepath + filename, 'w')
        f.write(s)
        f.close()
        
    def delete_file(self, filename, filepath):
        if os.path.exists(filepath + filename):
            os.remove(filepath + filename)
            
    def replace_line_content(self, filename, filepath, text_to_search, new_text):
        with open(filepath + filename) as fin, NamedTemporaryFile(dir=filepath, delete=False) as fout:
            for line in fin:
                if line.startswith(text_to_search):
                    line = text_to_search + new_text + '\n'
                fout.write(line.encode('utf8'))
            fin.close()
            fout.close()
            FileHandler.delete_file(self, filename, filepath)
            os.rename(fout.name, filepath + filename)   
            
    def delete_line_contains(self, filename, filepath, text):
        with open(filepath + filename) as fin, NamedTemporaryFile(dir=filepath, delete=False) as fout:
            for line in fin:
                if line.startswith(text):
                    line = ''
                fout.write(line.encode('utf8'))
            fin.close()
            fout.close()
            FileHandler.delete_file(self, filename, filepath)
            os.rename(fout.name, filepath + filename)  
            
    def copy_file(self, source_filename, destination_filename, filepath):
        shutil.copy(filepath + source_filename, filepath + destination_filename)
        