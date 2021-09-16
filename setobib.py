#!/usr/bin/env python
import panda as pd
import argparse


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
    parser.add_argument('-o', '--output', metavar='output_file',
                        default='publications.bib', help='Output file. \
                        (Default: publications.bib).')

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    output = open(args.output, 'r')

    if args.books is not None:
        parse_books(args.books, output)
