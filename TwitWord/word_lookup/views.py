from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .tweet_fetch import get_tweets, get_ids

def home(request):
    # display the homepage and redirect to the word input page when sent a post request
    if request.method == 'POST':
        url = reverse('home')
        user_input = request.POST['user_input']
        # TODO add word validation
        return HttpResponseRedirect(url + user_input)
    return render(request, 'word_lookup/home.html')

def word_input(request, word):
    if request.method == 'POST':
        url = reverse('home')
        user_input = request.POST['user_input']
        # TODO add word validation
        return HttpResponseRedirect(url + user_input)
    # Retrive the input word and process it
    raw_tweets = get_tweets(word)
    left_tweets, right_tweets = get_ids(raw_tweets)
    return render(request, 'word_lookup/tweets.html', {'left_tweets':left_tweets, 'right_tweets':right_tweets})