#!/usr/bin/env python
# vim: set fileencoding=utf-8 ts=4 sw=4 tw=79 :

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import glob
import os
import sys

def add_wheelhouse(path):
    for wheel in glob.glob(os.path.join(path, "*.whl")):
        sys.path.append(wheel)

wheelhouse = os.path.join(os.path.dirname(__file__), "wheelhouse")
add_wheelhouse(wheelhouse)

def webapp_django_setup():
    pass
