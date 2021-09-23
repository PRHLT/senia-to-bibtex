#!/usr/bin/env python
import pandas as pd
import argparse
from entries import Book, Chapter, Proceeding, Journal


def author_name(name, id, members):
    if members is not None and id in members.keys():
        return members[id]
    return name


def parse_journals(journals_db, output, members):
    df = pd.read_csv(journals_db).fillna(-1)
    journals = []
    for index, journal in df.iterrows():
        id = journal['ELC_ID']
        new_journal = True
        for p in journals:
            if id == p.get_id():
                new_journal = False
                p.add_author(author_name(journal['AUT_FIRMANTE'],
                                         journal['AUT_PER_ID'], members),
                             int(journal['AUT_ORDEN']))
        if new_journal:
            j = Journal(output)
            j.add_id(id)
            j.add_year(journal['ART_ANYO'])
            j.add_author(author_name(journal['AUT_FIRMANTE'],
                                     journal['AUT_PER_ID'], members),
                         int(journal['AUT_ORDEN']))
            j.add_title(journal['ART_TITULO'])
            j.add_journal(journal['REV_TITULO'])
            j.add_volume(journal['ART_VOLUMEN'])
            j.add_number(journal['ART_NUMERO'])
            j.add_pages(int(journal['ART_PAGDESDE']),
                        int(journal['ART_PAGHASTA']))
            journals.append(j)

    for journal in journals:
        journal.generate_entry()


def parse_proceedings(conferences_db, output, members):
    df = pd.read_csv(conferences_db).fillna(-1)
    proceedings = []
    for index, proceeding in df.iterrows():
        id = proceeding['ELC_ID']
        new_proceeding = True
        for p in proceedings:
            if id == p.get_id():
                new_proceeding = False
                p.add_author(author_name(proceeding['AUT_FIRMANTE'],
                                         proceeding['AUT_PER_ID'], members),
                             int(proceeding['AUT_ORDEN']))
        if new_proceeding:
            p = Proceeding(output)
            p.add_id(id)
            p.add_year(proceeding['COA_FECHA'].split('-')[0])
            p.add_author(author_name(proceeding['AUT_FIRMANTE'],
                                     proceeding['AUT_PER_ID'], members),
                         int(proceeding['AUT_ORDEN']))
            p.add_title(proceeding['PAC_TITULO'])
            p.add_booktitle(proceeding['COA_TITULO'])
            p.add_pages(int(proceeding['PAC_PAGINI']),
                        int(proceeding['PAC_PAGFIN']))
            proceedings.append(p)

    for proceeding in proceedings:
        proceeding.generate_entry()


def parse_chapters(chapters_db, output, members):
    df = pd.read_csv(chapters_db)
    chapters = []
    for index, chapter in df.iterrows():
        id = chapter['ELC_ID']
        new_chapter = True
        for c in chapters:
            if id == c.get_id():
                new_chapter = False
                c.add_author(author_name(chapter['AUT_FIRMANTE'],
                                         chapter['AUT_PER_ID'], members),
                             int(chapter['AUT_ORDEN']))
        if new_chapter:
            c = Chapter(output)
            c.add_id(id)
            c.add_year(chapter['LIB_ANYO'])
            c.add_author(author_name(chapter['AUT_FIRMANTE'],
                                     chapter['AUT_PER_ID'], members),
                         int(chapter['AUT_ORDEN']))
            c.add_title(chapter['LIB_TITULO'])
            c.add_isbn(chapter['LIB_ISBN'])
            c.add_publisher(chapter['LIB_EDITORIAL'])
            c.add_chapter_title(chapter['CAP_TITULO'])
            c.add_pages(chapter['CAP_PAGINICIO'], chapter['CAP_PAGFIN'])
            chapters.append(c)

    for chapter in chapters:
        chapter.generate_entry()


def parse_books(books_db, output, members):
    df = pd.read_csv(books_db)
    books = []
    for index, book in df.iterrows():
        id = book['ELC_ID']
        new_book = True
        for b in books:
            if id == b.get_id():
                new_book = False
                b.add_author(author_name(book['AUT_FIRMANTE'],
                                         book['AUT_PER_ID'], members),
                             int(book['AUT_ORDEN']))
        if new_book:
            b = Book(output)
            b.add_id(id)
            b.add_year(book['LIB_ANYO'])
            b.add_author(author_name(book['AUT_FIRMANTE'],
                                     book['AUT_PER_ID'], members),
                         int(book['AUT_ORDEN']))
            b.add_title(book['LIB_TITULO'])
            b.add_isbn(book['LIB_ISBN'])
            b.add_publisher(book['LIB_EDITORIAL'])
            books.append(b)

    for book in books:
        book.generate_entry()


def read_members(members_list):
    members = {}
    for member in open(members_list):
        id = member.strip().split()[0]
        name = ' '.join(member.strip().split()[1:])
        members[id] = name
    return members


def parse_args():
    parser = argparse.ArgumentParser(description='This script reads a \
                                     several csv files from Senia and \
                                     generates a BibTex file.')
    parser.add_argument('-b', '--books', metavar='books_csv',
                        help='csv containing the book database.')
    parser.add_argument('-c', '--chapters', metavar='chapters_csv',
                        help='csv containing the chapters database.')
    parser.add_argument('-p', '--proceedings', metavar='proceedings_csv',
                        help='csv containing the conference proocedings \
                        database.')
    parser.add_argument('-j', '--journals', metavar='journals_csv',
                        help='csv containing the journals database.')
    parser.add_argument('-t', '--thesis', metavar='thesis_csv',
                        help='csv containing the thesis database.')
    parser.add_argument('-m', '--members', metavar='members_list',
                        help='csv containing the thesis database.')
    parser.add_argument('-o', '--output', metavar='output_file',
                        default='publications.bib', help='Output file. \
                        (Default: publications.bib).')

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    if args.members is not None:
        members = read_members(args.members)
    else:
        members = None

    output = open(args.output, 'w')

    if args.books is not None:
        parse_books(args.books, output, members)

    if args.chapters is not None:
        parse_chapters(args.chapters, output, members)

    if args.proceedings is not None:
        parse_proceedings(args.proceedings, output, members)

    if args.journals is not None:
        parse_journals(args.journals, output, members)

    output.close()
