#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
    xmind.import_export.ExportFilter
    ~~~~~~~~~~~
    :mod:``xmind.import_export_filters.ExportFilter`` provide a handy way for exporting / importing 
    XMind files to other formats (e.g: GraphViz).
    :copyright: Michel Kern
    :license: MIT
"""

__author__ = "echopraxium@yahoo.com <Michel Kern>"

import os
import os.path

FILE_NOT_FOUND_ERROR = 1
        
#------------------- ExportFilter -------------------
class ExportFilter():
    def __init__(self):
        self.name = "export_filter"
    
    #---------- export() ----------    
    def export(self, source_path, target_path):
        print(self.name + ".export ")
        if (not os.path.isfile(source_path)): 
            print("source_path: '" + source_path + "' not found")
            exit(FILE_NOT_FOUND_ERROR)
    #---------- export()
#------------------- ExportFilter

#======================== main ========================
def main():
    print("** xmind.ExportFilter **")
    export_filter = ExportFilter()
    export_filter.export("", "")
    #pass

if __name__ == '__main__':
    main()
