#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
    xmind.core.notes
    ~~~~~~~~~~~~~~~~

    :copyright:
    :license:

"""

__author__ = "aiqi@xmind.net <Woody Ai>"

from . import const

from .mixin import TopicMixinElement


class LabelsElement(TopicMixinElement):
    TAG_NAME = const.TAG_LABELS

    def __init__(self, node=None, ownerTopic=None):
        super(LabelsElement, self).__init__(node, ownerTopic)

    def getContent(self):
        """ Get notes content

        """

        content = self.getFirstChildNodeByTagName(const.TAG_LABEL)

        if not content:
            return

        return content.getTextContent()


class _LabelContentElement(TopicMixinElement):
    def __init__(self, node=None, ownerTopic=None):
        super(_LabelContentElement, self).__init__(node, ownerTopic)

    def getFormat(self):
        return self.getImplementation().tagName


class Labels(_LabelContentElement):
    """ text notes

    :param content: utf8 plain text.
    :param node:    `xml.dom.Element` object`
    :param ownerTopic:  `xmind.core.topic.TopicElement` object

    """

    TAG_NAME = const.LABEL

    def __init__(self, content=None, node=None, ownerTopic=None):
        super(Labels, self).__init__(node, ownerTopic)
        if content is not None:
            self.setTextContent(content)

    def setContent(self, content):
        self.setTextContent(content)


def main():
    pass

if __name__ == '__main__':
    main()
