# Project 03

### Summary
Given any FASTA file, this program will split the file into several piece of subfiles. Every subfiles won't contain more than 5,000 sequences and will be analyzed by 'blastp' program with the given database. Afterward this program will generate a summary table which would show the name of matches proteins and the total number of alignments matches for that protein.

### Usage
```
sh doBatchBlast.srun [query file] [database name]
```

### Prerequisite
* Unix system

* blast 2.7.1+

### Output
  * #### File

  &nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp; **summary.out** :

  &nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp; **blast.out** : A tab-delimited table of blast results, which contains:
  1.	Query accession
  2.	Subject accession
  3.	Subject title
  4.	Percent identity
  5.	Alignment length
  6.	Number of mismatches
  7.	Number of gap openings
  8.	Start of alignment in query
  9.	End of alignment in query
  10.	Start of alignment in subject
  11.	End of alignment in subject
  12.	Expect value
  13.	Bitscore

  &nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp; **doBatchBlast.err** : A place where error messages are stored

  &nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp; **doBatchBlast.out** : A place where log message are stored. Users can track the progress from this file as shown below:

  ```
  Getting arguments ...
  Splitting files...
  Running BLAST...
  Processing seq_10 file...
  ```


  * #### Directory
  &nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp;  **splitFSA**: The split query files will be placed here

  &nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp;  **splitOut**: The blast result of each query files will be generated here
