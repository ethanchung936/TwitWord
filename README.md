# TwitWord
A website that allows the user to enter a word then shows them a series of embedded tweets that contain the word.

When a user enters a word or phrase it is recorded in a database using SQLite 3 and they are shown 6 embedded tweets that contain their word or phrase. 
This is done by interfacing with the twitter api using the Tweepy python library and getting links to tweets that meet the search criteria. The tweets are then embedded
on the web page and the user can interact with them and view the tweets on twitter.

Disclaimer: this is currently just the code for the website, but I plan publishing it in the near future.
