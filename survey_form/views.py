from django.shortcuts import render, redirect

def index(request):
    return render(request, 'form.html')

def process(request):
    request.session['name'] = request.POST['name']
    request.session['dojo_loc'] = request.POST['dojo_loc']
    request.session['fav_lang'] = request.POST['fav_lang']
    request.session['program'] = request.POST['program']
    request.session['like'] = request.POST.getlist('like')
    request.session['comment'] = request.POST['comment']
    return redirect('display/')

def display(request):
    return render(request, 'result.html')

def back(request):
    return redirect('/')
