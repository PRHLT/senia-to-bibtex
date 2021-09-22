import cx_Oracle
import csv

host = 'YOUR HOST'
port = 'YOUR PORT'
user = 'YOUR SENIA USER'
password = 'YOUR PASSWORD'

#nos conectamos a la BBDD
dsn_tns = cx_Oracle.makedsn(host, port, service_name='ALF')
conn = cx_Oracle.connect(user, password, dsn_tns)

c = conn.cursor()

csv_file = open("journals.csv", "w")
writer = csv.writer(csv_file, delimiter=',', lineterminator="\n", quoting=csv.QUOTE_NONNUMERIC)
c.execute('select * from SENIA_CENTROS.VTSEN_ELC_ARTICULO_PRHLT order by ELC_ID DESC') # use triple quotes if you want to spread your query across multiple lines
writer.writerow(row[0] for row in c.description)
for row in c:
    writer.writerow(row)
csv_file.close()

csv_file = open("congress.csv", "w")
writer = csv.writer(csv_file, delimiter=',', lineterminator="\n", quoting=csv.QUOTE_NONNUMERIC)
c.execute('select * from SENIA_CENTROS.VTSEN_PARTICIP_CONGRESO_PRHLT order by ELC_ID DESC') # use triple quotes if you want to spread your query across multiple lines
writer.writerow(row[0] for row in c.description)
for row in c:
    writer.writerow(row)
csv_file.close()

csv_file = open("tesis.csv", "w")
writer = csv.writer(csv_file, delimiter=',', lineterminator="\n", quoting=csv.QUOTE_NONNUMERIC)
c.execute('select * from SENIA_CENTROS.VTSEN_ELC_TESIS_PRHLT order by ELC_ID DESC') # use triple quotes if you want to spread your query across multiple lines
writer.writerow(row[0] for row in c.description)
for row in c:
    writer.writerow(row)
csv_file.close()

csv_file = open("book.csv", "w")
writer = csv.writer(csv_file, delimiter=',', lineterminator="\n", quoting=csv.QUOTE_NONNUMERIC)
c.execute('select * from SENIA_CENTROS.VTSEN_ELC_LIBRO_PRHLT order by ELC_ID DESC') # use triple quotes if you want to spread your query across multiple lines
writer.writerow(row[0] for row in c.description)
for row in c:
    writer.writerow(row)
csv_file.close()

csv_file = open("chapter.csv", "w")
writer = csv.writer(csv_file, delimiter=',', lineterminator="\n", quoting=csv.QUOTE_NONNUMERIC)
c.execute('select * from SENIA_CENTROS.VTSEN_ELC_CAPITULO_PRHLT order by ELC_ID DESC') # use triple quotes if you want to spread your query across multiple lines
writer.writerow(row[0] for row in c.description)
for row in c:
    writer.writerow(row)
csv_file.close()

c.close()
conn.close()
