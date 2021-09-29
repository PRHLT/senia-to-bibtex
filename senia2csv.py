import cx_Oracle
import csv
import argparse


def export_journals(file_name, c):
    csv_file = open(file_name, 'w')
    writer = csv.writer(csv_file, delimiter=',', lineterminator="\n",
                        quoting=csv.QUOTE_NONNUMERIC)
    c.execute('select * from SENIA_CENTROS.VTSEN_ELC_ARTICULO_PRHLT'
              + 'order by ELC_ID DESC')
    writer.writerow(row[0] for row in c.description)
    for row in c:
        writer.writerow(row)
    csv_file.close()


def export_proceedings(file_name, c):
    csv_file = open(file_name, 'w')
    writer = csv.writer(csv_file, delimiter=',', lineterminator="\n",
                        quoting=csv.QUOTE_NONNUMERIC)
    c.execute('select * from SENIA_CENTROS.VTSEN_PARTICIP_CONGRESO_PRHLT'
              + 'order by ELC_ID DESC')
    writer.writerow(row[0] for row in c.description)
    for row in c:
        writer.writerow(row)
    csv_file.close()


def export_thesis(file_name, c):
    csv_file = open(file_name, 'w')
    writer = csv.writer(csv_file, delimiter=',', lineterminator="\n",
                        quoting=csv.QUOTE_NONNUMERIC)
    c.execute('select * from SENIA_CENTROS.VTSEN_ELC_TESIS_PRHLT'
              + 'order by ELC_ID DESC')
    writer.writerow(row[0] for row in c.description)
    for row in c:
        writer.writerow(row)
    csv_file.close()


def export_books(file_name, c):
    csv_file = open(file_name, 'w')
    writer = csv.writer(csv_file, delimiter=',', lineterminator="\n",
                        quoting=csv.QUOTE_NONNUMERIC)
    c.execute('select * from SENIA_CENTROS.VTSEN_ELC_LIBRO_PRHLT'
              + 'order by ELC_ID DESC')
    writer.writerow(row[0] for row in c.description)
    for row in c:
        writer.writerow(row)
    csv_file.close()


def export_chapters(file_name, c):
    csv_file = open(file_name, 'w')
    writer = csv.writer(csv_file, delimiter=',', lineterminator="\n",
                        quoting=csv.QUOTE_NONNUMERIC)
    c.execute('select * from SENIA_CENTROS.VTSEN_ELC_CAPITULO_PRHLT'
              + 'order by ELC_ID DESC')
    writer.writerow(row[0] for row in c.description)
    for row in c:
        writer.writerow(row)
    csv_file.close()


def parse_args():
    parser = argparse.ArgumentParser(description='This script queries Senia \
                                     to obtain the publications of the \
                                     selected categories and generates a\
                                     csv file per category.')
    parser.add_argument('-b', '--books', metavar='books_csv',
                        help='csv in which to store the book database.')
    parser.add_argument('-c', '--chapters', metavar='chapters_csv',
                        help='csv in which to store the chapters database.')
    parser.add_argument('-p', '--proceedings', metavar='proceedings_csv',
                        help='csv in which to store the conference \
                        proocedings database.')
    parser.add_argument('-j', '--journals', metavar='journals_csv',
                        help='csv in which to store the journals database.')
    parser.add_argument('-t', '--thesis', metavar='thesis_csv',
                        help='csv in which to store the thesis database.')
    parser.add_argument('-o', '--host', metavar='host_ip',
                        required=True, help='Host IP/DNS address.')
    parser.add_argument('-r', '--port', metavar='port',
                        required=True, help='Port number.')
    parser.add_argument('-u', '--username', metavar='username',
                        required=True, help='Your Senia username.')
    parser.add_argument('-s', '--password', metavar='password',
                        required=True, help='Your Senia password.')

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    # Connect to database
    dsn_tns = cx_Oracle.makedsn(args.host, args.port, service_name='ALF')
    conn = cx_Oracle.connect(args.username, args.password, dsn_tns)

    c = conn.cursor()

    if args.journals is not None:
        export_journals(args.journals, c)

    if args.proocedings is not None:
        export_proceedings(args.proceedings, c)

    if args.thesis is not None:
        export_thesis(args.thesis, c)

    if args.books is not None:
        export_books(args.books, c)

    if args.chapters is not None:
        export_chapters(args.chapters, c)

    c.close()
    conn.close()
