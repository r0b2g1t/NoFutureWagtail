from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .models import Contact
from .forms import ContactForm, PrimesForm, Primes2Form, DivisorForm
from django.urls import reverse_lazy
from django.http import HttpResponse, request
from django.views.generic import View, RedirectView, FormView


class HomeView(TemplateView):
    template_name = 'home.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy("thanks")


def thanks(view):
    return HttpResponse("Thank you! Will get in touch soon.")


class ProgrammingView(TemplateView):
    pass


class KnittingView(TemplateView):
    template_name = 'knitting.html'


class HerbsView(TemplateView):
    pass


class MusicView(TemplateView):
    template_name = 'music.html'


class CalculatorsView(TemplateView):
    template_name = 'calculators.html'

    def get(self, request, *args, **kwargs):
        form2 = PrimesForm(self.request.GET or None)
        form3 = Primes2Form(self.request.GET or None)
        context = self.get_context_data(**kwargs)
        context['form2'] = form2
        context['form3'] = form3
        return self.render_to_response(context)


class PrimesView(View):
    """
    Checking if a number is a prime number and showing all prime numbers between two numbers.
    """

    def post(self, request, *args, **kwargs):
        form2 = self.form_class(request.POST)
        form3 = Primes2Form()
        if form2.is_valid():
            number = form2.cleaned_data['number']
            if number > 1:
                for i in range(2, number):
                    if (number % i) == 0:
                        number = "It is not a prime"
                        return self.render_to_response(
                            self.get_context_data(number=number, form2=form2, form3=form3
                                                  )
                        )

                else:
                    number = "It is a prime"
                    return self.render_to_response(
                        self.get_context_data(number=number, form2=form2, form3=form3
                                              )
                    )
            else:
                number = "It is not a prime"
                return self.render_to_response(
                    self.get_context_data(number=number, form2=form2, form3=form3
                                          )
                )

        else:

            return self.render_to_response(

                self.get_context_data(
                    form2=form2, form3=form3
                ))


class Primes2View(View):
    """
    Showing all prime numbers between two numbers.
    """

    def post(self, request, *args, **kwargs):
        form3 = self.form_class(request.POST)
        form2 = PrimesForm()
        if form3.is_valid():
            number2 = form3.cleaned_data['number2']
            number3 = form3.cleaned_data['number3']
            lst = []
            for num in range(number2, number3 + 1):
                if num > 1:
                    for i in range(2, num):
                        if (num % i) == 0:
                            break
                    else:
                        lst.append(num)

            return self.render_to_response(
                self.get_context_data(number2=number2, number3=number3, lst=lst, form2=form2, form3=form3
                                      )
            )

        else:
            return self.render_to_response(

                self.get_context_data(
                    form2=form2, form3=form3
                ))


class DivisorsView(View):
    """
    Showing all divisors of a number.
    """

    def get(self, request, *args, **kwargs):
        form = DivisorForm()
        context = {'form': form}
        return render(request, 'divisor.html', context)

    def post(self, request, *args, **kwargs):
        form = DivisorForm(data=request.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            lst = []
            for i in range(1, int(number / 2) + 1):
                if number % i == 0:
                    lst.append(i)
            return render(request,
                          'divisor.html',
                          {"number": number,
                           "lst": lst,
                           'form': form},
                          )
        else:
            return render(request,
                          'divisor.html',
                          {'form': form}, )


class YogaView(TemplateView):
    """
    Front page, showing what you can do on this website.
    """
    template_name = 'yoga.html'


class ShippingView(TemplateView):
    """
    Front page, showing what you can do on this website.
    """
    template_name = 'about.html'


class DesignView(TemplateView):
    """
    Front page, showing what you can do on this website.
    """
    template_name = 'about.html'
