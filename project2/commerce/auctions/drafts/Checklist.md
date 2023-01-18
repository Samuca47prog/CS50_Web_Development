# References

- [Model Field Reference](https://docs.djangoproject.com/en/4.0/ref/models/fields/)
- [DateTimeField](https://www.geeksforgeeks.org/datetimefield-django-models/)
- [Django Tutorial #27 - Foreign Keys](https://www.youtube.com/watch?v=zJWhizYFKP0)
- [49 - Basic Data Connection with Foreign Keys - Python & Django 3.2 Tutorial Series](https://www.youtube.com/watch?v=3VTeia-AoLo)
- [Using Multiple Database Tables With Django - Django Wednesdays #4](https://www.youtube.com/watch?v=z5e_8FgKZig)
- [Fetch Data From a Database And Output To A Webpage - Django Wednesdays #5](https://www.youtube.com/watch?v=H3joYTIRqKk)
- [How To Modify The Django Admin Area - Django Wednesdays #6](https://www.youtube.com/watch?v=_7Fi9dpw-ew)
- [How To Add Database Forms To A Web Page - Django Wednesdays #7](https://www.youtube.com/watch?v=CVEKe39VFu8)

- [Adding Extra Fields On Many-To-Many Relationships in Django](https://www.youtube.com/watch?v=-HuTlmEVOgU&t=787s)

# Pages

## Index page
* Shows current active auction listings

    each listing must be showing at leat:
    - [OK] title
    - [OK] description
    - [OK] current price
    - [OK] photo


    - [OK] creator
    - [OK] creation

## Create New Listing page
* This page will be a form that will add a listing in the site existing Listings

    Users will input:
    - [OK] title
    - [OK] description
    - [OK] start bid
    - [OK] Image URL
      - [OK] can be null
    - [OK] Category
      - [OK] field with select dropdown
      - can be null

## Listing page
* Shows all informations about the listing

    page interactions:
    - [OK] attach page when user click an listing image
    - if user signed, allow to add/remove to watch list
    - if user signed, allow to add only a higher bid
    - if user signed, allow to add comments
    - if current user is the listing creator, allow to close the auction
      * show pop up of are you sure?
    * [OK] if current user is the listing creator, allow to delete the auction
      * show pop up of are you sure?
    - when auction is closed, show winner bid
    - when auction is closed and user is still in that page, show to him if he is the winner

## WatchList page
* page that display current user favorite auctions

    similar to index page, but show just user favorite auctions

## Categories page
* shows currently categories

    - [OK] clicking in any category should show listings on that category
    - [OK] create new categories
    * allow creators to delete categories

---

# Models

## class Listing
    - Listing is the product that will be aucted

    # Mandatory
        - Title
        - Text description
        - Start bid

    # Optionally
        - Image URL
        - Category


        - creation
        - creator

## class Bids
    -  Bids are the prices offered for the listing

    - user
    - bid

## class Comments

## class Categories

    - name
    - creator

## class Users

    - watchlist

---

# Alternative learnings

## Reload CSS
* Sometimes the CSS stops updating even after reloading the page. When that happens, press ctrl + F5.