from django.shortcuts import render, redirect, get_object_or_404

from webapp.forms import MusicianForm, SearchForm
from webapp.models import Musician
import requests


def index_view(request):
    return redirect('musicians_list')


def musicians_list_view(request):
    musicians = Musician.objects.filter(position__gt=0)
    form = SearchForm(request.GET)
    if form.is_valid():
        search_query = form.cleaned_data['search']
        if search_query:
            musicians = musicians.filter(author__icontains=search_query)
    musicians = musicians.order_by('position', 'author')
    return render(request, 'musicians_list.html', context={'musicians': musicians, 'form': form})


def musician_view(request, pk):
    musician = get_object_or_404(Musician, pk=pk)
    return render(request, 'musician.html', context={'musician': musician})


def musician_get_view(request):
    response = requests.get(
        'https://music.yandex.ru/handlers/main.jsx?what=chart',
        headers={
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'Host': 'music.yandex.ru',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0',
        },
    )
    json_response = response.json()

    musicians = json_response['charts'][0]['entities']
    for musician in musicians:
        data = musician['data']
        mus = Musician.objects.create(
            author=data['track']['artists'][0]['name'],
            song=data['track']['title'],
            position=data['chartPosition']['position']
        )
        print(mus.author)
    return musicians_list_view(request)


def musician_add_view(request):
    if request.method == 'GET':
        form = MusicianForm()
        return render(request, 'musician_add.html', context={'form': form})
    elif request.method == 'POST':
        form = MusicianForm(data=request.POST)
        if form.is_valid():
            musician = Musician.objects.create(
                author=form.cleaned_data['author'],
                song=form.cleaned_data['song'],
                position=form.cleaned_data['position']
            )
            return redirect('musician', pk=musician.pk)
        else:
            return render(request, 'musician_add.html', context={'form': form})


def musician_edit_view(request, pk):
    musician = get_object_or_404(Musician, pk=pk)
    if request.method == 'GET':
        form = MusicianForm(data={
            'author': musician.author,
            'song': musician.song,
            'position': musician.position
        })
        return render(request, 'musician_edit.html', context={'form': form, 'musician': musician})
    elif request.method == 'POST':
        form = MusicianForm(data=request.POST)
        if form.is_valid():
            musician.author = form.cleaned_data['author']
            musician.song = form.cleaned_data['song']
            musician.position = form.cleaned_data['position']
            musician.save()
            return redirect('musician', pk=musician.pk)
        else:
            return render(request, 'musician_edit.html', context={'form': form, 'musician': musician})


def musician_delete_view(request, pk):
    musician = get_object_or_404(Musician, pk=pk)
    if request.method == 'GET':
        return render(request, 'musician_delete.html', context={'musician': musician})
    elif request.method == 'POST':
        musician.delete()
        return redirect('musicians_list')
