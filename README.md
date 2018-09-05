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

## Contributing to the project

