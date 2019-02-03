create table pizzas as
  select "Pizzahhh" as name, 12 as open, 15 as close union
  select "La Val's"        , 11        , 22          union
  select "Sliver"          , 11        , 20          union
  select "Cheeseboard"     , 16        , 23          union
  select "Emilia's"        , 13        , 18;

create table meals as
  select "breakfast" as meal, 11 as time union
  select "lunch"            , 13         union
  select "dinner"           , 19         union
  select "snack"            , 22;

-- Two meals at the same place
create table double as
select first_meal.meal, second_meal.meal, name from pizzas, meals as first_meal, meals as second_meal
      where first_meal.time != second_meal.time and first_meal.time + 6 < second_meal.time;

-- Pizza options for every meal
create table options as
  with helper(food, total, places, prev, t) as (
   select meal, 1, name, name, time from pizzas, meals where time >= open and time < close union
   select food, total + 1, name || ', ' || places, name, t from helper, pizzas, meals
          where t >= open and t < close and prev > name
   )
   select food as meal, max(total), places from helper group by food order by t;
