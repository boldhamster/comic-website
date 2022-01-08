from django.shortcuts import render

def home(request):
    return render(request, "home.html", {})

def news(request):
    return render(request, "news.html", {})

def cards(request):
    return render(request, "cards.html", {})

def issue1(request):
    return render(request, "issue1.html", {})

def otherimages(request):
    return render(request, "otherimages.html", {})

def contact(request):
    return render(request, "contact.html", {})
