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
