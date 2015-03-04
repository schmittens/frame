__author__ = 'split'

import os
import glob

#from django import forms


general_text = {'site': 'Framework Test',}
home_text = {'welcome': 'Welcome to the testsite!',}
about_text = {'about': 'About me',}
contact_text = {'contact': 'Contact me',}


def getKey(projectlist):
    return projectlist.folder

def project_collector(folder):

    base = os.path.dirname(__file__) + "/../projects/" + str(folder)
    title_base = base + "/title.txt"
    short_base = base + "/short.txt"
    text_base = base + "/content.txt"
    #url_base = os.path.relpath(__file__, "/projects/") + "/"
    #url_base = os.path.dirname(__file__) + "/../projects/" + str(folder)
    url_base = "/../projects/" + str(folder)
    url_base = os.path.normpath(url_base)
    image_base = base + "/*.png"
    image_base = os.path.normpath(image_base)
    image_thumb = base + "/thumb.png"

    #print(image_base)

    data = {}

    data['folder'] = str(folder)

    title = glob.glob(title_base)
    title = str(title[0])
    title = open(title, 'r')
    data['title'] = title.read()

    short = glob.glob(short_base)
    short = str(short[0])
    short = open(short, 'r')
    data['short'] = short.read()

    text = glob.glob(text_base)
    text = str(text[0])
    text = open(text, 'r')
    data['text'] = text.read()

    data['url'] = str(url_base) + '/'

    data['images'] = glob.glob(image_base)
    data['images'].pop()
    data['thumb'] = image_thumb

    return data


def projects_lister():

    projectlist = []
    projects = []

    base = os.path.dirname(__file__) + "/../projects/"
    #print(base)
    base = os.path.normpath(base)
    #print(base)

    for f in os.listdir(base):
        if os.path.isdir(os.path.join(base, f)):
            projectlist.append(f)

    for project in projectlist:
        p = project_collector(project)
        p = Project(p)
        projects.append(p)
        #projects[project] = p

    projects = sorted(projects, key=getKey)

    #print(projects)

    return projects


class Project():

    def __init__(self, data):
        self.title = data['title']
        self.short = data['short']
        self.text = data['text']
        self.images = data['images']
        self.url = data['url']
        self.folder = data['folder']

    def __str__(self):
        return self.title

