from django.views.generic import TemplateView 




class HomeView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'HomePage',
            'id': 'BACS350 Project 2',
        }

class HulkView(TemplateView):
    template_name = 'hulk.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Hulk',
            'id': 'Bruce Banner',
            'strengths': 'Strengths: Strong',
            'weaknesses': 'Weaknesses: Anger',
            'image': '/static/images/hulk.jpg'
        }
    
class IronManView(TemplateView):
    template_name = 'ironman.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'IronMan',
            'id': 'Tony Stark',
            'strengths': 'Strenghts: Smart',
            'weaknesses': 'Weaknesses: Human body',
            'image': '/static/images/iron_man.jpg'
        }

class BlackWidowView(TemplateView):
    template_name = 'blackwidow.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'BlackWidow',
            'id': 'Natasha Romanoff',
            'strengths': 'Strenghts: Stealthy',
            'weaknesses': 'Weaknesses: Trauma',
            'image': '/static/images/black_widow.jpg'
        }
    
    