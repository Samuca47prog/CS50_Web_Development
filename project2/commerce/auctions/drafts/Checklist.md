# References

- [Model Field Reference](https://docs.djangoproject.com/en/4.0/ref/models/fields/)
- [DateTimeField](https://www.geeksforgeeks.org/datetimefield-django-models/)

# Pages

## Index page
* Shows current active auction listings

    each listing must be showing at leat:
    - title
    - description
    - current price
    - photo

## Create New Listing page
* This page will be a form that will add a listing in the site existing Listings

    Users will input:
    - title
    - description
    - start bid
    - Image URL
    - Category
      - field with select dropdown

## Listing page
* Shows all informations about the listing

    page interactions:
    - attach page when user click an listing image
    - if user signed, allow to add/remove to watch list
    - if user signed, allow to add only a higher bid
    - if user signed, allow to add comments
    - if current user is the listing creator, allow to close the auction
    - when auction is closed, show winner bid
    - when auction is closed and user is still in that page, show to him if he is the winner

## WatchList page
* page that display current user favorite auctions

    similar to index page, but show just user favorite auctions

## Categories page
* shows currently categories

    clicking in any category should show listings on that category

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

## class Comments

## class Categories

## class Users

---

# Alternative learnings

## Reload CSS
* Sometimes the CSS stops updating even after reloading the page. When that happens, press ctrl + F5.