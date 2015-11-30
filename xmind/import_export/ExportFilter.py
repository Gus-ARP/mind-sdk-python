#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
    xmind.import_export.ExportFilter
    --------------------------------
    :mod:``xmind.import_export.ExportFilter`` provide a handy way for exporting / importing 
    XMind files to other formats (e.g: GraphViz).
    :copyright: Michel Kern
    :license:   MIT
"""

__author__ = "echopraxium@yahoo.com <Michel Kern>"

import os
import os.path
from xmind.framework.Enum import Enum

FILE_NOT_FOUND_ERROR         = 1
EMPTY_OUTPUT_FILE_PATH_ERROR = 2
RETURN_CODE = Enum('OK', 'FILE_NOT_FOUND_ERROR', 'EMPTY_OUTPUT_FILE_PATH_ERROR')
        
#------------------- ExportFilter -------------------
class ExportFilter():
    def __init__(self):
        self.name = "export_filter"
    
    #---------- export() ----------    
    def export(self, source_path, target_path):
        print(self.name + ".export ")
        if (not os.path.isfile(source_path)): 
            print("source_path: '" + source_path + "' not found")
            exit(RETURN_CODE.FILE_NOT_FOUND_ERROR)
        return RETURN_CODE.OK
    #---------- export()
#------------------- ExportFilter

#======================== main ========================
def main():
    print("** xmind.ExportFilter **")
    export_filter = ExportFilter()
    rc = export_filter.export("../data/t.txt", "")
    print(rc)
    #pass

if __name__ == '__main__':
    main()

