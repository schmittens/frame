__author__ = 'split'

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template import Template, Context
from django.core.mail import send_mail

from assets.helper import *


def home(request):
    return render_to_response('home.html', {'general_text': general_text, 'home_text': home_text})

def about(request):
    return render_to_response('about.html', {'general_text': general_text, 'about_text': about_text})

def contact(request):
    #return render_to_response('contact.html', {'general_text': general_text, 'contact_text': contact_text})

    errors = []
    form_errors = {
        'subject': '',
        'email': '',
        'message': '',
    }
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
            form_errors['subject'] = 'has-error has-feedback'
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
            form_errors['message'] = 'has-error has-feedback'
        if not request.POST.get('email', ''):
            errors.append('Enter a valid E-Mail address.')
            form_errors['email'] = 'has-error has-feedback'
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid E-Mail address.')
            form_errors['email'] = 'has-error has-feedback'
        if not errors:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email', 'noreply@testsite.com'),
                ['admin@frame.com'],
            )
            return HttpResponseRedirect('/thanks/')
    return render(request, 'contact.html', {'errors': errors, 'form_errors': form_errors, 'contact_text': contact_text})

def thanks(request):
    return render_to_response('thanks.html')

def project(request, folder):

    # collect project data
    data = project_collector(folder)

    # instantiate object with collected data as a dict
    project = Project(data)
    #print(project.folder)

    return render_to_response('project.html', {'general_text': general_text, 'project': project})

def projects(request):

    # get projects data
    projects = projects_lister()

    return render_to_response('projects.html', {'general_text': general_text, 'projects': projects})

def gallery(request):
    projects = projects_lister()
    return render_to_response('gallery.html', {'general_text': general_text, 'gallery': projects})

def image(request, image_path):
    print(image_path)
    return render_to_response('image.html', {'general_text': general_text, 'image': image_path})



