from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'pages/index.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

class GalleryPageView(TemplateView):
    template_name = 'pages/gallery.html'

class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'
