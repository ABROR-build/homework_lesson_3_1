from django.shortcuts import render
from .models import *


def list_topics(request):
    topics = Topics.objects.all()
    context = {
        'topics': topics
    }
    return render(request, 'list_topics.html', context=context)


def list_headlines(request, pk):
    headlines = News.objects.filter(topic_name=pk)
    context = {
        'headlines': headlines
    }
    return render(request, 'list_headlines.html', context=context)


def details(request, pk):
    article = News.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, 'details.html', context=context)
