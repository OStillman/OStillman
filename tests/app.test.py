import unittest
from os import path
import sys
import sqlite3
import re

sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from app import app
import db

class Reachability(unittest.TestCase):
    '''
        Test = Is everything reachable?
        Expected = Page Reachable, Database Reachable
    '''

    def test_index_reachable(self):
        self.tester = app.test_client(self)
        self.response = self.tester.get('/', content_type='html/text')
        self.assertEqual(self.response.status_code, 200)

    def test_database_reachable(self):
        tester = path.exists("DB/ostillman.db")
        self.assertEqual(tester, True)

class HTMLFetched(unittest.TestCase):
    '''
        Test = HTML page fetched from templates
        Expected = HTML fetched e.g. can see owen stillman title
    '''

    def setUp(self):
        self.app = app.test_client()
    
    def test_index_title(self):
        rv = self.app.get('/')
        assert b'<title> Owen Stillman </title>' in rv.data

class DatabaseContentFetched(unittest.TestCase):
    '''
        Test = Database content fetched as desired
        Expected:
            1) All records fetched
    '''

    def setUp(self):
        self.app = app.test_client()
        self.db = sqlite3.connect('DB/ostillman.db')
        self.cursor = self.db.cursor()

    def test_records_exists(self):
        assert hasattr(db, 'Records')

    def test_all_records_fetchable(self):
        self.Records = db.Records()
        self.entries_count = self.cursor.execute('''select COUNT(id) from entry''').fetchone()
        assert len(self.Records.all_records["Entries"]["Data"]) == self.entries_count[0]

        


    def tearDown(self):
        self.db.close()

        

if __name__ == '__main__':
    unittest.main()