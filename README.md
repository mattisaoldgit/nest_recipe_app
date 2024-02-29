# nest_recipe_app
Nest's Recipe Code

This is the proof of concept code at the start.

You will need the latest version of Django and its been created with Python 3.8

# Intro
So the idea is that with Django you can build apps and just plug them in. 

The requirement at the start is to allow the input of recipes and meet all
the requirements around uid, name, quantity, unit and type. You can see the 
DB sections in the migrations.

# Whats left!
A LOT!

This is just ripped of bits of various code cobbled together to do a proof of concept.

What is needed:
* food_items App building out with all the items (import from SpreadSheet)
* Unit convertor to solve... 5 banans or 200g of bananas, its nuts!
* A decent GUI, this is just raw HTML
* Recipe App needs a lot of love, need to be able to query, edit and delete better
* User login system (we can use a off-the-shelf django user admin addon for this)
* Event Page, so that each user can create an event and add recipes to it and be able to edit numbers, meal times, etc
* Some sort of export of the event page, so ppl can print it out
* Some sort of export of the reciepe page as well

Lots of other future stuff, like API's



The are 3 main Apps so far

# recipe_sharing_platform
Main App

# recipes
No shock that this is the recipe App

# food_items
This is the actual items and it is pulled into recipes form

