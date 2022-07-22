from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .tweet_fetch import get_tweets

def home(request):
    # display the homepage and redirect to the word input page when sent a post request
    if request.method == 'POST':
        url = reverse('home')
        word = request.POST['word']
        # TODO add word validation
        return HttpResponseRedirect(url + word)
    return render(request, 'word_lookup/home.html')

def word_input(request, word):
    if request.method == 'POST':
        url = reverse('home')
        word = request.POST['word']
        # TODO add word validation
        return HttpResponseRedirect(url + word)
    # Retrive the input word and process it
    tweets = get_tweets(word)
    return render(request, 'word_lookup/tweets.html', {'word': word})