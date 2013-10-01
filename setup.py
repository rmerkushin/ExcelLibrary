# -*- encoding: utf-8 -*-

import os
import sys
from distutils.core import setup

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))


def main():
    setup(name="robotframework-excellibrary",
          version="0.1",
          description="Excel library for Robot Framework",
          author="Roman Merkushin",
          author_email="rmerkushin@ya.ru",
          url="https://github.com/rmerkushin/ExcelLibrary",
          package_dir={"": "src"},
          packages=["ExcelLibrary"])


if __name__ == "__main__":
    main()
