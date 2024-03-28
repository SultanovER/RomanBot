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
        self.cursor.execute("DROP TABLE IF EXISTS bands")
        self.db.commit()

    def create_tables(self): 
        self.cursor.execute( 
            """ 
            CREATE TABLE IF NOT EXISTS bands ( 
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                band TEXT,
                genre TEXT
            )
            """
        ) 
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS albums ( 
                id INTEGER PRIMARY KEY AUTOINCREMENT,  
                album TEXT,
                genre TEXT,
                year_of_issue INTEGER,
                band_id INTEGER,
                FOREIGN KEY (band_id) REFERENCES bands(id)
            ) 
            """ 

        )
        self.db.commit() 

    def populate_tables(self):
        self.cursor.execute(
            """
            INSERT INTO bands (band, genre)
            VALUES ('NIRVANA', 'гранж'), ('Гражданская Оборона', 'Сибирский андеграунд'), ('Король и Шут', 'панк-рок?'), ('Кино', 'пост-панк')
            """
        )
        self.cursor.execute( 
            """ 
            INSERT INTO albums (album, genre, year_of_issue, band_id)   
                VALUES ('NEVERMIND', 'гранж', 1991, 1), 
                ('Bleach', 'гранж', 1989, 1),
                ('Герои и Злодеи', 'панк-рок?', 2000, 3),
                ('Так закалялась сталь', 'Сибирский андеграунд', 1988, 2),
                ('Сулейман Стальский', 'панк', 1988, 2),
                ('Чёрный альбом', 'пост-панк', 1991, 4),
                ('Неизвестные песни', 'пост-панк', 1992, 4),
                ('Оптимизм', 'Сибирский андеграунд', 1986, 2)
            """ 
        ) 
        self.db.commit()

    def select_groups(self):
        self.cursor.execute("SELECT * FROM bands")
        return self.cursor.fetchall()

    def select_albums(self):
        self.cursor.execute("SELECT * FROM albums")
        return self.cursor.fetchall()

if __name__ == "__main__":
    db = Database()
    db.drop_tables()
    db.create_tables()
    db.populate_tables()
    #pprint(db.get_all_albums())
    #for album in db.get_all_albums():
    #    pprint("Альбом: ", album[2], "Группа: ", album[1], "Год выпуска: ", album[4])
