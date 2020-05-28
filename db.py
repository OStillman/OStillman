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
        self.cursor.execute(''' SELECT * FROM entry''')
        self.all_records = self.cursor.fetchall()

    def sortEntries(self):
        all_entries = {"Entries": {"Data": []}}
        for entry in self.all_records:
            all_entries["Entries"]["Data"].append({"title": entry[1], "desc": entry[2], "year": entry[3], "type": entry[4]})
        self.all_records = all_entries
