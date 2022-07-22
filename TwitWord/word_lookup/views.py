from django.shortcuts import render
from django.http import HttpResponseRedirect
from .tweet_fetch import get_tweets
# Create your views here.

# display the home webpage

def home(request):
    if request.method == 'POST':
        word = request.POST['word']
        return HttpResponseRedirect(word)
    return render(request, 'word_lookup/home.html')

# Retrive the input word and process it
def word_input(request, word):
    tweets = get_tweets(word)
    return render(request, 'word_lookup/tweets.html', {'word': word})