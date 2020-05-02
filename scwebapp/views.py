from django.shortcuts import render


def home(request):
    # return HttpResponse('<h1>Blog Home Page</h1>')
    # context = {'posts': posts} // the data ( get it from db / models )
    # return render(request, 'blogapp/home.html', context)
    return render(request, 'scwebapp/_home.html', {'title' : 'Title of the blog'})


def recipes(request):
    # return HttpResponse('<h1>Blog Home Page</h1>')
    # context = {'posts': posts} // the data ( get it from db / models )
    # return render(request, 'blogapp/home.html', context)
    return render(request, 'scwebapp/recipes.html', {'title' : 'Title of the blog'})
