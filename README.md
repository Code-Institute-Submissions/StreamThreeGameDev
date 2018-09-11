# Zaniron Games

A public game development blog and hub for devs and customers.

## Overview

### What is it for?

The purpose of this multi-app website is to provide a way for this games studio to promote their new game through a
public 'dev diary'. Dev's can create an account to be able to contribute to the blog and also make use of the task 
management system. Fans and prospective customers can see the development live happening, seeing what mechanics are
being developed now. The public can also donate to the project through paypal payments and comment on blog posts.

### Included Features

- Blog App
    - Create and edit blog posts if you are logged in.
    - Blog posts consist of title, description, image and tags.
    - [Discus](https://disqus.com/), adding in a comment system to the blogs. Allowing users to comment on
    posts, voicing their opinions and excitement.
- Task Manager
    - Create and edit tasks if you are logged in.
    - Tasks consist of title, status choice and description
    - Overlay on hover, showing author and creation date of the task
- Donations
    - [PayPal API](https://developer.paypal.com/), utilising PayPal to handle donations. For users to contribute to
    the creation of the game project.
    - Users can donate from £1 to £100 using a single payment system set up with PayPal
- User Registration and Login
    - Contributers to the project can create an account, which data is saved into the SQL Database
    - Once logged in, contributers can make blog posts and tasks.
    - When one of these is created, the username/email is attached to that object.

## Tech Used

### Some of the tech used includes:

- Django
- Disqus
- PayPal API
- SQL Database

## Scope

Trying to scale back on my over estimation of the previous project, it was paramount that I try to plan a project
that hit all the criteria at it's most basic. A minimum viable product that did what it had to do. Throughout the 
development, the only major change was the initial use of the Django REST Framework. This was initially going to 
be used for the task management system, but was scrapped due to struggling to get to grips with utilising it with 
HTML templates. It was functional within a class based view, but didn't fit within the theme of the website.

The plan was for logged in users to see the class based view, to add and edit tasks, and for logged out users to 
see the data within a template view. This was becoming too time consuming for the constraints of the project, time
running out so it was scrapped in favour of a simpler style.

## Testing



## Maintained Issues

The biggest issue I feel that is maintained is just the simplicity. Despite being fully functional, and doing what it
needs to do, it's not the flashiest of websites. Although this is a minor issue that comes down to time constraints in
the development process.

Some glitches can be noticed when displaying the project on tablet, mostly with the overlay box over the task boxes
on the task management view.

## Hosting

This site is hosted using the [Heroku](http://heroku.com) platform.

To host this project, a few steps need to be made:

- Separate settings into, base, dev and staging files.
    - This is for hosting locally for testing updates and changes etc.
    - Also don't want users to have access to debug settings.
- Sign up to Heroku and create a new app.
- Create a `Procfile` and `Procfile.local` (for running on windows)
- Push changes to Github
- Link Heroku app to project on Github
- Install `CLEARDB` on Heroku
- Link database
    - install `dj-database-url`
    - use this to link to the CLEARDB
    - run `heroku run --app streamthreegamedev python manage.py migrate --settings=setting.staging`
    - this is the most important step, for setting the database tables on the hosted version
- Populate the database
    - create a JSON dumpfile of the data
    - `python manage.py dumpdata --natural-foreign -e contenttypes -e auth.Permission --indent=4 > db.json --settings=settings.dev`
    - push to Github
    - `heroku run --app streamthreegamedev python manage.py loaddata db.json --settings=settings.staging`

With these steps done, the project is fully hosted. When initially hosting, I missed steps, causing problems with 
populating the database and the loading of the staticfiles. Once the whitenoise library was better integrated and
setting STATIC_ROOT in the settings, everything loaded!

## Contributing to the project

