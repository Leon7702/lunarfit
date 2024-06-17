# Lunarfit App (frontend)

Lunarfit project for IMI

## Install the dependencies

Before starting the project, install the project dependencies with:

```bash
yarn
# or
npm install
```

This will install all the necessary packages for the project.


### Start the app in development mode (hot-code reloading, error reporting, etc.)
```bash
quasar dev
```


### Lint the files
```bash
yarn lint
# or
npm run lint
```


### Format the files
```bash
yarn format
# or
npm run format
```


### Build the app for production
```bash
quasar build
```

### Customize the configuration
See [Configuring quasar.config.js](https://v2.quasar.dev/quasar-cli-vite/quasar-config-js).



## Using the JSON-server for Frontend Development

### Create data

Define your data inside the `db.json` file. This JSON data can be an array of objects or an object with nested objects. Each object represents a data entity and should each have a unique id.
The `db.json` file will act as the data source for `json-server`.


### Start the JSON Server

You can start the `json-server` with the following command:

```bash
npm run json-server
```

This will start the `json-server` and watch the `db.json` file for changes. The server will run on `http://localhost:3000` by default.
So this means, you can then view this in your browser on port 3000.

The JSON Server automatically generate RESTful endpoints based on the data you defined in your `db.json` file.


### Stop the JSON Server

To stop the `json-server`, press `Ctrl + C` in the terminal where the server is running. This will interrupt the process and stop the server.


## Additional Resources

For more information about using `json-server` for frontend development, you can visit the following websites:

- [How to Use JSON Server for Front-end Development](https://www.freecodecamp.org/news/json-server-for-frontend-development/)
