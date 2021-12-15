# Game Guides Code Sample

I'm not in my twenties anymore, so I don't have nearly as much time for gaming as I used to. When I
do, though, I like to rescue all the puppies, fight all the baddies, and gather every single item,
even if I already have six Wands of Destruction. I'm an organized guy, and sometimes it's weeks or
months between play sessions. So the idea here was to make a simple checklist / guide for games
that you could share with friends or publicly.

## Frontend

The frontend is a single-page Vue.js / Tailwind application, served (in test/production) as a
static website. The local development environment uses [Vue CLI](https://cli.vuejs.org/) to serve
changes to the frontend in real-time to the browser.

## Backend

On the backend, this project uses a Python, Django, the
[Django REST framework](https://www.django-rest-framework.org/), and
[dj-rest-auth](https://pypi.org/project/dj-rest-auth/) to run a RESTful API.

## What's Here and What's Coming

The current version (0.1.0) has a working development deployment with authentication. It has a
placeholder for the Dashboard, and it doesn't really _do_ anything yet.

The next version, I'll copy over the API and UI features for creating a simple checklist for a game
and displaying it to the user.

I had a module that would allow OAuth logins through the Steam service and would get your owned and
most-played games from your account. I'd like to add this back to the code sample when I get the
time.

## Fate of this Project

I haven't abandoned this little project, but I did take the useful bits to a Serverless
Architecture. So, the idea is still there, but it isn't going to be completed with a Django/Docker
backend.

## Installation

This should work on any system with Docker and the ability to run Linux scripts.

Generate a dev environment and some randomized passwords:

```shell
./gen-passwords.sh dev
```

You may want to customize the dev.env file, and then:

```shell
./deploy-dev.sh
```