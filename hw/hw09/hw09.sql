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
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
create table size_of_dogs as
select name, size from dogs, sizes where min < height and height <= max;


-- All dogs with parents ordered by decreasing height of their parent
create table by_height as
select child from parents, dogs where parent = name order by -height;


-- Sentences about siblings that are the same size
create table sentences as
  with siblings(first, second, f_size, s_size) as (
    select a.child, b.child, c.size, d.size from parents as a, parents as b, size_of_dogs as c, size_of_dogs as d
    where a.parent = b.parent and a.child != b.child and a.child = c.name and b.child = d.name
  )
select first || ' and ' || second || ' are ' || f_size || ' siblings' from siblings where f_size = s_size order by first limit 2;


-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
create table stacks as
  with additional(dogs, total, num_dogs, tallest) as (
    select name, height, 1, height from dogs union
    select dogs || ', ' || name, total + height, num_dogs + 1, height from additional, dogs where num_dogs < 4 and tallest < height
  )
select dogs, total from additional where total >= 170 order by total;


create table tallest as
select height, name from dogs group by height/10 having max(height) limit 3;


-- All non-parent relations ordered by height difference
create table non_parents as
select "REPLACE THIS LINE WITH YOUR SOLUTION";
