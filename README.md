[![BrickStickerShop](https://s3-eu-west-1.amazonaws.com/bss-msp-4/static/images/logo.1.png)](https://bss-msp-4.herokuapp.com)   
Travis says:  
[![Build Status](https://travis-ci.org/arjanvdmeij/msp4-bricksticker.svg?branch=master)](https://travis-ci.org/arjanvdmeij/msp4-bricksticker)  
The logo up here is clickable for the live site, but alternatively you can click 
[**here**](https://bss-msp-4.herokuapp.com)

This is the fourth project created for the Full Stack Web Developer course by [**Code Institute**](https://codeinstitute.net).  
The goal here was to create a full stack application, using Django with multiple apps and (in my case) a PostGres database.  

For the project, I recreated my brother's site, as a template to eventually update his actual webshop as well.
Anything a regular user of a webshop should be able to do is present. With the exception of actually receiving any ordered items.
The site contains a good number of items, however the total number of items is far less than eventually would be in a live version.

For the project, **Django** was used as framework, with **Heroku** for site and database hosting and **Amazon (AWS)** for file storage.

## UX
 
With a site that is aimed at Lego enthusiasts, specifically those looking for replacement stickers for their sets, one of the requirements
is to immediately show the latest additions to the site, and provide a way for them to subscribe to a newsletter if wanted.
The site overall needs to have a search option, both by category or by keyword.  
Aside from the above, cart contents must be changeable, where the quantity needs to be adjustable, or the item can be removed from the cart entirely. 
If and when an item is unavailable, an option needs to be in place for people to contact the shop owner and request the addition of an item.
Last but certainly not least, customers need to be able to place their actual order and receive a receipt for their placed order.

All the above is available in this site. Along with the above, additional information is available in the form of a FAQ page, as well as pages offering 
the privacy policy, the terms and conditions and the returns policy.  
  
- Unregistered user can browse the site, perform searches, filtering, and make purchases.  
- Registered users can do the same, but also receive the newsletter and have a profile page where they can remove their own account to opt out of the newsletter.  
- Staff members cannot remove their accounts through the profile. They do have access to a staff page where they can add products, handle order, add FAQ items and 
downlaod a csv file for newsletter purposes. In the admin panel they can also modify and delete items. They can not perform user management there.
- The superuser can do what staff members can, plus perform user management in the admin panel, as well as group management.

#### Wireframe and User Stories
For user stories and wireframe mockups created as part of this project, see the [**Word document**](https://github.com/arjanvdmeij/msp4-bricksticker/blob/master/MSP-4-Brickstickershop.docx) located in the root of this repository.

## Features
### Existing apps
The application holds a number of apps, carrying out various different tasks.
- **accounts**:  
   This app takes care of all tasks related to registering, signing in and out, and generation of the csv file for staff members
- **cart**:  
   This app ensures the cart is viewable, editable, and that its content can be used across the site 
- **checkout**:
   handles payments and order processing. Delivers staff the list of order items yet to be sent out
- **contact**:
   Fairly generic contact form, processing sending the form to site admins as well as submitter
- **infopages**:
   re-usable set of pages with generic information, including a model for easy adding of FAQ items
- **products**:
   home of the opening page, all products and product detail page. Holds models for products and comments on them, as well as staff form to add products.

### Existing Features
- Opening page with a banner, some info and basic links, followed by the 6 most recent additions to the site's inventory  
   **a.** *Optional* account creation for the use of newsletter subscribing. Account creation is explicitly *not* needed to make purchases
- Optionally, users can delete their account themselves to be removed from the newsletter through profile page
- Links to various information in the footer of the site, detailing information about:  
   **a.** products FAQ  
   **b.** privacy statement  
   **c.** terms and conditions (with optional PDF downlaod)  
   **d.** returns policy  
- Navbar containing links to:  
   **a.** home page  
   **b.** products page  
   **c.** contact form  
   **d.** user sign in / sign out - *After sign-in, menu becomes dropdown allowing access to profile and sign-out*
- Products page offers category filter as well as search bar 
- Contact form transcript is mailed to submitter as well as site's mail address
- Cart page linking to checkout page
- Checkout with (test) payment system for credit card using Stripe
- Mail sent to user after checkout with list of items, submitted address for delivery and order ID
- Staff / Admin page added into the site  
   **a.** page to add products to the catalog without the need to use Django Admin  
   **b.** page to add FAQ items without the need to use Django Admin  
   **c.** quick order handling (items and delivery address shown, button to mark order processed)  
   **d.** download button to retrieve a csv file with all users and their email addresses for newsletter use  
- Standard Django admin pages allow addition of products, FAQ's and comment management for products by staff members  
   **a.** offers complete overview of all orders as well, both processed and unprocessed

### Features Left to Implement  
- Expand user's accounts to allow:  
   **a.** in-site order history  
   **b.** easy address filling  
   **c.** saving the cart  
   **d.** forum option (in time)
- Extended staff/admin in-site pages allowing:  
   **a.** existing product modifications, as well as product comment management  
   **b.** full order history download  
   **c.** newsletter processing in-site
- Further sophistication of mails sent out
- Finish upgrade to Stripe v3
- Add more payment options

## Technologies Used
- **HTML**, **CSS**, **Javascript/jQuery**, **Python** were all at the heart of things
- [**Django**](https://www.djangoproject.com/) - The entire site uses **Django 1.11.20** as its framework  
   Django add-ons used:  
   *django-materializecss-form* - used for the styling of the forms in Materialize  
   *stripe* - used in processing of payments  
   *boto3* and *django-storages* - used for the AWS storage  
   *dj-database-url* - used for Heroku PostGres integration  
- [**MaterializeCSS**](https://materializecss.com) - The site is styled based on **MaterializeCSS 1.0.0**  
   *Originally the site was being developed using Bootstrap 4, but this was changed to MAterializeCSS.*  
   *The pages created up to the switch can be downloaded still however* [***HERE***](https://github.com/arjanvdmeij/msp4-bricksticker/blob/master/bss_booststrap.tar.gz)
   *should anyone want to build on those. An accompanying text file details which changes need to be made to switch to Bootstrap 4*
- [**Stripe**'s stripe.js](https://stripe.com/) - test version used for (m/f)aking payments.  
   *No actual payments can be made*  
   ***Cards to use in testing:***
   | Card Number      | Card Type       | Payment?        |
   |------------------|:---------------:|:---------------:|
   | 4242424242424242 | Visa            | Yes             |
   | 5555555555554444 | Mastercard      | Yes             |
   | 378282246310005  | AMEX            | Yes             |
   | 4000000000000127 | Visa            | No, cvc error   |
   | 4000000000009995 | Visa            | No, funds error |  
   In all card cases, a valid expiration should be provided.
   
- [**JQuery**](https://jquery.com) - The project uses **JQuery** to simplify DOM manipulation.  
   *Additional javascript was used to perform some enhancements as well, like smooth scrolling to the top of the page. Most of the* 
   *jQuery in use however is through MaterializeCSS, with some settings applied, with exception of added alert-box functionality.*

## Testing
Testing the site has been ongoing from the very start, with each and every addition tested manually and/or automated with the aid of
[**Travis CI**](https://travis-ci.org/).  
Every aspect of the site was tested manually extensively, even those tests that are automated.  

In the [**Word document**](https://github.com/arjanvdmeij/msp4-bricksticker/blob/master/MSP-4-Brickstickershop.docx) 
in the root of the repository, a chapter is dedicated
to the tests, including screenshots of manual testing, overview of automated tests and the result as Travis relays.  
Each app contains a `tests.py` file. In order to run all tests manually instead of using Travis, 
go to a terminal prompt, and enter `python3 manage.py test` to run all tests.  
In order to run tests for a specific app, enter (e.g.) `python3 manage.py products` where products is the app to run the tests for.

Testing was done every step of development, as well as automated using **[Travis](https://travis-ci.org)**


### Look and Feel on various browsers / devices
The site has been tested on multiple environments:  
   **a.** Google Chrome (Desktop) - *both direct and using developer tools to emulate devices (see f. below)*  
   **b.** Safari (Desktop)  
   **c.** Google Chrome (Mobile) - *installed on iPhone XR, 7+, iPad Air (1st gen) and iPad (2018)*  
   **d.** Safari (Mobile) - *installed on iPhone XR, 7+, iPad Air (1st gen) and iPad (2018)*  
   **e.** Opera (Mobile)
   **f.** Developer tools - *emulated versions of Pixel 2 (XL), iPhone 6/7/8(Plus) and X and iPad(Pro)*

Scaling on all devices works as intended. The site does not scale well to the tiny screens of iPhone 5 and/or Galxy S5. This was
a deliberate choice on my part, as those devices are not much used anymore by the target audience. The majority of traffic will
be coming from desktop and/or tablet sized browsers. I therefore chose to focus on those instead of (semi-)obsolete mobile phones.

### Bugs encountered
At present, there is a small 'bug' in the products page, where the search form shows as an ellips-like inputfield on iPhone.  
This is something that doesn't occur for any other form within the site. There is however no loss of functionality. 
It is a small bug that will need tending in time, however for the moment, it is left as is. The desktop version does not have this
same issue at all.

While 'rebooting' the site in a MaterializeCSS form, I ran into issues with stripe payments, where stripe.js wuold throw an error and not process payments.
After (a LOT) of trial and error, it turned out that adding in the CSS class `hide` into the form template directly, which is 
possible when using django-materializecss-form (e.g. `{{ payment_form.cvv | materializecss:'s3 hide'}}`), caused the form to fail.  
By the time that became clear, I was on route to upgrade from Stripe v2 to Stripe v3. This needs finishing still, but hiding the form field in its own
separate `div` solved the problem with payments.  

Another interesting bug was trying to apply migrations to the databse after I had split off a settings file specifically for the production environment on Heroku.
In booting on Heroku a check was built in to perform any migrations needed, which it did. Based on the general Dev/Travis configuration. And once done, boot the application
using the production settings. Needless to say settings are now integrated again in a single file and settings are applied based on an environment variable.  

Any other things I've run into were simply my fault, and corrected on-the-go whenever needed. Whenever a page was changed, adjustments were made to parts
broken elsewhere. This mostly applies to the HTML and CSS where changes for specific screensizes would break things. I do not consider those bugs however.  

## Deployment

For a description of the deployment process, see the corresponding chapter in the 
[**Word document**](https://github.com/arjanvdmeij/msp4-bricksticker/blob/master/MSP-4-Brickstickershop.docx) located in the root of the repository.
This chapter describes the current deployment, as well as the environment variables required in order to run the code locally, 
including creation of a `Staff` group within Django Admin for easy adding of staff members.

## Credits

### Content, Media and Acknowledgements
*Three headers rolled into one. There is a reason for that.*  

All content and media was obtained from my brother's webshop [**brickstickershop**](https://www.brickstickershop.com/?Lng=en)  
This site is also what inspired me to use this subject, both because it is close to the chest with him being my brother, 
and because like him, I've always had a weak spot for Lego, from a very young age already. His site deserves an overhaul,
this is my first step towards that goal, eventually applying a new look and feel to his site.

Thanks bro, for handing me everything needed to make this all work!
I owe you all the images, logos and descriptions (heck, even the prices!)