






'''
View¶
class django.views.generic.base.View¶
The master class-based base view. All other class-based views inherit from this base class.
It isn’t strictly a generic view and thus can also be imported from django.views.
Method Flowchart:
    setup()
    dispatch()
    http_method_not_allowed()
    options()
'''


'''
TemplateView¶
class django.views.generic.base.TemplateView¶
Renders a given template, with the context containing parameters captured in the URL.
This view inherits methods and attributes from the following views:

    django.views.generic.base.TemplateResponseMixin
    django.views.generic.base.ContextMixin
    django.views.generic.base.View

Method Flowchart
    setup()
    dispatch()
    http_method_not_allowed()
    get_context_data()
'''
from django.views.generic.base import TemplateView
from .models import Languages, Menus

class HomePageView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar_list'] = Menus.objects.all()
        return context


'''
RedirectView¶
class django.views.generic.base.RedirectView¶
Redirects to a given URL.
The given URL may contain dictionary-style string formatting, which will be interpolated against the parameters captured in the URL. Because keyword interpolation is always done (even if no arguments are passed in), any "%" characters in the URL must be written as "%%" so that Python will convert them to a single percent sign on output.
If the given URL is None, Django will return an HttpResponseGone (410).
This view inherits methods and attributes from the following view:
django.views.generic.base.View

Method Flowchart

    setup()
    dispatch()
    http_method_not_allowed()
    get_redirect_url()
'''



# Handling forms with class-based views
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .forms import MyForm

class MyFormView(View):
    form_class = MyForm
    initial = {'key': 'value'}
    template_name = 'form_template.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})
