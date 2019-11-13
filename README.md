# Assembly


[Documentation](https://mardix.github.io/assembly)

**Assembly** is A mid stack, batteries included Flask  framework, that adds structure 
to your Flask application, and groups the endpoints by classes instead of loose functions. 

Technically **Assembly** is an attempt of making a simple framework based on Flask Great Again!

 
## Decisions made for you + Features

- Smart routing: automatically generates routes based on the classes and methods in your views

- Class name as the base url, ie: class UserAccount will be accessed at '/user-account'

- Class methods (action) could be accessed: hello_world(self) becomes 'hello-world'

- Smart Rendering without adding any blocks in your templates

- Auto rendering by returning a dict of None


- Templates are mapped as the model in the class the $module/$class/$method.html

- Markdown ready: Along with  HTML, it can also properly parse Markdown

- Auto route can be edited with @route()

- Restful: GET, POST, PUT, DELETE

- REST API Ready

- bcrypt is chosen as the password hasher

- Session: Redis, AWS S3, Google Storage, SQLite, MySQL, PostgreSQL

- ORM: [Active-Alchemy](https://github.com/mardix/active-alchemy) (SQLALchemy wrapper)

- Uses Arrow for dates 

- Active-Alchemy saves the datetime as arrow object, utc_now

- CSRF on all POST

- CloudStorage: Local, S3, Google Storage [Flask-Cloudy](https://github.com/mardix/flask-cloudy)

- Mailer (SES or SMTP)

- Caching



## Quickstart

#### Install Assembly

To install Assembly, it is highly recommended to use a virtualenv, in this case I 
use virtualenvwrapper 

    mkvirtualenv my-assembly-site

Install Assembly

    pip install assembly
    
#### Initialize your application

Now Assembly has been installed, let's create our first application

```
    cd your-dir
    
    asm-admin init
```


`asm-admin init` setup the structure along with the necessary files to get started

### Hello World

```

from assembly import (Assembly, response)

class Index(Assembly):
    
    index(self):
        return "Hello World"

    @response.json
    api(self):
        return {
            "name": "Assembly",
            "version": "x-to-infinity"
        }


```

 You will see a structure similar to this
 
    /your-dir
        |
        |__ .gitignore
        |
        |__ app.json
        |
        |__ requirements.txt
        |
        |__ assembly.py
        |
        |__ application/
            |
            |__ __init__.py
            |
            |__ config.py
            |
            |__ /models/
                |
                |__ __init__.py
                |
                |__ models.py
            |
            |__ /views/
                |
                |__ __init__.py
                |
                |__ main.py
            |
            |__ /templates/
                | 
                |__ /layouts/
                    | 
                    |__ base.jade
                |
                |__ /main/
                    |
                    |__ /Index/
                        |
                        |__ index.jade
            |
            |__ /static/
                |
                |__ assets.yml
                |
                |__ package.json
            |
            |__ /data/
                |
                |__ babel.cfg
                |
                |__ /uploads/
                |
                |__ /babel/
                |
                |__ /mail-templates/
            |
            |__ /lib/


 
#### Serve your first application

If everything is all set, all you need to do now is run your site:

    asm-admin server
    
It will start serving your application by default at `127.0.0.1:5000`

Go to http://127.0.0.1:5000/ 

---

I hope this wasn't too hard. Now Read The Docs at [http://mardix.github.io/assembly/](http://mardix.github.io/assembly/)
for more 

Thanks, 

Mardix :) 

--- 

## Read The Docs

To dive into the documentation, Read the docs @ [http://mardix.github.io/assembly/](http://mardix.github.io/assembly/)

---

License MIT

Copyright: 2019 - Forever Mardix

