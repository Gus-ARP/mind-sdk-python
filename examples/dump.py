#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:  hzsunshx
# Created: 2014-11-14 11:27

"""
dump xmind files
"""

import xmind
import pipes

M = {}

def _echo(tag, element, indent=0):
    title = element.getTitle()
    M[element.getID()] = title
    print '\t'*indent, tag, ':', pipes.quote(title)

def dump_sheet(sheet):
    rootTopic = sheet.getRootTopic()
    _echo('RootTopic', rootTopic, 1)

    for topic in rootTopic.getSubTopics() or []:
        _echo('AttachedSubTopic', topic, 2)

    for topic in rootTopic.getSubTopics(xmind.core.const.TOPIC_DETACHED) or []:
        _echo('DetachedSubTopic', topic, 2)

    for rel in sheet.getRelationships():
        id1, id2 = rel.getEnd1ID(), rel.getEnd2ID()
        print 'Relation:', M.get(id1), '-->', M.get(id2)

def main():
    x = xmind.load('test2.xmind')
    for sheet in x.getSheets():
        _echo('Sheet', sheet)
        dump_sheet(sheet)

if __name__ == '__main__':
    main()
