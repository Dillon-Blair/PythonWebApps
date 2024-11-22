from django.shortcuts import render
from pathlib import Path
from django.views.generic import TemplateView
from hero.models import Superhero

def photo_list():
    def photo_details(i):
        datatup = getherodata(i)
        return dict(id=i, name=datatup[0], strengths=datatup[1], weaknesses=datatup[2])

    photos = Path('static/images').iterdir()
    photos = [photo_details(str(f)[14]) for i, f in enumerate(photos)]
    return photos

def singlephoto(id):
    def photo_details(i):
        datatup = getherodata(i)
        if i == id:
            return dict(id=i, name=datatup[0], strengths=datatup[1], weaknesses=datatup[2])

    photos = Path('static/images').iterdir()
    idlist = [str(f)[14] for i, f in enumerate(photos)]
    print(idlist)
    photos = []
    for thisid in idlist:
        if thisid == id:
            photos.append(photo_details(thisid))
    #photos = [photo_details(str(f)[14]) for i, f in enumerate(photos)]
    return photos

def getherodata(searchid):
    result = ()
    for s in Superhero.objects.filter(id=searchid):
        result = (
        s.name,
        s.strengths,
        s.weaknesses)
    return result


class HeroListView(TemplateView):
    template_name = 'heroes.html'

    def get_context_data(self, **kwargs):
        return dict(photos=photo_list())


class HeroDetailView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        i = kwargs['id']
        #print(i)
        for j in range(len(photo_list())):
            if str(photo_list()[j]["id"]) == str(i):
                return dict(photo=photo_list()[int(j)])
        # return dict(photo=photo_list()[int(i)])