# Overview

The API doesn't handle **controller** authentication since all requests pass through the authentication proxy. Instead, it manages authentication tasks, including:

- Account creation
- Password change
- Login

The user authenticates using their password as a secret to retrieve a token. They use this token as proof of authentication to perform requests.

### Password
Passwords are stored in the database in the form of hashed passwords using the bcrypt algorithm.

The private key is stored in `./secrets/private_key.pem`.

### Token
**Note: Currently, the tokens are JWTs. This will be changed, but it will follow this documentation.**
Tokens are JSON objects of the following type:
```yaml
{
    claims : {
        user : email of the user,
        nonce : random int,
        exp : timestamp of expiration
    }
    signature: signature
}
```

# Routes

#### [GET] /auth/check/
check token in base
```yaml
{token: string}
```
---
#### [GET] /auth
get a new token 
```yaml
{
    email:  string
    pwd:    string    
}

```
```yaml
{
    token : string
}
```
---
#### [POST] /auth/user
create accunt and get new token
```yaml
{
    email:  string 
    name:   string 
    pwd:    string 

required: [email,name,pwd]
}
```
```yaml
{
    token : string
}
```
---
#### [PUT] /auth/user/pwd/?email
change password and get new token
```yaml
{pwd: string}
```
```yaml
{token: string}
```
