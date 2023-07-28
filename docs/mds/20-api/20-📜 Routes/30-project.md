#### [GET] /project/?email
```yaml
{id: integer}
```
```yaml
{   
    id:     string
    name:   string
}
```
-
#### [POST] /user/?email 
```yaml
{name: string}
```
```yaml      
{id: new_id}
```
-
#### [PUT] /project/?email
```yaml
{
    id:     integer
    name:   string
}
```
-
#### [DELETE] /project/?email
```yaml
{id: integer}
```
-
#### [GET] /project/users/?email
```yaml
{id: integer}
```
```yaml
{
    id_project:     integer
    users : [
        email:      string
        rights:     string
    ]
}
```
-
#### [PUT] /project/user/?email
```yaml
{
    id:     integer
    email:  string
}
```
-
#### [PUT] /project/user/owner/?email
```yaml
{
    id:     integer
    email:  string
}
```
-
#### [GET] /project/lists/?email
```yaml
{id: integer}
```
```yaml
{
    id:     integer
    name:   string
    lists: [
        id:     integer
        name:   string 
        tasks : [
            id:         integer        
            name:       string     
            tag:        integer              
            priority:   integer        
            state:      integer          
        ]
    ]
    users:[
        email: string
    ]
}
```
-
#### [DELETE] /project/user?email
