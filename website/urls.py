from django.urls import path

from . import views

app_name = 'website'

urlpatterns = [
    path('home/', views.HomeView.as_view(), name="home"),
    path('about/', views.AboutView.as_view(), name="about"),
    path('music/', views.MusicView.as_view(), name="music"),
    path('calculators/', views.CalculatorsView.as_view(), name="calculators"),
    path('calculators/divisors/', views.DivisorsView.as_view(), name="divisors"),
    path('calculators/primes/', views.PrimesView.as_view(), name="primes"),
    path('calculators/primes2/', views.Primes2View.as_view(), name="primes2"),
    path('yoga/', views.YogaView.as_view(), name="yoga"),
    path('contact/', views.ContactView.as_view(), name="contact"),
    path("thanks/", views.thanks, name="thanks"),
    path('shipping/', views.ShippingView.as_view(), name="shipping"),
    path('design/', views.DesignView.as_view(), name="design"),
    path('programming/', views.ProgrammingView.as_view(), name="programming"),
    path('knitting/', views.KnittingView.as_view(), name="knitting"),
    path('herbs/', views.HerbsView.as_view(), name="herbs"),

]
