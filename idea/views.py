from django.shortcuts import render

# Create your views here.
def index(req):
    context = {

    }
    
    return render(req, 'index.html', context=context)

def about(req):
    context = {

    }
    
    return render(req, 'about.html', context=context)

def blog(req):
    context = {

    }
    
    return render(req, 'blog.html', context=context)

def contact(req):
    context = {

    }
    
    return render(req, 'contact.html', context=context)

def portfolio(req):
    context = {

    }
    
    return render(req, 'portfolio.html', context=context)