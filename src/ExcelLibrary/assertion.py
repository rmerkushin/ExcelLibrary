# -*- encoding: utf-8 -*-
# Copyright (c) 2013 Roman Merkushin
# rmerkushin@ya.ru


class Assertion(object):

    def cell_value_should_be(self, sheet, row, column, value):
        """
        Check if value returned from cell is equal to the content submitted.
        If cell value and defined content is not equal, then this will throw an AssertionError.
        Sheets, rows and columns index start at 0.\n
        Example usage:
        | Cell Value Should Be | 0 | 1 | 1 | Anna |
        """
        cell_value = self.read_cell(sheet, row, column)
        if cell_value == value:
            print "Cell have expected value : '%s'." % value
        else:
            raise AssertionError("Expected to have cell value equal to '%s' "
                                    "but it is : '%s'." % (value, cell_value))

    def cell_should_contain(self, sheet, row, column, value):
        """
        Check if value returned from cell is contain submitted content.
        If cell value not contain defined content, then this will throw an AssertionError.
        Sheets, rows and columns index start at 0.\n
        Example usage:
        | Cell Should Contain | 0 | 1 | 1 | Anna |
        """
        cell_value = self.read_cell(sheet, row, column)
        if value in cell_value:
            print "Cell contain value : '%s'" % value
        else:
            raise AssertionError("Cell value not contain '%s'." % value)

    def cell_range_should_be(self, sheet, row, start_column, end_column, range_values):
        """
        Check if value returned from cell range is equal to the content submitted.
        If cell range and defined content is not equal, then this will throw an AssertionError.
        Sheets, rows and columns index start at 0. Content values should be written with semicolon delimited.\n
        Example usage:
        | Cell Range Should Be | 0 | 1 | 0 | 2 | Anna;Mary;John; |
        """
        range_string = ""
        for x in range(int(start_column), int(end_column) + 1):
            range_string += self.read_cell(sheet, row, x) + ";"
        if range_string == range_values:
            print "Range cell have expected values : '%s'" % range_values
        else:
            raise AssertionError("Expected to have cell range values : '%s' "
                                    "but it is : '%s'." % (range_values, range_string))

    def cell_range_should_contains(self, sheet, row, start_column, end_column, text):
        """
        Check if value returned from cell range is contains submitted content.
        If cell range not contains defined content, then this will throw an AssertionError.
        Sheets, rows and columns index start at 0.\n
        Example usage:
        | Cell Range Should Contains | 0 | 1 | 0 | 2 | Anna |
        """
        range_string = ""
        for x in range(int(start_column), int(end_column) + 1):
            range_string += self.read_cell(sheet, row, x) + ";"
        if text in range_string:
            print "Range cell contain expected text : '%s'" % text
        else:
            raise AssertionError("Cell range not contains '%s'." % text)
