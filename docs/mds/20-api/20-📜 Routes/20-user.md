# routes

#### [GET] /user/<email>
```yaml
{email: string}
```
```yaml
{
    email: string,
    name: string
}
```
-
#### [PUT] /user
 ```yaml
{
    name:     string,
    pwd:      string
}
```
```yaml
{
    projects : [
        {
            id: int,
            name: string
        }
    ]
}
```
-
#### [DELETE] /user/<email>
