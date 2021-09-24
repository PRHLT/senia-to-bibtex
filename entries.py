class Thesis:
    def __init__(self, output):
        self._output = output
        self._id = None
        self._year = None
        self._author = None
        self._advisors = []
        self._title = None
        self._school = None

    def get_id(self):
        return self._id

    def add_advisor(self, advisor):
        self._advisors.append(advisor)

    def add_author(self, author):
        self._author = author

    def add_year(self, year):
        self._year = year

    def add_title(self, title):
        self._title = title

    def add_id(self, id):
        self._id = id

    def add_school(self, school):
        self._school = school

    def generate_bib_id(self):
        return self._author.split()[0] + str(self._year)

    def generate_entry(self):
        entry = ('@phdthesis{' + self.generate_bib_id() + ',\n'
                 + 'title = {' + self._title + '},\n'
                 + 'author = {' + self._author + '},\n'
                 + 'year = {' + str(self._year) + '},\n'
                 + 'school = {' + self._school + '},\n'
                 + 'note = {Advisor/s: ' + ' and '.join(self._advisors)
                 + '},\n'
                 + '}\n\n')
        self._output.write(entry)


class Journal:
    def __init__(self, output):
        self._output = output
        self._id = None
        self._year = None
        self._authors = {}
        self._title = None
        self._pages = None
        self._volume = None
        self._number = None
        self._journal = None

    def get_id(self):
        return self._id

    def add_author(self, name, order):
        self._authors[order] = name

    def add_year(self, year):
        self._year = year

    def add_title(self, title):
        self._title = title

    def add_volume(self, volume):
        self._volume = str(volume) if volume != -1 else ''

    def add_number(self, number):
        self._number = str(number) if number != -1 else ''

    def add_journal(self, journal):
        self._journal = journal

    def add_id(self, id):
        self._id = id

    def add_pages(self, start, end):
        if start == -1 or end == -1:
            self._pages = ''
        else:
            self._pages = str(start) + '--' + str(end)

    def get_author_field(self):
        field = ''
        indexes = [k for k in self._authors.keys()]
        indexes.sort()
        counter = 0
        for index in indexes:
            author = self._authors[index]
            if type(author) == str:
                field += author
                if counter + 1 < len(indexes):
                    field += ' and '
            counter += 1
        return field

    def generate_bib_id(self):
        authors = [k for k in self._authors.keys()]
        authors.sort()
        return (self._authors[authors[0]].split()[0].strip(',')
                + str(self._year))

    def generate_entry(self):
        entry = ('@article{' + self.generate_bib_id() + ',\n'
                 + 'title = {' + self._title + '},\n'
                 + 'journal = {' + self._journal + '},\n'
                 + 'author = {' + self.get_author_field() + '},\n'
                 + 'year = {' + str(self._year) + '},\n'
                 + 'pages = {' + self._pages + '},\n'
                 + 'volume = {' + self._volume + '},\n'
                 + 'number = {' + self._number + '}\n'
                 + '}\n\n')
        self._output.write(entry)


class Proceeding:
    def __init__(self, output):
        self._output = output
        self._id = None
        self._year = None
        self._authors = {}
        self._title = None
        self._booktitle = None
        self._pages = None

    def get_id(self):
        return self._id

    def add_author(self, name, order):
        self._authors[order] = name

    def add_year(self, year):
        self._year = year

    def add_title(self, title):
        self._title = title

    def add_booktitle(self, title):
        self._booktitle = title

    def add_id(self, id):
        self._id = id

    def add_pages(self, start, end):
        if start == -1 or end == -1:
            self._pages = ''
        else:
            self._pages = str(start) + '--' + str(end)

    def get_author_field(self):
        field = ''
        indexes = [k for k in self._authors.keys()]
        indexes.sort()
        counter = 0
        for index in indexes:
            author = self._authors[index]
            if type(author) == str:
                field += author
                if counter + 1 < len(indexes):
                    field += ' and '
            counter += 1
        return field

    def generate_bib_id(self):
        authors = [k for k in self._authors.keys()]
        authors.sort()
        return (self._authors[authors[0]].split()[0].strip(',')
                + str(self._year))

    def generate_entry(self):
        entry = ('@inproceedings{' + self.generate_bib_id() + ',\n'
                 + 'title = {' + self._title + '},\n'
                 + 'booktitle = {In proceedings of the '
                 + self._booktitle + '},\n'
                 + 'author = {' + self.get_author_field() + '},\n'
                 + 'year = {' + str(self._year) + '},\n'
                 + 'pages = {' + self._pages + '}\n'
                 + '}\n\n')
        self._output.write(entry)


class Chapter:
    def __init__(self, output):
        self._output = output
        self._id = None
        self._year = None
        self._authors = {}
        self._title = None
        self._isbn = None
        self._publisher = None
        self._pages = None
        self._chapter_title = None

    def get_id(self):
        return self._id

    def add_author(self, name, order):
        self._authors[order] = name

    def add_year(self, year):
        self._year = year

    def add_title(self, title):
        self._title = title

    def add_isbn(self, isbn):
        self._isbn = isbn

    def add_publisher(self, publisher):
        self._publisher = publisher

    def add_id(self, id):
        self._id = id

    def add_chapter_title(self, title):
        self._chapter_title = title

    def add_pages(self, start, end):
        self._pages = str(start) + '--' + str(end)

    def get_author_field(self):
        field = ''
        indexes = [k for k in self._authors.keys()]
        indexes.sort()
        counter = 0
        for index in indexes:
            author = self._authors[index]
            if type(author) == str:
                field += author
                if counter + 1 < len(indexes):
                    field += ' and '
            counter += 1
        return field

    def generate_bib_id(self):
        authors = [k for k in self._authors.keys()]
        authors.sort()
        return (self._authors[authors[0]].split()[0].strip(',')
                + str(self._year))

    def generate_entry(self):
        entry = ('@inbook{' + self.generate_bib_id() + ',\n'
                 + 'title = {' + self._chapter_title + '},\n'
                 + 'booktitle = {' + self._title + '},\n'
                 + 'author = {' + self.get_author_field() + '},\n'
                 + 'year = {' + str(self._year) + '},\n'
                 + 'isbn = {' + self._isbn + '},\n'
                 + 'publisher = {' + self._publisher + '}\n'
                 + 'pages = {' + self._pages + '}\n'
                 + '}\n\n')
        self._output.write(entry)


class Book:
    def __init__(self, output):
        self._output = output
        self._id = None
        self._year = None
        self._authors = {}
        self._title = None
        self._isbn = None
        self._publisher = None

    def get_id(self):
        return self._id

    def add_author(self, name, order):
        self._authors[order] = name

    def add_year(self, year):
        self._year = year

    def add_title(self, title):
        self._title = title

    def add_isbn(self, isbn):
        self._isbn = isbn

    def add_publisher(self, publisher):
        self._publisher = publisher

    def add_id(self, id):
        self._id = id

    def get_author_field(self):
        field = ''
        indexes = [k for k in self._authors.keys()]
        indexes.sort()
        counter = 0
        for index in indexes:
            author = self._authors[index]
            field += author
            if counter + 1 < len(indexes):
                field += ' and '
            counter += 1
        return field

    def generate_bib_id(self):
        authors = [k for k in self._authors.keys()]
        authors.sort()
        return (self._authors[authors[0]].split()[0].strip(',')
                + str(self._year))

    def generate_entry(self):
        entry = ('@book{' + self.generate_bib_id() + ',\n'
                 + 'title = {' + self._title + '},\n'
                 + 'author = {' + self.get_author_field() + '},\n'
                 + 'year = {' + str(self._year) + '},\n'
                 + 'isbn = {' + self._isbn + '},\n'
                 + 'publisher = {' + self._publisher + '}\n'
                 + '}\n\n')
        self._output.write(entry)
