# Flight Delay Predictor

Flight Delay Predictor is a web application designed to predict the likelihood of a flight delay

```
https://flightdelaypredictor.herokuapp.com/
```

## Django Code

Django web framework was used after some inital research in which framework would work best for this project.
Shortly after working with this framework it seemed fairly straight forward but as I ran into road blocks I spent more time
troubleshooting implimentation of code as opposed to writing the code.  I may choose another framwork in the future.

I initially thought I might use a database with this project but realized that it was not necessary for simple API
requests and some simple statistical analysis

When the application is called from a web browser the input form view is presented with the form fields set in forms.py.
The user will input airline,flight, and date of travel.  This information is passed to views.py (POST) and the user
information is sorted into variables.   I struggled with tring to get the django date/time picker widget to work
properly.  Tried to parse outhe individual piece of information to add to the API call but no luck.  Instead I had to
break out the individual year, month, day as inidividual inputs to work properly.

The information from the user is then used to make 3 inidividual API request to Flightstats.com.  THe first API call
gathers all the available information about the flight (arrival airport, departure airport, flight number, etc.).
The second and third API call gathers the arrival/departure airport weather conditions.

The JSON data provided from the API calls are then processed with Python code to determine the likely hood of a flight delay.

### HTML

Once the data is processed by the django form it is rendered and returned to the predict_output.html form.   This HTML
template was provided free of use by colorlib.com.  It is a simple form but had the correct format I needed to output my
analysis is a clear/simple format.  Bootstrap and a local style css file provided all the design visuals for the output information.


### Heroku and Herok CLI

Heroku was not my first choice of web application host.  I originally tried the free version of pythonanywhere at the
recommendation of an online Django tutorial I was utilizing.   Pythonanywhere worked well for the tutorial but became cumbersome to
add python packages properly between the virtual environments and the deployed application.  Lots of workaround and wasted time.
Decided to switch to Heroku.  Not the most new user friendly site but I had learned so much trying to fix/repair the site
at pythonanyhere that the instructions of how to deploy a django app were not to bad.  Once I learne dhow to navigate better
with the Heroku CLI it was a lot easier to fix the deployment issues.


##Future

I still need to fine tune the application to use future weather forcasts since some flights today can last up to 16 hours.
The reason I did not try to design/build on the CS50 IDE is because I wish to actually use this for some of my business travel.
More opportunity to test in the real world...and fine tune.


## Author

* **Michael Bliss** - *Initial work* - [goldkn22](https://github.com/goldkn22)



