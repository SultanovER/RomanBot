import sqlite3
from pathlib import Path
from pprint import pprint

class Database:
    def __init__(self) -> None:
        db_path = Path(__file__).parent.parent / "database.sqlite"
        self.db = sqlite3.connect(db_path)
        self.cursor = self.db.cursor()

    def drop_tables(self):
        self.cursor.execute("DROP TABLE IF EXISTS albums")
        self.db.commit()

    def create_tables(self): 
        self.cursor.execute( 
            """ 
            CREATE TABLE IF NOT EXISTS albums ( 
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                band TEXT, 
                album TEXT,
                genre TEXT,
                year_of_issue INTEGER
            ) 
            """ 
        ) 
        self.db.commit() 

    def populate_tables(self):
        self.cursor.execute( 
            """ 
            INSERT INTO albums (band, album, genre, year_of_issue)   
                VALUES ('NIRVANA', 'NEVERMIND', 'grunge', 1991), 
                ('Гражданская Оборона', 'Оптимизм', 'Сибирский андеграунд', 1986),
                ('Король и Шут', 'Герои и Злодеи', 'панк-рок', 2000)
            """ 
        ) 
        self.db.commit()

    def get_all_albums(self):
        self.cursor.execute("SELECT * FROM albums")
        return self.cursor.fetchall()

if __name__ == "__main__":
    db = Database()
    db.drop_tables()
    db.create_tables()
    db.populate_tables()
    pprint(db.get_all_albums())
    for album in db.get_all_albums():
        pprint("Альбом: ", album[2], "Группа: ", album[1], "Год выпуска: ", album[4])
