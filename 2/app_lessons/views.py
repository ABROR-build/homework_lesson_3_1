from django.shortcuts import render
from . import models


def list_subjects(request):
    subjects = models.Subjects.objects.all()
    context = {
        'subjects': subjects
    }
    return render(request, 'list_subjects.html', context=context)


def list_lessons(request, pk):
    lessons = models.Lessons.objects.filter(subject=pk)
    context = {
        'lessons': lessons
    }
    return render(request, 'list_lessons.html', context=context)


def get_lesson(request, pk):
    lesson = models.Lessons.objects.get(pk=pk)
    context = {
        'lesson': lesson
    }
    return render(request, 'get_lesson.html', context=context)
