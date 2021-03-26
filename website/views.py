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


class MusicView(TemplateView):
    template_name = 'music.html'


class CalculatorsView(TemplateView):
    template_name = "calculators.html"

    def get(self, request, *args, **kwargs):
        form2 = PrimesForm()
        form3 = Primes2Form()
        context = {'form2': form2,
                   'form3': form3}
        return render(request, 'calculators.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            if "prime" in request.POST:
                form2 = PrimesForm(data=request.POST, prefix="banned")
                if form2.is_valid():
                    number = form2.cleaned_data['number']
                    if number > 1:
                        for i in range(2, number):
                            if (number % i) == 0:
                                return render(request,
                                              'isnotprime.html',
                                              {"number": number, 'form2': form2},
                                              )
                        else:
                            return render(request,
                                          'isprime.html',
                                          {"number": number, 'form2': form2},
                                          )
                    else:
                        return render(request,
                                      'isnotprime.html',
                                      {"number": number, 'form2': form2},
                                      )
                form3 = Primes2Form(prefix='expected')


            elif "prime2" in request.POST:
                form3 = Primes2Form(request.POST, prefix='expected')
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

                    return render(request,
                                  'primes2.html',
                                  {"number2": number2,
                                   "number3": number3,
                                   "lst": lst,
                                   'form3': form3},
                                  )

                form2 = PrimesForm(prefix='banned')

        else:
            form2 = PrimesForm(prefix='banned')
            form3 = Primes2Form(prefix='expected')
            context = {'form2': form2,
                       'form3': form3}
            return render(request, 'calculators.html', context)


class PrimesView(View):
    """
    Checking if a number is a prime number.
    """

    def get(self, request, *args, **kwargs):
        form2 = PrimesForm()
        context = {'form2': form2}
        return render(request, 'primes.html', context)

    def post(self, request, *args, **kwargs):
        form2 = PrimesForm(data=request.POST)
        if form2.is_valid():
            number = form2.cleaned_data['number']
            if number > 1:
                for i in range(2, number):
                    if (number % i) == 0:
                        return render(request,
                                      'isnotprime.html',
                                      {"number": number, 'form2': form2},
                                      )

                else:
                    return render(request,
                                  'isprime.html',
                                  {"number": number, 'form2': form2},
                                  )
            else:
                return render(request,
                              'isnotprime.html',
                              {"number": number, 'form2': form2},
                              )

        else:
            return render(request,
                          'primes.html',
                          {'form2': form2},
                          )


class Primes2View(View):
    """
    Showing all prime numbers between two numbers.
    """

    def get(self, request, *args, **kwargs):
        form3 = Primes2Form()
        context = {'form3': form3}
        return render(request, 'primes2.html', context)

    def post(self, request, *args, **kwargs):
        form3 = Primes2Form(data=request.POST)
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

            return render(request,
                          'primes2.html',
                          {"number2": number2,
                           "number3": number3,
                           "lst": lst,
                           'form3': form3},
                          )
        else:
            return render(request,
                          'primes2.html',
                          {'form3': form3}, )


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
