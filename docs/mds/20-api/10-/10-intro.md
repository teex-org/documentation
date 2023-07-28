This section is intended for the API. It documents its general functionalities and usage.

The API is the logical interface of the database, allowing the following:

- Manage authentication
- Manage authorization
- Read and write to the database

# Technologies
The API is coded in Python using the Flask.py web server, which enables the creation of a RESTful API.

The database is an SQLite3 database directly integrated into the API.

# Structure
```
.
├── database
│   ├── create.sh         - script to create SQL tables
│   └── database.sqlite   - SQLite3 database file
│
├── router                - API routes organization
│   ├── auth.py
│   ├── list.py
│   ├── project.py
│   ├── task.py
│   ├── user.py
│   └── yagni.py
│
├── secrets
│   ├── private_key.pem   - private key for signing tokens
│   └── public_key.pem    - public key for checking tokens
│
├── tools
│   ├── db.py             - useful functions for the database
│   ├── jsonchecker.py    - functions for testing JSON format
│   └── logs.py           - functions for better logs, replacing 'print'
│
├── env.py                - store environment variables
├── requirements.txt      - all Python dependencies
├── testing.py            - run a test scenario
├── run.sh                - run the API server with Python control before
└── api.py                - entrypoint Flask
```