from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import FormView, ListView
from django.views.generic.detail import SingleObjectMixin
from .models import Languages, Menus
from .forms import ContactForm
from django.core.mail import send_mail


class LayoutListView(ListView):
    # TBD
    #

    context_object_name = 'menu_list'

    def get_template_names(self, **kwargs):
        template_name = 'main/' + self.kwargs['section'] + '.html'
        return template_name

    def get_queryset(self):
        self.lang = get_object_or_404(Languages, language=self.kwargs['lang'])
        return Menus.objects.filter(language=self.lang, location='navbar')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        # Generally, get_context_data will merge the context data of all parent classes
        # with those of the current class
        context['lang_list'] = Languages.objects.all()
        context['selflang'] = self.lang
        context['selfsection'] = self.kwargs['section']
        # TBD : really need here?
        context['form'] = ContactForm()
        return context


class ContactUsMix(SingleObjectMixin, FormView):

    template_name = 'main/contactus.html'
    form_class = ContactForm
    model = Menus

    def post(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            return HttpResponseForbidden()

        self.object = self.get_object()
        return super().post(request, *args, **kwargs)


class Index(View):

    def get(self, request, *args, **kwargs):
        view = LayoutListView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = ContactUsMix.as_view()
        return view(request, *args, **kwargs)
