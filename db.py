import sqlite3

class Records():
    def __init__(self, all_records=None):
        self.db = sqlite3.connect('DB/ostillman.db')
        self.cursor = self.db.cursor()
        self.query()
        self.sortEntries()
        self.db.close()

    @property
    def all_records(self):
        return self._all_records

    @all_records.setter
    def all_records(self, all_records):
        self._all_records = all_records

    def query(self):
        #print (today, file=sys.stderr)
        self.cursor.execute(''' SELECT * FROM entry ORDER BY year DESC''')
        self.all_records = self.cursor.fetchall()

    def sortEntries(self):
        all_entries = {"Entries": {"Data": []}}
        for entry in self.all_records:
            all_entries["Entries"]["Data"].append({"title": entry[1], "desc": entry[2], "year": entry[3], "type": entry[4]})
        self.all_records = all_entries


class Bio():
    def __init__(self, bio=None):
        self.db = sqlite3.connect('DB/ostillman.db')
        self.cursor = self.db.cursor()
        self.query()
        self.sortBio()
        self.db.close()


    @property
    def bio(self):
        return self._bio

    @bio.setter
    def bio(self, bio):
        self._bio = bio

    def query(self):
        self.bio = self.cursor.execute('''SELECT body FROM data WHERE name = ?''', ("Bio",)).fetchone()[0]

    def sortBio(self):
        self.bio

class Name():
    def __init__(self, name=None):
        self.db = sqlite3.connect('DB/ostillman.db')
        self.cursor = self.db.cursor()
        self.query()
        self.sortName()
        self.db.close()


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def query(self):
        self.name = self.cursor.execute('''SELECT Body FROM data WHERE name = ?''', ("Name",)).fetchone()[0]

    def sortName(self):
        self.name