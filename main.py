"""
An app for logging watched films and saving notes, quotes, timestamps, and stills.

classes:
- film library
    - film object
        - memos
"""


class Memo:
    def __init__(self, title, start_time, end_time, quotation, notes, themes):
        self.title = title
        self.start_time = start_time
        self.end_time = end_time
        self.quotation = quotation
        self.notes = notes
        self.themes = themes

class Film:
    def __init__(self, title, year, status, director=None, language=None, location=None, genre=None,
                 memos=None, tags=None, imdb_id=None):
        self.title = title
        self.year = year
        self.status = status
        self.director = director
        self.language = language
        self.location = location
        self.genre = genre
        self.memos = memos if memos else []
        self.tags = tags if tags else []
        self.imdb_id = imdb_id

    def add_memo(self):
        start_time = input("Timestamp Start: ")
        end_time = input("Timestamp End: ")
        quotation = input("Quotation: ")
        notes = input("Notes: ")
        themes = input("Themes (comma-separated): ").split(',')
        title = input("Memo Name: ")

        memo = Memo(title, start_time, end_time, quotation, notes, themes)
        self.memos.append(memo)

        return f"{memo.title}:\n{memo.themes}\n{memo.start_time} - {memo.end_time}\n{memo.quotation}\n{memo.notes}"

    def __str__(self):
        return f"{self.title} ({self.year}) - {'seen' if self.status else 'watchlist'}"


new_film = Film("Ponyo", 2008, True)
print(new_film)
new_memo = new_film.add_memo()
print(new_memo)
