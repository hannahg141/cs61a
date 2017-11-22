-------------------------------------------------------------
                                                   -- DOGS --
-------------------------------------------------------------

create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";

create table dogs as
  select "abraham" as name, "long" as fur, 26 as height union
  select "barack"         , "short"      , 52           union
  select "clinton"        , "long"       , 47           union
  select "delano"         , "long"       , 46           union
  select "eisenhower"     , "short"      , 35           union
  select "fillmore"       , "curly"      , 32           union
  select "grover"         , "short"      , 28           union
  select "herbert"        , "curly"      , 31;

create table sizes as
  select "toy" as size, 24 as min, 28 as max union
  select "mini",        28,        35        union
  select "medium",      35,        45        union
  select "standard",    45,        60;

-------------------------------------------------------------
    -- PLEASE DO NOT CHANGE ANY DOG TABLES ABOVE THIS LINE --
-------------------------------------------------------------

-- -- The size of each dog
create table size_of_dogs as
  select a.name, b.size from dogs as a, sizes as b where b.min < a.height and b.max >= a.height;

-- All dogs with parents ordered by decreasing height of their parent
create table by_height as
  select a.child from parents as a, dogs as b where a.parent = b.name order by - b.height;
  -- select a.child, from parents as a, dogs as b order by b.height;

-- Sentences about siblings that are the same size
create table sentences as 
WITH helper as (select distinct a.child as name1, b.child as name2, c.size as size1, f.size as size2, d.height as height1, e.height as height2
    from parents as a, parents as b, sizes as c, dogs as d, dogs as e, sizes as f
    where a.parent = b.parent AND a.child != b.child AND a.child < b.child AND a.child = d.name AND b.child = e.name
        AND c.min < d.height AND d.height <= c.max AND f.min < e.height AND e.height <= f.max
)
  select name1 || " and " || name2 || " are " || size1 || " siblings" from helper where size1 = size2;
  
-- Heights and names of dogs that are above average in height among
-- dogs whose height has the same first digit.
create table above_average as
  WITH averages(average, top) as 
  (select avg(height), height / 10 
    from dogs 
    group by height / 10)
    
  select height, name from averages, dogs 
  where height > average and height / 10 = top order by height desc;

-- create table above_average as
--   with hs(ave, h) as 
-- (select avg(height), height/10 
--   from dogs
--    group by height/10)
--   select height, name 
-- from dogs, hs 
-- where height > ave and height/10 = h order by height desc;
-------------------------------------------------------------
                                     -- EUCLID CAFE TYCOON --
-------------------------------------------------------------

-- Locations of each cafe
create table cafes as
  select "nefeli" as name, 2 as location union
  select "brewed"        , 8             union
  select "hummingbird"   , 6;

-- Menu items at each cafe
create table menus as
  select "nefeli" as cafe, "espresso" as item union
  select "nefeli"        , "bagels"           union
  select "brewed"        , "coffee"           union
  select "brewed"        , "bagels"           union
  select "brewed"        , "muffins"          union
  select "hummingbird"   , "muffins"          union
  select "hummingbird"   , "eggs";

-- All locations on the block
create table locations as
  select 1 as n union
  select 2      union
  select 3      union
  select 4      union
  select 5      union
  select 6      union
  select 7      union
  select 8      union
  select 9      union
  select 10;

-------------------------------------------------------------
   -- PLEASE DO NOT CHANGE ANY CAFE TABLES ABOVE THIS LINE --
-------------------------------------------------------------

-- Locations without a cafe
create table open_locations as
  select n from locations, cafes group by n having min(abs(n - location)) > 0;


-- Items that could be placed on a menu at an open location
create table allowed as
  with item_locations(item, location) as (
    select item, location from cafes, menus where name = cafe
  )
  select n, item from item_locations, locations
  group by n, item 
  having min(abs(n - location)) > 2; --if there is an exact copy within 2 of us we get rid of it



