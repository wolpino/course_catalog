# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Course
from .models import Desc
from django.contrib import messages

# Create your views here.


def index(request):
    context= {
        "all_courses" : Course.objects.all(),
        "all_descriptions" : Desc.objects.all()
            }
    return render(request, "courses/index.html", context)


def add(request):
     if request.method == "POST":
        errors = Course.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error)
            return redirect(reverse('main'))
        else:
            Course.objects.create(name=request.POST['name'],)
            a = Course.objects.last()
            number = a.id
            Desc.objects.create(desc=request.POST['desc'], course_id=number,)
            return redirect(reverse('main'))


def destroy(request, number):
    context= {
        "course" : Course.objects.get(id=number)
    }
    return render(request, "courses/destroy.html", context)

def delete(request, number):
    a = Course.objects.get(id=number)
    a.delete()
    return redirect(reverse('main'))    