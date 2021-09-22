#!/usr/bin/env python
import pandas as pd
import argparse
from entries import Book


def author_name(name, id, members):
    if members is not None and id in members.keys():
        return members[id]
    return name


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

    output.close()
