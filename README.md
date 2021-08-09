# a maykinmedia project for fetching data and checking duplicate

Respective python and Django versions are mentioned in the requirements.txt
<br>

The core of the project fetch the csv files through http authentication and then check for valid city names and hotels names, afterward look for duplicate names in both,
<br>
Finally, it will get all the data from database and then turn it into sets and check for duplicates so that we have unique values to save into the database after every interval.
<br>
Once we have unique items we will proceed to enter those into the database.

To run the project simply,
Copy it in location wherever you want, make sure Python and Django are installed then use the command,
<br>
Python manage.py runserver 0.0.0.0:80
It will start the Django development server on 127.0.0.1 <br>
You can check URL: http://127.0.0.1/maykinapp/ to view the hotels by city selection <br>
Call following url to start the corn job http://127.0.0.1/maykinapp/startcornjob
<br>
It’s a basic demonstration of Django project please feel free to ask how to improve it or add extra things such as test, bootstrap, ajax as I could not get much time to put these things in.

