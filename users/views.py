from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm
from users.newsapi import get_news_data,get_date


def news(request):
    """ This function is responsible for handling a form submission,
    retrieving news data based on the user's search query, formatting the retrieved data,
     and rendering it in a template."""
    if request.method == 'POST':
        formdata = request.POST
        text = formdata.get("search")
        if text:
            resp = get_news_data(text)
            success = resp.get("Success")
            if success:
                res = resp.get("records")
                article_list = res.get("articles")
                data = []
                for art in article_list:
                    date = get_date(art.get("publishedAt"))
                    day = date.date()
                    time = date.time()
                    data.append({"title":art.get("title"),"url":art.get("url"),"published":f'{day} {time}'})
                return render(request, 'users/news.html', context={"data":data})
    return render(request, 'users/news.html')


def signup(request):
    """ This function handles the signup process of a user in a newsapi webapp"""
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = SignupForm()
    context = { 'form': form }
    return render(request, 'users/signup.html', context)



