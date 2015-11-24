#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
    xmind.import_export_filters.ExportFilter
    ~~~~~~~~~~~
    :mod:``xmind.import_export_filters.ExportFilter`` provide a handy way for exporting / importing 
    XMind files to other formats (e.g: GraphViz).
    :copyright: Michel Kern
    :license: MIT
"""

__author__ = "echopraxium@yahoo.com <Michel Kern>"

import os
import os.path
from ExportFilter import ExportFilter
from ExportFilter import FILE_NOT_FOUND_ERROR

#------------------- GraphvizExportFilter -------------------
class GraphvizExportFilter(ExportFilter):
    def __init__(self):
        ExportFilter.__init__(self)
        self.name = "graphviz_export_filter"
    
    #---------- export() ----------    
    def export(self, source_path, target_path):
        print(self.name + ".export ")
        print("export_filter.name: '" + self.name + "'")
        if (not os.path.isfile(source_path)): 
            print("source_path: '" + source_path + "' not found")
            exit(FILE_NOT_FOUND_ERROR)
    #---------- export()
#------------------- GraphvizExportFilter

#======================== main ========================
def main():
    print("** xmind.GraphvizExportFilter **")
    export_filter = GraphvizExportFilter()
    export_filter.export("", "")
    #pass

if __name__ == '__main__':
    main()
