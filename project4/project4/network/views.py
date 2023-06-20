from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import PostForm

from .models import User, UserProfile
from .models import Posts


def index(request):

    return all_posts(request)


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            profile = UserProfile.objects.create(user=user)
            user.save()
            profile.save
            
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")




def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("all_posts")
        
    else:
        form = PostForm

    return render(request, 'network/add_post.html', {
        'form': form,
    })




def all_posts(request):
    all_posts = Posts.objects.all().order_by('-posted_date')

    return render(request, "network/all_posts.html", {
        "all_posts": all_posts
    })



def user_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user_posts = Posts.objects.filter(author=request.user).order_by('-posted_date')
    user_profile = UserProfile.objects.get(user=user)
    following = user_profile.following.all()
    followers = user_profile.followers.all()

    return render(request, "network/user_profile.html", {
        "user": user,
        "user_posts": user_posts,
        "following": following,
        "followers": followers
    })