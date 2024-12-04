from pathlib import Path
from django.views.generic import TemplateView


#Hero Python List
herolist = [
    {"id" : 0, "Title" : "Black Widow", "Strengths" : "Cool", "Weaknesses" : "everything", "Image" : "/static/images/black_widow.jpg"},
    {"id" : 1, "Title" : "Hulk", "Strengths" : "Strong", "Weaknesses" : "Anger", "Image" : "/static/images/hulk.jpg"},
    {"id" : 2, "Title" : "ironMan", "Strengths" : "Smart and Rich", "Weaknesses" : "Heart", "Image" : "/static/images/iron_man.jpg"}
]

def photo_list():
    def photo_details(i, f):
        return dict(id=i, file=f) #Heroes Dictionary

    photos = Path('static/images').iterdir()
    photos = [photo_details(i, f) for i, f in enumerate(photos)]
    return photos


class HeroListView(TemplateView):
    template_name = 'heroes.html'

    def get_context_data(self, **kwargs):
        return dict(photos=photo_list())


class HeroView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        i = kwargs['id']
        photos = photo_list()
        p = photos[i]
        
        return herolist[i]

        #From Mark Seaman
