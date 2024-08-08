from django.shortcuts import render, redirect
from .models import Emp, Blog, Comment


# Create your views here.

def signup(request):
    if request.POST:
        u = request.POST['uname']
        e = request.POST['email']
        p = request.POST['password']
        obj = Emp(uname=u, email=e, password=p)
        obj.save()
        return redirect('/#')
    return render(request, "signup.html")


def login(request):
    if request.session.get('is_login'):
        return redirect('/home')
    if request.POST:
        e = request.POST['email']
        p = request.POST['password']
        count = Emp.objects.filter(email=e, password=p).count()
        if count > 0:
            request.session['is_login'] = True
            return redirect('/home')
    return render(request, "login.html")


def home(request):
    data = Blog.objects.all
    return render(request, "home.html", {"data": data})


def readMore(request, id):
    data = Blog.objects.get(id=id)
    c = Comment.objects.filter(pid=id)
    if request.POST:
        m = request.POST['msg']
        obj = Comment(msg=m)
        obj.pid_id = id
        obj.save()
    return render(request, "readmore.html", {"data": data, "c": c})


def createPost(request):
    if request.POST:
        postby = request.POST['postby']
        title = request.POST['title']
        desc = request.POST['pdetail']
        img = request.FILES['img']
        obj = Blog(title=title, image=img, desc=desc, postby=postby)
        obj.save()
        return redirect('/home')
    return render(request, "createPost.html")


def logout(request):
    del request.session['is_login']
    return redirect('/#')
