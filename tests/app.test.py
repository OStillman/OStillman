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

class DatabaseEntries(unittest.TestCase):
    '''
        Test = Database content fetched as desired
        Expected:
            1) All records fetched
            2) Output
            3) All elements are output
    '''

    def setUp(self):
        self.app = app.test_client()
        self.db = sqlite3.connect('DB/ostillman.db')
        self.cursor = self.db.cursor()
        self.entries_count = self.cursor.execute('''select COUNT(id) from entry''').fetchone()[0]
        self.entry_singular = self.cursor.execute('''select * from entry''').fetchone()
        self.rv = self.app.get('/')

    def test_records_exists(self):
        """Records Class Reachable?"""
        assert hasattr(db, 'Records')

    def test_all_records_fetchable(self):
        """Records output from db.Records match length"""
        self.Records = db.Records()
        assert len(self.Records.all_records["Entries"]["Data"]) == self.entries_count


    def test_all_records_output(self):
        """Records carried over to HTML"""
        assert len(re.findall("record", self.rv.data.decode("utf-8"))) == self.entries_count

    def test_record_correctly_rendered(self):
        """Record info output to HTML"""
        data = self.rv.data.decode("utf-8")
        assert self.entry_singular[1] in data
        assert self.entry_singular[2] in data
        assert self.entry_singular[3] in data

    def test_type_rendering(self):
        """Type of H/W"""
        data = self.rv.data.decode("utf-8")
        if len(self.cursor.execute('''SELECT COUNT(id) FROM entry WHERE type = "H"''').fetchall()) > 0:
            assert "hobby" in data
        if len(self.cursor.execute('''SELECT COUNT(id) FROM entry WHERE type = "W"''').fetchall()) > 0:
            assert "work" in data

    def test_bio_fetch(self):
        """Correct Bio Fetch?"""
        fetched_bio = self.cursor.execute('''SELECT Body FROM data WHERE name = ?''', ("Bio",)).fetchone()[0]
        Bio = db.Bio()
        assert fetched_bio in Bio.bio

    def test_bio_output(self):
        """Bio Output?"""
        data = self.rv.data.decode("utf-8")
        bio = self.cursor.execute('''SELECT Body FROM data WHERE name = ?''', ("Bio",)).fetchone()[0]
        assert bio in data

    def test_name_fetch(self):
        """Correct Name Fetch?"""
        fetched_name = self.cursor.execute('''SELECT Body FROM data WHERE name = ?''', ("Name",)).fetchone()[0]
        Name = db.Name()
        print(Name.name)
        assert fetched_name in Name.name

    def test_name_output(self):
        """Name Output?"""
        data = self.rv.data.decode("utf-8")
        bio = self.cursor.execute('''SELECT Body FROM data WHERE name = ?''', ("Name",)).fetchone()[0]
        assert bio in data        
        

    def tearDown(self):
        self.db.close()

        

if __name__ == '__main__':
    unittest.main(verbosity=1)