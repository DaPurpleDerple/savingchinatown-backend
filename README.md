This is the backend for [SavingChinatown.org](https://www.savingchinatown.org), forked from [the code](https://github.com/mikeyk/saveourfaves-server) by Mikey K.

It's a fairly straightforward Django app with Postgres/PostGIS backing it for the 'nearby' queries. You'll also need [the React frontend](https://github.com/DaPurpleDerple/savingchinatown-frontend). It also uses `nginx` as the load balancer and file server for the static files/React app.

## Setting up the server
* Install Docker on your machine
* Create a `certificates` folder at `../certificates/` and place in the following:
    * HTTPS Certificates using `letsencrypt` and put the results of `/etc/letsencrypt/` into `/certificates/letsencrypt/`. If you aren't using HTTPS, edit `nginx/nginx.conf` to remove the HTTPS/letsencrypt references
    * An `htpasswd` formatted file named `nginx_auth` (this is used to password-protect the Django admin site; there’s also Django’s standard auth there, but this adds another optional layer.)
    * A `private_keys.py` file with the following format:
```
GOOGLE_PLACES_API_KEY = "" # Your Google Places API Key
EMAIL_HOST_USER = "" # Your SMTP Server (by default SendGrid) User to send emails, or leave blank to not use emails
EMAIL_HOST_PASSWORD = "" # Your SMTP Server (by default SendGrid) Password to send emails, or leave blank to not use emails
```

* From the root folder, run `docker-compose up -d`  to bring up all the services
* You’ll want to edit `nginx/nginx.conf` and `.env.dev` to match the hostname you’re trying to deploy to. To quickly test if this is all working on your local machine, you can connect to `localhost`
* Log into the Django container using `docker exec -it <name of Django container> /bin/bash`
    * Set up the Django admin account with `python manage.py createsuperuser`
    * Set up the DB with `python manage.py migrate`
    * Set up the Django admin site with `python manage.py collectstatic`

At this point you should have a running Django instance on `localhost/admin`. You should then create at least one `Area` object (major areas, such as by cities), a few `Neighborhood` objects inside each `Area`, and then add some `Places` to each `Neighborhood`. Once you’ve done all of that, you can run:

```
# log into the Docker container running Django
docker exec -it <name of Django container> /bin/bash
cd /usr/local/site
python scripts/dump_areas.py Areas.js
python scripts/dump_neighborhoods.py Neighborhoods.js
python scripts/dump_places.py Places.js
```

At that point, you can copy the `Areas.js`, `Neighborhoods.js`, and `Places.js` files into the savingchinatown-frontend repository; use them to overwrite the ones in `src/CityData/`.

## Running on Prod
* In both `docker-compose.yml` and `.env.dev`, change the `DB_PASSWORD` field
* Generate a new `SECRET_KEY` for `.env.dev` and set `DEBUG=0` 
