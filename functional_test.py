#!/usr/bin/env python
# vim: set fileencoding=utf-8 ts=4 sw=4 tw=79 :

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from selenium import webdriver

import unittest
import subprocess
import glob
import importlib
import os.path
import sys
import distutils.spawn
import appengine_config as _


def insert_appengine_path():
    """Find the realpath where dev_appserver.py located, and add it to
    sys.path.

    NOTE: this should work on OS X and Linux.
    """
    dev_appserver = distutils.spawn.find_executable('dev_appserver.py')
    realpath = os.path.realpath(dev_appserver)
    appengine_path = os.path.dirname(realpath)
    sys.path.insert(0, appengine_path)
    for directory in glob.glob(os.path.join(appengine_path, 'lib/*')):
        sys.path.insert(0, directory)

insert_appengine_path()

class NonLoginUserTest(unittest.TestCase):
    def setUp(self):
        self.dev_appserver = subprocess.Popen(['dev_appserver.py', '.'])
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(5)

    def tearDown(self):
        self.browser.quit()
        self.dev_appserver.kill()
        self.dev_appserver.wait()


    def test_non_login_user_can_access_most_pages(self):
        self.browser.get('http://localhost:8080')
        self.assertIn('V2EX', self.browser.title)

        self.browser.get('http://localhost:8080/signup')
        self.assertIn('V2EX', self.browser.title)


class BasicTest(unittest.TestCase):
    def test_collect_urls(self):
        """Ensure all python files at the top level directory defined
        `application` variable.

        NOTE: maybe also test there are no url router defined in any non top
        level directories?
        """
        for pyfile in glob.glob("*.py"):
            if not pyfile.endswith('_test.py'):
                importlib.import_module(os.path.splitext(pyfile)[0],
                                        'application')
