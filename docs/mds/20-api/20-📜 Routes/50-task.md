
#### [GET] /task/?email

```yaml
{id: integer}
```
```yaml
{
    'id':               integer
    "name" :            string
    "tag" :             integer
    "priority" :        integer
    "state" :           integer
    "descr" :           string
    "id_last_editor" :  integer
    "id_list" :         integer
}
```
-
#### [POST] /task/?email
```yaml
{    
    id_list:    integer
    name:       string
    tag:        integer
    priority:   integer 
}
```
```yaml         
{id: string}
```
-
#### [PUT] /task/metadata/?email
```yaml
{
    id:         integer
    (name):     string
    (tag):      integer
    (priority): integer
}
```
-
#### [PUT] /task/state/?email
```yaml
{            
    id:     integer
    state:  integer
}
```
-
#### [DELETE] /task/?email
```yaml
{id: integer}
```


