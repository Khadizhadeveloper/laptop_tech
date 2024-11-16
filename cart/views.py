from django.shortcuts import render


def add(request):
    render(request, 'cart/add.html',{})

def remove(request):
    render(request, 'cart/remove.html',{})

def update(request):
    render(request, 'cart/update.html',{})

def retreive_all(request):
    render(request, 'cart/retreive_all.html',{})