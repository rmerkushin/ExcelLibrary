# -*- encoding: utf-8 -*-
# Copyright (c) 2013 Roman Merkushin
# rmerkushin@ya.ru

from excel import Excel
from assertion import Assertion

__version__ = "0.1"
__author__ = "Roman Merkushin"


class ExcelLibrary(Excel, Assertion):

    ROBOT_LIBRARY_SCOPE = "GLOBAL"
