#!/usr/bin/env python

import unittest, sys

sys.path.append('..')
import extract

class TestHeredocStringFunction(unittest.TestCase):
    def test_no_gettext(self):
        self.assertEqual(extract.search_heredoc_string('testtesttest'), [])

    def test_with_just_gettext(self):
        self.assertEqual(extract.search_heredoc_string("{$_('yo')}"), ['yo'])

    def test_mixed_gettext_and_plaintext(self):
        self.assertEqual(extract.search_heredoc_string("foo {$_('yo')} bar"), ['yo'])

    def test_multiple_gettext_and_plaintext(self):
        self.assertEqual(extract.search_heredoc_string("{$_('foo')} {$_('yo')} bar"), ['foo', 'yo'])

class TestParsingPHPFile(unittest.TestCase):
    def test_php_1(self):
        self.assertEqual(extract.check_file('data/php_1.php'), ['blue', 'red', 'green'])

if __name__ == '__main__':
    unittest.main()
