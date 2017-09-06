# SubSunday Front End

This front-end was bootstrapped with [Create React App](https://github.com/facebookincubator/create-react-app) with Typescript.

You can find a guide on the most recent version of Create React App [here](https://github.com/facebookincubator/create-react-app/blob/master/packages/react-scripts/template/README.md).

The `app_builder` container is used to build the production code into the `build` folder. This is then mounted by the `web` container which acts as the actual web server, serving up the static production files. Alternatively, when running the development composer file this container can also be used for local development by running the app in development while mounting your local folder.

## FAQ

How do I start the app in development mode?

```sh
docker exec -it subsunday_app_builder_1 npm start
```

How do I view the site locally?

```sh
http://localhost:3000
```

How do I bash into the app container?

```sh
docker exec -it subsunday_app_builder_1 bash
```

How do I run the sass watcher?

```sh
docker exec -it subsunday_app_builder_1 npm run-script watch-css
```

How do I re-build the app so I can see what it would look like on the `web` container?

```sh
docker exec -it subsunday_app_builder_1 npm build
```