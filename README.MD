# Movie Database Website 🎥🎥🎥

This project demonstrates the basic capabilities of Django framework and Django REST Framework for creating a movie database website.

## Description

Web application with minimal frontend where users can view and edit a list of movies, actors and directors.

Each movie have the following details:
- Title
- Release Date
- List of Directors
- List of Actors

Database population is done through the API from https://www.omdbapi.com/

CRUD operations for Movie, Actor, Director.

Live-demo is available on Render:



## API Endpoints🪝 

- `/api/movies/` (GET, POST)
- `/api/movies/<id>/` (GET, PUT, DELETE)
- `/api/directors/` (GET, POST)
- `/api/directors/<id>/` (GET, PUT, DELETE)
- `/api/actors/` (GET, POST)
- `/api/actors/<id>/` (GET, PUT, DELETE)

## Features ⭐

- CRUD operations for movies
- CRUD operations for actors
- CRUD operations for directors
- Pagination for list views
- Filters for movies, actors, directors (via django_filters) for both frontend and API
- API endpoints for CRUD operations with movies, actors, directors

## Technologies Used 🧑‍💻

- Django Framework
- Django REST Framework
- Django Filters
- SQLite (for development)
- PostgreSQL (for production)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/movie-database.git
   cd movie-database
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Apply migrations:
   ```bash
   python manage.py migrate
   ```
4. Acquire API key for OMBD API:   
https://www.omdbapi.com/apikey.aspx  
And then put it into .env file (see .env-sample for reference)    
    

5. Load data form OMDB API using management command:  
   ```bash
   python manage.py migrate import_movies 80000 81000
    ```
    Note: 80000 and 81000 are range of movies' IMDB IDs, explanation from IMDB below:
   ```bash
   tt0050083 is the unique identifier for the 
   movie "12 Angry Men (1957)", where tt signifies 
   that it's a title entity and 0050083 uniquely 
   indicates "12 Angry Men (1957)"
    ```
6. Run the development server:

   ```bash
    python manage.py runserver
    ```
7. Access the website at http://localhost:8000/
