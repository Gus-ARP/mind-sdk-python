#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    xmind.core.labels
    ~~~~~~~~~~~~~~~~

    :copyright:
    :license:

"""

__author__ = "evgeny2900@gmail.com <Evgenii T.>"

from . import const

from .mixin import TopicMixinElement


class LabelsElement(TopicMixinElement):
    TAG_NAME = const.TAG_LABELS

    def __init__(self, node=None, ownerTopic=None):
        super(LabelsElement, self).__init__(node, ownerTopic)

    def getContent(self, format=const.PLAIN_FORMAT_LABEL):
        """ Get labels content

        :parma format:  specified returned content format, plain text
                        by default.
        """

        content = self.getFirstChildNodeByTagName(format)

        if not content:
            return

        content = Labels(node=content, ownerTopic=self.getOwnerTopic())

        return content.getTextContent()


class _LabelContentElement(TopicMixinElement):
    def __init__(self, node=None, ownerTopic=None):
        super(_LabelContentElement, self).__init__(node, ownerTopic)

    def getFormat(self):
        return self.getImplementation().tagName


class Labels(_LabelContentElement):
    """ Plain text label

    :param content: utf8 plain text.
    :param node:    `xml.dom.Element` object`
    :param ownerTopic:  `xmind.core.topic.TopicElement` object

    """

    TAG_NAME = const.PLAIN_FORMAT_LABEL

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
