#!/usr/bin/python3
"""The unittests for console"""

import unittest
import console
from console import HBNBCommand


class test_console(unittest.TestCase):
    """The test console class"""

    def create(self):
        """the instance creation"""
        return HBNBCommand()

    def test_quit(self):
        """testing the quit method"""
        the_test = self.create()
        self.assertTrue(the_test.onecmd("quit"))

    def test_EOF(self):
        """testing the EOF method"""
        the_test = self.create()
        self.assertTrue(the_test.onecmd("EOF"))
