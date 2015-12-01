#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
    xmind.import_export.GraphvizExportFilter
    ----------------------------------------
    :mod:       ``xmind.import_export.ExportFilter`` provide a handy way for exporting 
                XMind files to dot format (see http://www.graphviz.org/pdf/dotguide.pdf)
                GraphViz (http://www.graphviz.org/) 
    :copyright: Michel Kern
    :license:   MIT
"""

__author__ = "echopraxium@yahoo.com <Michel Kern>"

import os
import os.path
import xmind
from xmind.core       import workbook,saver
from xmind.core.topic import TopicElement
from ExportFilter     import ExportFilter
from ExportFilter     import FILE_NOT_FOUND_ERROR, EMPTY_OUTPUT_FILE_PATH_ERROR

#------------------- GraphvizExportFilter -------------------
class GraphvizExportFilter(ExportFilter):
    #---------- constructor ----------
    def __init__(self):
        ExportFilter.__init__(self)
        self.name = "graphviz_export_filter"
        self.output_str = ''
        self.topic_count = 0
        
    #---------- traverse() ----------
    def getOutput(self):
        return self.output_str
    
    #---------- export() ----------    
    def export(self, source_path, target_path):
        print(self.name + ".export ")
            
        if (not os.path.isfile(source_path)): 
            print("> *ERROR* source_path: '" + source_path + "' not found")
            exit(FILE_NOT_FOUND_ERROR)
           
        # load an existing file or create a new workbook if nothing is found 
        workbook   = xmind.load(source_path) 
        worksheet  = workbook.getPrimarySheet() # get the first sheet
        root_topic = worksheet.getRootTopic()   # get the root topic of this sheet
        
        self.generateGraphvizDotString(root_topic)
        self.writeGraphvizDotToFile(target_path)
        self.generateImageFile(target_path, '../data/out.pdf')
        
        print(">> export done")
        
    #---------- generateGraphvizDotString() ----------  
    def generateGraphvizDotString(self, root_topic):
        self.output_str = u"digraph G {\n"
        
        #self.output_str = self.output_str + u'    overlap=scalexy;';
        #self.output_str = self.output_str + u'    ranksep=3;\n'
        #self.output_str = self.output_str + u'    ratio=auto;\n'

        self.output_str = self.output_str + u'root=topic_1;'
        self.output_str = self.output_str + u'overlap=false;';

        self.traverse(root_topic)    
        self.output_str = self.output_str + u"}"
    #---------- generateGraphvizDotString()
    
    #---------- writeGraphvizDotToFile() ----------  
    def writeGraphvizDotToFile(self, target_path):
        if (target_path == ''): 
            print("> *ERROR* target_path is empty")
            exit(EMPTY_OUTPUT_FILE_PATH_ERROR)
            
        out_fd = open(target_path, "w")
        out_fd.write(self.output_str.encode(('utf8')))
        out_fd.close()
    #---------- writeGraphvizDotToFile()
    
    #---------- generateImageFile() ----------  
    def generateImageFile(self, dot_input_path, img_output_path):
        if (img_output_path == ''): 
            print("> *ERROR* output_path is empty")
            exit(EMPTY_OUTPUT_FILE_PATH_ERROR)
            
        #graphviz_tool = 'dot'
        graphviz_tool = 'twopi'
        graphviz_dot_path = 'C:\\Program Files (x86)\\Graphviz\\bin\\' + graphviz_tool + '.exe'
        if (not os.path.isfile(graphviz_dot_path)): 
            print("> *ERROR* Graphviz dot.exe: '" + graphviz_dot_path + "' not found")
            exit(FILE_NOT_FOUND_ERROR)
        
        # dot -Tps -l lib.ps file.gv -o file.ps
        print(os.getcwd())
        cmd = '\"' + graphviz_dot_path + '\" -Tpdf ' + dot_input_path + ' -o ' + img_output_path
        print(cmd)
        os.system(cmd)
    #---------- generateImageFile()
        
    #---------- traverse() ----------
    def traverse(self, topic, parent_id='', parent_index=0, level=0):
        self.topic_count = self.topic_count + 1
        topic_index = self.topic_count
        
        if (parent_id != ''):
            topic_id = u'topic_' + str(parent_index) + '_' + str(topic_index)
            self.output_str = self.output_str + u'    ' + parent_id + u'->' + topic_id + u';\n' 
        else:
            topic_id = u'topic_' + str(topic_index)
        
        indent = ' ' * (level * 2)
        topic_title = unicode(topic.getTitle())
        
        msg = indent + '> ' + str(level) + ': ' + topic_title
        
        font_size = 30 - level*2.5
        shape_attribute = ' shape=box, '
        
        # http://rich-iannone.github.io/DiagrammeR/graphviz.html
        color_attribute = ' style=filled, color=Beige, '
        
        if (level == 0):
            font_size = 35
            shape_attribute = ' shape=box, margin=\"0.2,0.1\", '
        elif (level == 1):
            font_size = 30
            shape_attribute = ' shape=box, margin=\"0.2,0.07\", '
        else:
            font_size = 30 - level*2.5
            shape_attribute = ' shape=plaintext, '
            color_attribute = ' style=filled, color=LightCyan, '
            
        font_attribute = u'fontname = \"Helvetica\", fontsize = ' + str(font_size) + ', '
        
        #if (len(topic_title) > 15):
        #    words = topic_title.split(' ')
        #    word_count = len(words)
        #    multiline_topic_title= ''
        #    word_index = 0
        #    for word in words:
        #        multiline_topic_title = multiline_topic_title + word[word_index]
            
        label_attribute = ' label=\"' + topic_title + '\", '
        
        self.output_str = self.output_str + u'    ' + topic_id + u' [' 
        self.output_str = self.output_str + font_attribute + label_attribute + shape_attribute + color_attribute
        self.output_str = self.output_str + u' ];\n'
        
        topics = topic.getSubTopics()

        if (topics == None):
            print(msg + ' is a LEAF')
            return 
        else:
            print(msg)
            
        for child_topic in topics:
            self.traverse(child_topic, topic_id, topic_index, level+1)
    #---------- export()
#------------------- GraphvizExportFilter

#======================== main ========================
def main():
    print("** xmind.GraphvizExportFilter **")
    export_filter = GraphvizExportFilter()
    export_filter.export("../data/Hindouisme.xmind", "../data/map.dot")
    print(export_filter.getOutput())
    #pass

if __name__ == '__main__':
    main()