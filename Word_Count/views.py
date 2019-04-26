from django.http import HttpResponse
from django.shortcuts import render

import operator

def home(request):
    return render(request, 'home.html')
def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    
    wordcountDictionary = {}
    
    
    
    for word in wordlist:
        word = word.lower()
        wordcountDictionary[word] = wordcountDictionary.get(word, 0) + 1
        sortedwords = sorted(wordcountDictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'count':len(wordlist), 'sortedwords': sortedwords})

def about(request):
    return render(request, "about.html")