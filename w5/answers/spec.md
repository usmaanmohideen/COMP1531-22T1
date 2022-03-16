# Tutorial 5 - Solutions

## A. A Simple Server

### Part 1 - The Backend

In `names_ages.py`, write a simple program which:
* Stores a list of dictionaries containing names and ages
* Has a function `add_name_age` that takes in a name and a date of birth, and adds the dictionary {name, age} to the data store
* Has a function `get_names_ages` that returns the list of name-ages
* Has a function `clear_names_ages` that clears the list of name-ages
* Uses a helper function `date_to_age` which converts the date to an age

> See [solutions/names_ages.py](solutions/names_ages.py).

### Part 2 - Server Stubs

Write a simple Flask server that contains corresponding routes for adding names/ages and getting names/ages in `server.py`. The routes should simply be stubs for now.

> See [solutions/server.py](solutions/server.py).

### Part 3 - Failing HTTP Tests

Write a HTTP test for each of your routes inside `names_ages_test.py`. You will need to check:
* The response status code;
* The contents of the return value;

in each of your tests. The tests should fail when you run them.

Once you have done this, complete the implementations of the Flask route wrapper functions. The tests should pass.

* Discuss briefly why clearing the data store using the `.clear()` method works, when simply setting it to `= []` doesn't.

> See [solutions/names_ages_test.py](solutions/names_ages_test.py).

## B. Code Review

1. Your tutor will break up into groups for this activity. Take a look at [this webpage](https://www.youtube.com/watch?v=GfL5zOhpB14). What routes do you think are necessary to allow this webpage to function? For each route:
 * Discuss the data it might take in
 * Discuss the data it might return

Your tutor may provide you with a [hackmd.io](https://hackmd.io) file for everyone to edit together.

> Examples include:
>  * like/dislike
>  * save button
>  * subscribe button
>  * viewing comments (notice how this loads after initial load? Implies API call)
>  * posting comment

> Ones that probably aren't routes include:
>  * share
>  * volume change
>  * full screen

2. Are there any considerations that need to be made when choosing how to breakup routes?

> A balance in how much is captured in one route. For example, should the like/dislike be two routes or one? If they're functionally similar enough it can pay to have them in one route and just have a flag that differs them

## C. Networks

Breakdown the key components of an HTTP URL, such as http://unsw.com/calendar/view?term=t3&week=5#top

> Protocol: HTTP<br />
> Domain: unsw.com<br />
> Path: calendar/view<br />
> Query String: term=t3&week=5<br />
> Anchor: #top<br />

## D. More Flask

1. Add a new route, `edit_name_age` that, given a name and a new date of birth, updates corresponding record. Develop this HTTP test-first by stubbing out the backend function and Flask route, writing the failing test and then implementing to pass the test.

2. Change the `get_names_ages` route and backend method to optionally accept a minimum age, and only returns people who are older than that age. Use the `filter` function in your backend solution.

> See [solutions/server.py](solutions/server.py).

## E. JSON & YAML

* Convert the JSON file [data_1.json](data_1.json) to YAML in [data_1.yml](data_1.yml)
* Convert the YAML file [data_2.yml](data_2.yml) to JSON in [data_2.json](data_2.json)

Of course, you can do this with [simple online tools](https://www.json2yaml.com/). However, we encourage you to try and do this manually because during the exam if we test you on these items you need to be prepared!

> See [data_1.yml](solutions/data_1.yml) and [data_2.json](solutions/data_2.json).
