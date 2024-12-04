from pathlib import Path
from django.views.generic import TemplateView

herolist = [
    {"id" : 0, "Name" : "Black Widow", "Strengths" : "Cool", "Weaknesses" : "everything", "Image" : "/static/images/black_widow.jpg"},
    {"id" : 1, "Name" : "Hulk", "Strengths" : "Strong", "Weaknesses" : "Anger", "Image" : "/static/images/hulk.jpg"},
    {"id" : 2, "Name" : "ironMan", "Strengths" : "Smart and Rich", "Weaknesses" : "Heart", "Image" : "/static/images/iron_man.jpg"}
]

def photo_list():
    def photo_details(i, f):
        return dict(id=i, file=f) #Dictionary for heroes

    photos = Path('static/images').iterdir()
    photos = [photo_details(i, f) for i, f in enumerate(photos)]
    return photos


class HeroListView(TemplateView):
    template_name = 'heroes.html'

    def get_context_data(self, **kwargs):
        return dict(photos=photo_list())


class HeroDetailView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        i = kwargs['id']
        photos = photo_list()
        p = photos[i]
        
        return herolist[i]

        #From Mark Seaman
