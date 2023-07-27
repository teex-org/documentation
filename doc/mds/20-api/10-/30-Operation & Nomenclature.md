# Summary of Functioning
The API handles 4 different tasks:

- Verify the authorization to perform the request.
- Request processing (verification of fields, existence of resources, etc.).
- Read and write to the database.
- Update the notifier.

Here is a brief presentation; refer to the associated pages for more details.

#### Authorization
To verify authorization, each route has access to the email of the calling user. Therefore, at the beginning of each processing, an API call is made to the database to retrieve the user's rights and ensure they correspond to the request.

#### Processing
The processing involves ensuring the integrity of the request body (no additional fields, correct types, etc.). Apart from that, the processing varies greatly between different routes.

#### Read/Write
Since SQLite3 does not have a native provider, it must be embedded in the server itself. Thus, the Python library acts as the provider, and SQL calls are made directly to the database provider without going through HTTP or other calls.

#### Update the Notifier
For each modification of the database (successful POST or PUT), the API will call the notifier service to inform that a modification has been made.

# Routes & Naming Convention
For the sake of simplicity and consistency in the different API routes, each route follows the same logic, regardless of the HTTP method:

```
URL:  {path}/{user email}
Body: {json data}
```

- Path: The standard REST path.
- User email: The end of the URL must be the email (identifier) of the user making the request.
- Body: All data passed is placed in the body, even for a GET request.

!!-Body: Each JSON body must follow the expected format by the API:<br>
No field (even unnecessary) can be added without triggering a 400 error.<br>
Refer to the specific documentation of the different routes to verify the expected bodies-!!

# Error Codes and Responses
## Formalism
All response bodies are in JSON format.

Responses to 200 requests may be without a body.

Responses to requests with errors are of the type `{'err','...'}`, even if the `...` is empty.

## Codes
HTTP error codes are respected, but custom error codes may be used.

Here is the list of custom error codes with their meanings:
ii-No custom codes are used at the moment-ii