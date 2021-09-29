# Senia to BibTex
This repository contains tools for generating a BibTex file from [UPV](www.upv.es)'s *Senia* database.

## CSV generation

## BibTex generation
Given the csv files obtained from the previous step, you can generate a BibTex file with the publications from all the desired categories as follows:

```
setobib.py [-h] [-b books_csv] [-c chapters_csv] [-p proceedings_csv]
                  [-j journals_csv] [-t thesis_csv] [-m members_list]
                  [-o output_file]

This script reads one or more csv files from Senia and generates a BibTex file.

optional arguments:
  -h, --help            show this help message and exit
  -b books_csv, --books books_csv
                        csv containing the book database.
  -c chapters_csv, --chapters chapters_csv
                        csv containing the chapters database.
  -p proceedings_csv, --proceedings proceedings_csv
                        csv containing the conference proocedings database.
  -j journals_csv, --journals journals_csv
                        csv containing the journals database.
  -t thesis_csv, --thesis thesis_csv
                        csv containing the thesis database.
  -m members_list, --members members_list
                        csv containing the thesis database.
  -o output_file, --output output_file
                        Output file. (Default: publications.bib).

```

where `members_list` is a list containing a *Senia*'s author id and the desire name you want to give them (to correct the name discrepancies present in *Senia*). Here's an example of how this file should look like:

```
001 Jane Doe
002 John Doe
```
