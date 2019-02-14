# [BrickStickerShop](https://bss-msp-4.herokuapp.com) [![Build Status](https://travis-ci.org/arjanvdmeij/msp4-bricksticker.svg?branch=master)](https://travis-ci.org/arjanvdmeij/msp4-bricksticker)

## Overview

### What is this?

This is the fourth project created for the Full Stack Web Developer course by [Code Institute](https://codeinstitute.net).
The goal here was to pull together everything learned over the course's run.
In this case, I created a webshop 'mockup', with content based on my brother's actual shop.
In time, the actual shop can (and will) be re-designed, however it will be based on frameworks provided by his hosting.
For the project, Django was used as a framework, with Heroku for site hosting and Amazon AWS for file storage of uploaded content.

The site is 99% functional, the only thing that will not happen is actual payment processing.
The site is currently restricted to a test version of Stripe, and orders will never be sent out (sorry!)

### What does it do?

Like any other shop, the site opens with general information and the latest additions to the inventory of the shop.
From here, the full list can be opened, which in turn can be filtered on category, or a search can be performed to find a specific product.
Any product presented can then be zoomed in on, and added into the cart. In a product detail page, comments can be left as well on the product.
When viewing the cart, the quantity of the item can be adjusted, or the item can be removed entirly from the cart.
During checkout changes can be made still as well.
Users can create an account in order to receive a newsletter at this point. 
They can log on later to have themselves 'forgotten', effectively removing the account and with it, the subscription to the newsletter.

### How does it work

On the opening page, data is retrieved from the database and filtered for most recent items. 
These are then shown on the page, using Django to render the information onto the page.
The same goes for the products page, where two sets of data are retrieved to populate the page with.
The full list of products, as well as a list of unique category names is used in this case.
Whenever a user selects a category from the dropdown, the page is refreshed with a subset of data where the products all share the same category.
The search function bases itself on the product name and the description, returning only those results where products have the search statement in either field.

The database used depends on the environment the application is running on.
Logic looking at the environment 'picks' the correct database to use. For development (on Cloud9), the application uses a SQLite database,
on the production environment (on Heroku), a PostGres database is used. 
This logic is also applied to the content uploaded (when adding products), where development stores in Cloud9, and production uses an Amazon AWS Bucket for static files and media.

The code used is mostly based on **Django**, version 1.11.18 and **Python**, version 3.4.3.
For the HTML, **Bootstrap 4.1.3** was used for styling. 
- Bootstrap with popper.js included was used for full Bootstrap functionality.
Some **javascript** was used for the product detail pages, but this was kept to a minimum and instead Bootstrap's basics were used.
**Font Awesome**, version 5.6.0, was used for icons.

The site can be viewed [HERE](https://bss-msp-4.herokuapp.com)

## Features

### Existing Features
- Opening page with a banner, some info and basic links, followed by 5 most recent additions to the site's inventory
- *Optional* account creation for the use of newsletter subscribing
  - Account creation is specifically not needed to make purchases
- Optionally, users can delete their account themselves to be removed from the newsletter through profile page
- Links to various information in the footer of the site, detailing information about:
  - products FAQ
  - privacy statement
  - terms and conditions (with optional PDF downlaod)
  - returns policy
- Navbar containing links to:
  - home page
  - products page
  - contact form
  - user sign in / sign out
    - After sign-in, menu becomes dropdown allowing access to profile
- Products page offers category filter as well as search bar 
- Contact form transcript is mailed to submitter as well as site mail
- Cart page linking to checkout
- Checkout with (test) payment system for credit card using Stripe
- Mail sent to user after checkout with list of items, submitted address for delivery and order ID
- Staff / Admin page added into the site
  - easier order handling (items and delivery address shown, button to mark order processed)
  - download button to retrieve a csv file with all users and their mail addresses for newsletter use
- Standard Django admin pages allowing addition of products, FAQ's and comment management for products
  - Complete overview of all orders as well, both processed and unprocessed

### Apps created
- Accounts
  - All basic Django user information with adjusted pages to conform to site overall looking
  - Provides the base for the profile page and the staff page
  - Changed from standard pages for password reset, login and registration

- Cart
  - Available across all apps
  - Also contains the logic for changing the content during checkout

- Checkout
  - Processing of order into payment and database

- Contact
  - Small app specifically for the contact form

- Infopages
  - Contains the 4 links in the footer of the page
  - Table created for FAQ, for easily adding Q&A through Django Admin

- Products
  - Provides the opening page to the site
  - Views for total products page and product detail page
  - Contains the Product comments

- Search
  - Search function based on text string returning results containing the string
  - Filter function to return a view based on category selected from the dropdown
  - Both options available within the products page

### Features Left to Implement
- Expand user's accounts to allow in-site order history and easy address filling
- Extended staff/admin in-site pages allowing:
  - product additions / modifications
  - full order history download
  - newsletter processing in-site
- Further sophistication of mails sent out

## Tech Used

### Technologies and outside sources:
- **HTML**, **CSS**, **Javascript**, **Python**
- **[Django](https://www.djangoproject.com)** version 1.11.18
  - Framework used for the site
  - Add-on for forms: django-crispy-forms
- **[Bootstrap](https://getbootstrap.com)** version 4.1.3
  - Used for the styling of the site
  - version used includes [popper.js](https://popper.js.org)
  - used with [jQuery](https://jquery.com) version 3.3.1
- **[Stripe](https://stripe.com/)** test version used for (m/f)aking payments. 
  - ***No actual payments can be made***
- **[Stack Overflow](https://stackoverflow.com/)**

## Wireframe and User Stories
- In the root of the repository is a document with stories and mockup drawings (though crude, they turned out more or less as envisioned)

## Testing

Testing was done every step of development, as well as automated using **[Travis](https://travis-ci.org)**

### Travis tests
- **Cart** tests to open cart and to change quantity of item
- **Checkout** tests to check forms
- **Infopages** tests to open separate pages and add an FAQ subject
- **Products** tests to verify templates used and verify naming in database

The files for testing (*tests.py*) can be found in the apps named above.

### Manual Tests
- Manual testing was entirely done by continuous testing of every step created
  - initial pages with just placeholders
  - manual addition of items through Django admin pages
  - processing data onto page placeholders
  - expand code and page continuously, updating python code or HTML as needed
  - make modifications to the mails to be sent out and immediately run tests from shop to verify
  - verify search valid by searching a word, reviewing resulting product(s)
    - perform the same search on page from Chrome to count resulting matches
  - create orders, add items to cart, break off checkout and continue shopping
  - modify item value to zero to get same effect as deletion
  - add to quantity in cart, reduce it in checkout and complete order
  - add comments to a product's detail page and refresh result to verify POST data isn't sent again
  - open a page to a link requiring login, without being logged in and verify re-directs
  
### Devices for testing
- Testing was done on the following browsers:
  - Safari
  - Google Chrome
  
- Mobile device testing was done:
  - Using Chrome's developer tools, emulating all available formats
  - iPhone 7+
    - iOS Safari
    - iOS Opera
    - iOS Chrome
  - iPad Air2
    - iOS Safari
    - iOS Opera
    - iOS Chrome

### Media and Information
- Product images and descriptions courtesy of the real Brickstickershop, owned by my brother
  - Payment Lego Figure found on Google
