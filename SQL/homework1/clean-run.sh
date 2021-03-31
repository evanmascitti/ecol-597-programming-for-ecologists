Problem 2a 

sqlite3

.mode csv

.import tNumber.csv tNumber

.save tNumber.db

.exit

-- Now read the .db file using SQLite

sqlite3
.open tNumber.db

-- check that the table is in there 

.tables

-- send output to a text file
-- turn headers on 

.header on
.output prob2a.txt

-- show schema and the head/tail of the table
.schema tNumber
SELECT * FROM tNumber ORDER BY IDOTU LIMIT 6;
SELECT * FROM tNumber ORDER BY IDOTU DESC LIMIT 6;

.quit


_____

Problem 2b

sqlite3

CREATE TABLE tSPP(
  IDSpp INTEGER PRIMARY KEY AUTOINCREMENT,
  Spp TEXT
  );
```

.mode csv
.import tSPP-no-header.csv tSPP
INSERT INTO tSPP VALUES(NULL, 'Amitermes floridensis');

.mode column
.header on

.output prob2b.txt

SELECT * FROM tSPP;
.quit

____

Problem 2c

sqlite3

CREATE TABLE tOTU(
  IDOTU INTEGER PRIMARY KEY AUTOINCREMENT,
  OTU TEXT
);

.mode csv
.import tOTU-no-header.csv tOTU

.header on

.output problem2c.txt
SELECT * FROM tOTU ORDER BY IDOTU LIMIT 6;
SELECT * FROM tOTU ORDER BY IDOTU DESC LIMIT 6;
.exit


sqlite3

CREATE TABLE tOTU(
  IDOTU INTEGER PRIMARY KEY AUTOINCREMENT,
  OTU TEXT
);

.mode csv
.import tOTU-no-header.csv tOTU

.save Mikaelyan_et_al_2015_data.db
.save Mikaelyan_et_al_2015_data.sql

.exit

