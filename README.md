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

Testing was aided by the service [BrowserStack](http://browserstack.com) for testing on different browsers, phones
and tablets. Supporting test screenshots were provided in the testingimages folder supplied.
Manual testing was done via iPhone 6 Plus.

Testing for the project was iterative, focusing on more trial and error design. A drawback to my approach is noted
by the lack of test code. This could be due to some time constraints mixed in with current comfortability with the
concepts. Future projects will have more emphasis in building this lack of skill in this area.

## Testing PayPal Donations

To test the donations page, use email:

`zanirontest9@test.com`

This will use the test account for the sandbox mode of PayPal's API. This will save you from spending real money to 
test out the functionality! All of the test payment details are saved, you can use any string of text as the password.

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

With all of the code in place, contributing to the project is simple. Download the project using 
`git clone https://github.com/Zaniron/StreamThreeGameDev.git` to starting working.

To test code locally, run `python manage.py runserver --setting=setting.dev` and find the project up on
`localhost:8000`

Heroku is set to auto deploy from the github project, so to push any changes to go live:

```
git add .
git commit -m "commit message"
git push
```

Pushing any local database changes, run:

`heroku run --app streamthreegamedev python manage.py migrate --settings=settings.staging`

This will update any databases and tables, but not populate them.

`python manage.py dumpdata --natural-foreign -e contenttypes -e auth.Permission --indent=4 > db.json --settings=settings.dev`

Then: `heroku run --app streamthreegamedev python manage.py loaddata db.json --settings=settings.staging`

This will update and populate the tables, make sure everything is pushed back to GitHub.

## Extra Notes

Thanks to [The Code Institute](http://lms.codeinstitute.net/) I was able to build this multi app website. By following
through their units as reference I was able to build the multiple sites and diverge from the path where I needed to
build the website I needed. Using the resources available I was able to learn all the systems in place, while leaving
room for me to expand and research separately where I needed extra help. 
