from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .tweet_fetch import get_tweets, get_ids
from django.core.exceptions import ValidationError
from .models import WordTable

def home(request):
    # display the homepage and redirect to the word input page when sent a post request
    url = reverse('home')
    if request.method == 'POST':
        #redirect to home page if no input is provided
        if request.POST['user_input'] == '':
            return HttpResponseRedirect(url)
        # save input word to database
        user_input = WordTable(word=request.POST['user_input'])
        user_input.save()
        return HttpResponseRedirect(url + 'tweets/' + str(user_input.id))
    return render(request, 'word_lookup/home.html')

def word_input(request, user_id):
    url = reverse('home')
    if request.method == 'POST':
        #redirect to home page if no input is provided
        if request.POST['user_input'] == '':
            return HttpResponseRedirect(url)
        # save input word to database
        user_input = WordTable(word=request.POST['user_input'])
        user_input.save()
        return HttpResponseRedirect(url + 'tweets/' + str(user_input.id))
    # Retrive the input word and process it
    try:
        prompt_word = WordTable.objects.get(id=user_id)
    except ValidationError:
        return HttpResponseRedirect(url)
    
    # used to delete cant refresh or return to page if used in current state
    # UserWord.objects.get(id=user_id).delete()
    
    raw_tweets = get_tweets(prompt_word)
    left_tweets, right_tweets = get_ids(raw_tweets)
    return render(request, 'word_lookup/tweets.html', {'left_tweets':left_tweets, 'right_tweets':right_tweets})