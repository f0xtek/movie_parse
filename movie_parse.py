#!/usr/bin/env python
import csv
from collections import defaultdict, namedtuple, OrderedDict
import os
import urllib3

MOVIE_DATA = 'https://raw.githubusercontent.com/pybites/challenges/solutions/13/movie_metadata.csv'
MOVIE_CSV = 'movies.csv'
MOVIE_CSV_PATH = f"{os.getcwd()}/{MOVIE_CSV}"
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def download_data_to_csv(url):
    http = urllib3.PoolManager()
    r = http.request('GET', url, preload_content=False)

    with open(MOVIE_CSV_PATH, 'wb') as f:
        while True:
            data = r.read(1024)
            if not data:
                break
            f.write(data)

    r.release_conn()


def get_movies_by_director(data=MOVIE_CSV_PATH):
    directors = defaultdict(list)

    with open(data, encoding='utf-8') as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                # ignore bad data from CSV file
                continue

            m = Movie(title=movie, year=year, score=score)
            if m.year >= MIN_YEAR:
                directors[director].append(m)
    # We're only interested in directors with at least 4 movies
    # convert the output to a defaultdict again to preserve functionality
    return defaultdict(list, {k: v for k, v in directors.items() if len(v) >= 4})


def get_average_scores(directors):
    for director, movies in directors.items():
        directors[director] = sorted(movies, key=lambda x: x.score, reverse=True)
        movies_avg = _calc_mean(movies)
        directors[director].append(movies_avg)
    return directors


def _calc_mean(movies):
    score_sum = 0
    for movie in movies:
        score_sum += movie.score
    return round(score_sum / len(movies), 1)


def sort_by_avg_score(directors):
    return defaultdict(list, sorted(directors.items(), key=lambda k_v: k_v[1][-1], reverse=True))


def print_results(directors):
    counter = 0
    for director, movies in list(directors.items())[:20]:
        counter += 1
        print(f'{str(counter).zfill(2)}. {director:<52} {movies[-1]}')
        print('-' * 60)
        for movie in movies[:-1]:
            print(f'{movie.year}] {movie.title:<50} {movie.score}')
        print()


def main():
    download_data_to_csv(MOVIE_DATA)
    directors = get_movies_by_director()
    get_average_scores(directors)
    directors = sort_by_avg_score(directors)
    print_results(directors)


if __name__ == '__main__':
    main()
