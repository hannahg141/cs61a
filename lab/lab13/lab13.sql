.read sp17data.sql
.read su17data.sql

CREATE TABLE obedience AS
  select seven, image from students;

CREATE TABLE smallest_int AS
 select time, smallest from students where smallest > 5 order by smallest limit 20;

CREATE TABLE greatstudents AS
  select a.date, a.color, a.pet, a.number, b.number from students as a, sp17students as b where a.color = b.color AND a.pet = b.pet AND a.date = b.date;

CREATE TABLE sevens AS
  select a.seven from students as a, checkboxes as b where a.number = 7 AND b.'7' = "True" AND a.time = b.time;

CREATE TABLE matchmaker AS
  select a.pet, a.beets, a.color, b.color from students as a, students as b where a.pet = b.pet AND a.beets = b.beets AND a.time < b.time;
