# subsunday
A sub sunday website that will be coming soon-ish for lirik.

https://twitch.tv/lirik

### How to start hacking ?

The easiest way is to first get `docker` and `docker-compose`:
simple way to get docker:
```sh
curl -fsSL get.docker.com | sudo sh
```
simple way to get docker-compose:
```sh
sudo -i
curl -L https://github.com/docker/compose/releases/download/1.15.0/docker-compose-`uname-s`-`uname -m` -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
```

Then, from the root of the project, start by populating the database once:
```sh
./scripts/dev up -d datastore # starts up the db
./scripts/admin run --rm populate-datastore
```

and then just start all the services:
```sh
./scripts/dev up -d
```

You can check the logs using:
```sh
./scripts/dev logs -f
# or
./scripts/dev logs -f specific_service
```

More information by using:
```sh
./scripts/dev help
```
or by reading the [docker-compose documention](https://docs.docker.com/compose/)

### Repository structure summary

The root of the repository is composed of a `backend` and a `frontend` root folder as well as a a docker-compose service description file that will serve as a base for the project's orchestration.
There are currently 3 services defined in it:
 - `web` : the webserver used as an entrypoint for all the requests. It currently builds the image described in `frontend/server` which just uses an `nginx 1.13` as a base and uses the configuration present in that same folder
- `api`: the backend app written in python which embeds a small webserver which will serve the api and will be proxied by the `web` service above
- `datastore`: the persistent layer. Currently building the image described in `backed/datastore` which just uses a `postgresql 9.6` as a base and uses a mounted docker volume called `subsunday-data` to store the data

You will also find a `scripts` folder that contains docker-compose overrides files and handy bash one-liner scripts to invoke them:
- `docker-compose.dev.yaml` contains overrides suitable for a development environment. It currently defines a different exposed network port for nginx and an environment variable used to tell the python api webserver to run in debug mode. This is the override you should be using if you're hacking on the backend. You can invoke this override by calling the handy `./scripts/dev` script from the root of the repository
- `docker-compose.prod.yaml` contains overrides suitable for a production environment. It currently exposes real world network ports. Use it with the `./scripts/prod` helper script.
- `docker-compose.admin.yaml` contains additional one off services useful for administrative tasks. It currently contains one service that can be used to seed the database using models from the api. Use it with `./scripts/admin`
