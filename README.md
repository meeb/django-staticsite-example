# django-staticsite-example

This is a complete working example of how to build a static site with Django,
and Django Static Site.

 * [Django](https://www.djangoproject.com/)
 * [Django Static Site](https://github.com/meeb/django-staticsite)

This site is fully working and a live demo if this sites output is available
here, hosted on Cloudflare pages:

https://django-staticsite-example.meeb.org/

This example is slightly unusual in that it commits the SQLite database
with the content into the repository, this is fine for single developer or
small teams, however larger sites with a lot of content should use a secured
external database or you'll end up overwriting each others content edits with
endless merge conflicts.


# Usage

You can use this style of site generation on any platform which supports
continuous deployment, good (and free or low cost) examples being:

 * [Cloudflare pages](https://pages.cloudflare.com/)
 * [Netlify](https://netlify.com/)
 * [GitLab Pages](https://docs.gitlab.com/ee/user/project/pages/)

This example repo includes working demo content and a working Django admin. To
get it working, just clone this repository and install the requirements (note:
requires "make" to be installed):

```bash
$ uv sync
```

Then run the development server:

```bash
$ make runserver
```

You should be able to access the site on your local development server at
[http://127.0.0.1:8000/](http://127.0.0.1:8000/). The admin is at
[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin) and the default
credentials are:

* Username: `blogadmin`
* Password: `blogadmin`

**Note** This is obviously not at all secure, the static site once generated is
secure, however the Django interface is *only* suitable for local development
and content editing on a secure computer. If you want to secure the development
server interface make sure you change the `SECRET_KEY` to something sensible
(and store it in an environment variable).

To build a static website:

```bash
$ make staticsite
```

And you static site will be in the `docs` directory.

See the `Makefile` for more command examples.


# Deployment example on Cloudflare Pages

1. Clone this repo
2. Log into your Cloudflare account and go to "Workers & Pages" under "compute"
3. Follow the steps to link your GitHub account to Cloudflare and grant access to your cloned repo
4. For "build command" enter `make staticsite`
5. For the "build output directory" enter `docs`
6. Click deploy
