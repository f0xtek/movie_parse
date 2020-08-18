# Movie Parse

This is my solution to [Pybites code challenge 13 - Highest Rated Movie Directors](https://pybit.es/codechallenge13.html)

This script downloads a CSV movie data set and parses the results to display the top 20 directors, sorted based on average IMDB movie score.

The results only contain directors that have a minimum of 4 movies, that were released on or after 1960.

```bash
$ python3 movie_parse.py
01. Sergio Leone                                         8.5
------------------------------------------------------------
1966] The Good, the Bad and the Ugly                     8.9
1968] Once Upon a Time in the West                       8.6
1984] Once Upon a Time in America                        8.4
1964] A Fistful of Dollars                               8.0

02. Christopher Nolan                                    8.4
------------------------------------------------------------
2008] The Dark Knight                                    9.0
2010] Inception                                          8.8
2014] Interstellar                                       8.6
2012] The Dark Knight Rises                              8.5
2006] The Prestige                                       8.5
2000] Memento                                            8.5
2005] Batman Begins                                      8.3
2002] Insomnia                                           7.2

03. Quentin Tarantino                                    8.2
------------------------------------------------------------
1994] Pulp Fiction                                       8.9
2012] Django Unchained                                   8.5
1992] Reservoir Dogs                                     8.4
2009] Inglourious Basterds                               8.3
2003] Kill Bill: Vol. 1                                  8.1
2004] Kill Bill: Vol. 2                                  8.0
2015] The Hateful Eight                                  7.9
1997] Jackie Brown                                       7.5

04. Hayao Miyazaki                                       8.2
------------------------------------------------------------
2001] Spirited Away                                      8.6
1997] Princess Mononoke                                  8.4
2004] Howl's Moving Castle                               8.2
2008] Ponyo                                              7.7

05. Frank Darabont                                       8.0
------------------------------------------------------------
1994] The Shawshank Redemption                           9.3
1999] The Green Mile                                     8.5
2007] The Mist                                           7.2
2001] The Majestic                                       6.9

06. Stanley Kubrick                                      8.0
------------------------------------------------------------
1964] Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb 8.5
1980] The Shining                                        8.4
1968] 2001: A Space Odyssey                              8.3
1975] Barry Lyndon                                       8.1
1962] Lolita                                             7.7
1999] Eyes Wide Shut                                     7.3

07. James Cameron                                        7.9
------------------------------------------------------------
1991] Terminator 2: Judgment Day                         8.5
1986] Aliens                                             8.4
1984] The Terminator                                     8.1
2009] Avatar                                             7.9
1997] Titanic                                            7.7
1989] The Abyss                                          7.6
1994] True Lies                                          7.2

08. Peter Jackson                                        7.9
------------------------------------------------------------
2003] The Lord of the Rings: The Return of the King      8.9
2001] The Lord of the Rings: The Fellowship of the Ring  8.8
2002] The Lord of the Rings: The Two Towers              8.7
2013] The Hobbit: The Desolation of Smaug                7.9
2012] The Hobbit: An Unexpected Journey                  7.9
2014] The Hobbit: The Battle of the Five Armies          7.5
1994] Heavenly Creatures                                 7.4
2005] King Kong                                          7.2
2009] The Lovely Bones                                   6.7

09. Alejandro G. Iñárritu                                7.8
------------------------------------------------------------
2015] The Revenant                                       8.1
2000] Amores Perros                                      8.1
2014] Birdman or (The Unexpected Virtue of Ignorance)    7.8
2003] 21 Grams                                           7.7
2010] Biutiful                                           7.5
2006] Babel                                              7.5

10. Alfonso Cuarón                                       7.8
------------------------------------------------------------
2006] Children of Men                                    7.9
2004] Harry Potter and the Prisoner of Azkaban           7.8
2013] Gravity                                            7.8
2001] Y Tu Mamá También                                  7.7

11. Martin Scorsese                                      7.7
------------------------------------------------------------
1990] Goodfellas                                         8.7
2006] The Departed                                       8.5
1980] Raging Bull                                        8.3
1976] Taxi Driver                                        8.3
2013] The Wolf of Wall Street                            8.2
1995] Casino                                             8.2
1978] The Last Waltz                                     8.2
2010] Shutter Island                                     8.1
1988] The Last Temptation of Christ                      7.6
2011] Hugo                                               7.5
2004] The Aviator                                        7.5
2002] Gangs of New York                                  7.5
1973] Mean Streets                                       7.4
1991] Cape Fear                                          7.3
1993] The Age of Innocence                               7.2
2008] Shine a Light                                      7.2
1997] Kundun                                             7.0
1986] The Color of Money                                 7.0
1999] Bringing Out the Dead                              6.8
1977] New York, New York                                 6.7

12. David Fincher                                        7.7
------------------------------------------------------------
1999] Fight Club                                         8.8
1995] Se7en                                              8.6
2014] Gone Girl                                          8.1
2008] The Curious Case of Benjamin Button                7.8
2011] The Girl with the Dragon Tattoo                    7.8
1997] The Game                                           7.8
2007] Zodiac                                             7.7
2010] The Social Network                                 7.7
2002] Panic Room                                         6.8
1992] Alien 3                                            6.4

13. Matthew Vaughn                                       7.7
------------------------------------------------------------
2011] X-Men: First Class                                 7.8
2007] Stardust                                           7.7
2010] Kick-Ass                                           7.7
2004] Layer Cake                                         7.4

14. Peter Weir                                           7.7
------------------------------------------------------------
1998] The Truman Show                                    8.1
1989] Dead Poets Society                                 8.0
2003] Master and Commander: The Far Side of the World    7.4
1985] Witness                                            7.4

15. Brad Bird                                            7.6
------------------------------------------------------------
2007] Ratatouille                                        8.0
2004] The Incredibles                                    8.0
1999] The Iron Giant                                     8.0
2011] Mission: Impossible - Ghost Protocol               7.4
2015] Tomorrowland                                       6.5

16. Paul Greengrass                                      7.6
------------------------------------------------------------
2007] The Bourne Ultimatum                               8.1
2013] Captain Phillips                                   7.9
2004] The Bourne Supremacy                               7.8
2002] Bloody Sunday                                      7.7
2006] United 93                                          7.6
2016] Jason Bourne                                       7.1
2010] Green Zone                                         6.9

17. Spike Jonze                                          7.6
------------------------------------------------------------
2013] Her                                                8.0
1999] Being John Malkovich                               7.8
2002] Adaptation.                                        7.7
2009] Where the Wild Things Are                          6.8

18. Edgar Wright                                         7.6
------------------------------------------------------------
2004] Shaun of the Dead                                  8.0
2007] Hot Fuzz                                           7.9
2010] Scott Pilgrim vs. the World                        7.5
2013] The World's End                                    7.0

19. Wes Anderson                                         7.6
------------------------------------------------------------
2014] The Grand Budapest Hotel                           8.1
2009] Fantastic Mr. Fox                                  7.8
2012] Moonrise Kingdom                                   7.8
1998] Rushmore                                           7.7
2001] The Royal Tenenbaums                               7.6
2004] The Life Aquatic with Steve Zissou                 7.3
1996] Bottle Rocket                                      7.1

20. David Lynch                                          7.6
------------------------------------------------------------
1980] The Elephant Man                                   8.2
2001] Mulholland Drive                                   8.0
1999] The Straight Story                                 8.0
1977] Eraserhead                                         7.4
1984] Dune                                               6.6
```

## Running the script

To run the script:

1. `python3 -m venv venv && source venv/bin/activate`
2. `pip install -r requirements.txt`
3. `python3 movie_parse.py`