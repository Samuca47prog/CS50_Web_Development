from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Listing, Categories, Watchlist, Bid


def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all(),
        "header": "Active Listings"
    })


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
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


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
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def create_listing(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        start_bid = request.POST["start_bid"]
        image_url = request.POST["image_url"]
        category = Categories.objects.get(pk=int(request.POST["category"]))
        user = User.objects.get(pk=int(request.user.id))

        bid = Bid(author=user, bid=start_bid)
        bid.save()

        # Create new Listing
        try:
            new_listing = Listing(  title=title,
                                    description=description, 
                                    start_bid=start_bid,
                                    image_url=image_url,
                                    category=category,
                                    creator=user,
                                    bid=bid
            )
            new_listing.save()
        except IntegrityError:
            return render(request, "auctions/create_listing.html", {
                "message": "unable to create listing",
                "categories": Categories.objects.all()
            })

        return HttpResponseRedirect(reverse("index"))

    else:
        return render(request, "auctions/create_listing.html", {
            "categories": Categories.objects.all()
        })

def listing(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    return render(request, "auctions/listing.html", {
        "listing": listing
    })

def categories(request):
    if request.method == 'POST':
        new_category = request.POST["category"]

        # Create new Category
        try:
            category = Categories(name=new_category)
            category.save()
        except:
            return render(request, "auctions/create_categories.html", {
                "message": "unable to create category"
            })
        return HttpResponseRedirect(reverse("categories"))
    else: 
        return render(request, "auctions/categories.html", {
            "categories": Categories.objects.all()
        })


def category(request, category_id):
    category = Categories.objects.get(id=int(category_id))

    return render(request, "auctions/index.html", {
        "listings": Listing.objects.filter(category=category),
        "header": "Listings on category: " + str(category.name)
    })


def delete_auction(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    listing_name = listing.title
    listing.delete()

    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all(),
        "header": "Active Listings",
        "message": "listing deleted: " + listing_name
    })

def watchlist(request):
        return render(request, "auctions/index.html", {
            "listings": Listing.objects.all(),
            "header": "Watchlist"
        })

def add_bid(request, listing_id):
    listing = Listing.objects.get(pk=int(listing_id))

    if request.method == "POST":
        user_bid = request.POST["bid"]
        user = User.objects.get(pk=int(request.user.id))
        bid = Bid(author=user, bid=float(user_bid))

        if bid.bid > listing.bid.bid:
            listing.bid = bid
            bid.save()
            listing.save()
            return render(request, "auctions/listing.html", {
                "listing": listing,
                "message": "You have placed your bid!"
            })
        else:
            return render(request, "auctions/listing.html", {
                "listing": listing,
                "message": "Your Bid must be bigger than $" + str(listing.bid.bid) + ", the actual bid"
            })

    return render(request, "auctions/listing.html", {
        "listing": listing
    })