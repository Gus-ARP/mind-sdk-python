import unittest
import logging
import datetime
from os.path import isdir, exists
from os import mkdir

testModules = [
    'xmind.tests.test_loader',
    ]

suite = unittest.TestSuite()

for t in testModules:
    try:
        # If the module defines a suite() function, call it to get the suite.
        mod = __import__(t, globals(), locals(), ['suite'])
        suitefn = getattr(mod, 'suite')
        suite.addTest(suitefn())
    except (ImportError, AttributeError):
        # else, just load all the test cases from the module.
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName(t))

FORMAT = '[%(name)s - %(levelname)s] %(asctime)-15s: %(message)s'

now = datetime.datetime.now()
fileNameToStoreLogs = now.strftime('%Y-%m-%d_%H-%M-%S')

if not exists('./logs'):
    mkdir('./logs')
elif not isdir('./logs'):
    raise Exception('No directory logs for storing logs, remove file with a similar name')


logging.basicConfig(format=FORMAT, level=logging.DEBUG, filename='./logs/%s.log' % fileNameToStoreLogs)
logging.getLogger('global').info('Start tests')
unittest.TextTestRunner().run(suite)
logging.getLogger('global').info('End tests')