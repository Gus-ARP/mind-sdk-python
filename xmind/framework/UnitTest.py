#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
    xmind.framework.UnitTest
    ------------------------
    :mod:       ``xmind.framework.UnitTest`` provides unit test superclass 
    :copyright: Michel Kern 
    :license:   MIT
"""

__author__ = "echopraxium@yahoo.com <Michel Kern>"

#------------------- UnitTest -------------------
class UnitTest:
   def __init__(self):
      self.name = "unit_test"
      
   def run(self):
      print("> run '" + self.name + "'")
#------------------- UnitTest

#======================== main ========================
def main():
   print("** xmind.framework.UnitTest **")

   ut = UnitTest()
   ut.run()

if __name__ == '__main__':
    main()
