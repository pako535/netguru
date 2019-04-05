## How to run
I recommend creating a virtual environment
* Linux 
``python3 -m venv /path/to/new/virtual/environment``
* Windows
``python -m venv c:\path\to\myenv``

Install required packages from requirements.txt
``pip install -r requirements.txt``

Create database and migrate
* Linix ``python3 manage.py migrate``
* Windows ``python manage.py migrate``

Run localhost
* Linix ``python3 manage.py runserver``
* Windows ``python manage.py runserver``

## Online version
Application is available online [here](http://netguru.bielpawel.pl/) on my private hosting.

## Librares and database
I used three libraries for this project:
* django==2.2 (I don't think, that I need to explain why I used the django framework)
* djangorestframework==3.9.2 (The most popular library/framework to creating REST API in Django.
 Is a powerful and flexible toolkit for building Web APIs)
* requests==2.21.0 (Requests is an HTTP library, written in Python. I needed some library to get data from external api.)

I think that for such a simple and small one does not need a better database.
The principle of using this database from another (from the django level) does not differ too much, because we use django ORM anyway.

How we can read in django documentation.
"SQLite provides an excellent development alternative for applications 
that are predominantly read-only or require a smaller installation footprint." 

## How to use
* `GET /Movies/` - Displays the list of all movies full object already present in application database. 
You can ordering by any movie field. [How to?](https://www.django-rest-framework.org/api-guide/filtering/#orderingfilter)
* `​POST /movies` - Based on passed title, where title is validated, other movie details fetched from http://www.omdbapi.com/
 (or other similar, public movie database) - and saved to application database.
 Response include full movie object.
 * `GET /comments` - It fetch list of all comments present in application database. 
  If you add the `movie_id` parameter to url, the application should return all comments to the selected movie.
  For eg.`comments/?movie_id=1`
* `POST /comments` - To add comment to movie you must to pass `content` and `movie_id` in request.
* `GET /top` - Return top movies already present in the database ranking based on a number of 
comments added to the movie (as in the example) in the specified date range. 
To set range, add the `start_date` and `end_date` parameter to url, the application should return all movies from range.
 For eg.`top/?start_date=0&end_date=2020`

###### Post Scriptum:

I know that the date range w `/top` I could solve using the `rest_framework.filters` and 
I know that the test coverage is not 100% and does not test all functionalities.

