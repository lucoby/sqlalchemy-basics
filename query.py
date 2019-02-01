from datetime import date
from actor import Actor
from base import Session
from contact_details import ContactDetails
from movie import Movie


session = Session()

movies = session.query(Movie).all()
print('All movies:')
for movie in movies:
    print('%s was released on %s' % (movie.title, movie.release_date))
print()

movies = session.query(Movie) \
        .filter(Movie.release_date > date(2015, 1, 1)) \
        .all()
print('Recent movies:')
for movie in movies:
    print('%s was released on %s' % (movie.title, movie.release_date))
print()

the_rock_movies = session.query(Movie) \
        .join(Actor, Movie.actors) \
        .filter(Actor.name == 'Dwayne Johnson') \
        .all()
print('Dwayne Johnson movies:')
for movie in the_rock_movies:
    print('The rock starred in %s' % (movie.title))
print()

glendale_stars = session.query(Actor) \
        .join(ContactDetails) \
        .filter(ContactDetails.address.ilike('%glendale%')) \
        .all()
print('Actors that live in Glendale:')
for actor in glendale_stars:
    print('%s has a house in Glendale' % (actor.name))
print()
