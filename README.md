# Hangman
## _PRO1 - seminarska naloga_


[![Build Status](https://travis-ci.com/xtemp3r/hangman.svg?token=ph3uoqDz9qkCKaARptfe&branch=main)](https://travis-ci.com/xtemp3r/hangman)

## Description:

Hangman is a guessing game for two or more players.
A random word is chosen from a wordlist and then the player tries to guess it by suggesting letters within a certain number of guesses/lifes.

## Instructions (in slo):

 - Napiši program za igro 'Vislice'.
 - V programu kreiraj podatkovno strukturo v katero boš shranil 50 različnih angleških besed.
 - Program naj na začetku igre naključno izbere eno od besed in na zaslonu nariše toliko znakov * kolikor je črk v besedi.
 - Potem naj uporabniku dovoli vnos črk tolikor časa, dokler ne ugane besedo ali pa preseže dovoljeno število uganjevanj (določi ga kot konstanto v programu – število delov vislic).
 - Če uporabnik ugane črko, naj program izpiše to črko namesto * na vseh mestih, kjer nastopa.
 - Če črka ni vsebovana v besedi, naj izriše en del vislic.
 - Glede samega izrisovanja vislic pa imaš umetničko svobodo.
 - Program naj na začetku prikaže enostavni meni iz katerega lahko uporabnik izbira opciji na novo igro ali konec dela s programom.



## Installation

Hangman requires Docker or just Python 3.

Build and run the docker container.

```sh
cd hangman/
docker build -t pro1 .
docker run -it pro1
```

Run the python script without docker.

```sh
cd hangman/app/
python3 hangman.py
```
