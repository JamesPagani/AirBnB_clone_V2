# Web Framework

**This part of the AirBnB clone project doesn't implement anything to the final web page. Rather, it serves as an introduction to Flask, a Python package/library used to develop web applications.

## Contents

### Files

+ 0-hello_route.py: Display a basic string when making a request to `/` (root).
+ 1-hbnb_route.py: Displays another string when making a request to `/hbnb`.
+ 2-c_route.py: Displays a string when making a request to `/c/<text>`. You can add text after the slash to display that text too.
+ 3-pyhton_route.py: Displays a string when making a request to `/python/<text>`. Similar to `2-c_route.py`, but it has a default value.
+ 4-number_route.py: Displays the variable sent to `/number/<number>` ONLY if it is a number.
+ 5-number_template.py: Similar to `4-number_route.py`, but displays a web template instead.
+ 6-number_odd_or_even.py: When making a request to `/number_odd_or_even/<n>`, display a web template if `n` is an integer while also saying if the number is odd or even.
+ 7-states_list.py: Making a request to `/states_list` will display all states stored in the database (DBStorage). 

### Folders

+ templates/: Contains the web templates used in files 5 to 10