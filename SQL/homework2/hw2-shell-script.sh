# start sqlite3 and set some options 

```bash
cd SQL/homework2

sqlite3;
.echo on
.trace
.header on
.mode column
```

# 1a
.open lohr_and_haag.db


.once prob1a.txt
SELECT pop, MIN(afr), MAX(afr), AVG(afr) 
  FROM lohr_and_haag 
  GROUP BY pop;
```

# 1b

```SQL
.once prob1b.txt
SELECT pop, COUNT(pop) AS numInd 
  FROM lohr_and_haag 
  WHERE ad > 55 GROUP BY pop;
```

# 2a

```SQL
# open database 
.open Mikaelyan_et_al_2015.db

# ouput schema 
.once prob2a.txt
.schema
```

# 2b

```SQL
.output prob2b.txt
SELECT Spp, OTU, Num FROM tNumber 
  INNER JOIN tOTU 
    ON tNumber."IDOTU" = tOTU."IDOTU" 
  INNER JOIN tSpp
    ON tNumber."IDSpp" = tSpp."IDSpp"
  LIMIT 10;
.output
```

# 2c 

```SQL
.once prob2c.txt
CREATE VIEW IF NOT EXISTS summary AS SELECT Spp, OTU, Num 
  FROM tNumber 
  INNER JOIN tOTU 
    ON tNumber."IDOTU" = tOTU."IDOTU" 
  INNER JOIN tSpp
    ON tNumber."IDSpp" = tSpp."IDSpp";

# save as new database just in case 
.save summary.db
```

# 2d

```SQL
.once prob2d.txt
SELECT Spp, COUNT(DISTINCT(OTU)) AS "NumOTU" 
  FROM summary 
  WHERE Num > 0
  GROUP BY Spp
  ORDER BY NumOTU DESC;

```

# 2e 

.once prob2e.txt
SELECT OTU, COUNT(Num) AS "NumSpp" 
  FROM summary
  WHERE Num > 0
  GROUP BY OTU
  HAVING NumSpp >= 7;
  

# 2f 

.once prob2f.txt
SELECT Spp, MIN(Num), MAX(Num), AVG(Num) 
  FROM summary
  WHERE Spp LIKE "Nasutiterm%" AND Num> 0
  GROUP BY Spp;
