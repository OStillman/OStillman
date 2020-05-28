import unittest
from os import path
import sys

sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from app import app

class BasicTestCase(unittest.TestCase):

    def test_index_reachable(self):
        self.tester = app.test_client(self)
        self.response = self.tester.get('/', content_type='html/text')
        self.assertEqual(self.response.status_code, 200)

    def test_database_reachable(self):
        tester = path.exists("DB/ostillman.db")
        self.assertEqual(tester, True)

class FunctionalityTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
    
    def test_index_title(self):
        rv = self.app.get('/')
        assert b'Owen Stillman' in rv.data


if __name__ == '__main__':
    unittest.main()