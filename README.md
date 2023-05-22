# Getting started

To start the project, first install dependencies:
```
make install
```

Then, start Django server by running:
```
make start
```

# Using the server

Once the server is running, send a GET request to `localhost:8000` passing connectiong string as a `connection_string` parameter. For example:
```
curl "http://localhost:8000/metadata/?connection_string=postgresql://localhost/database_name"
```
