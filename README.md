
# How to run? 

```shell
docker-compose -f local.yml build
docker-compose -f local.yml run
```

Then go to http://0.0.0.0:8000/

I used cookie cutter which gives me default register/login interface. You can create user by registering through that
interface or create user from console with the following command
```shell
docker-compose -f local.yml run --rm django python manage.py createsuperuser
```

The parts that are interested for the interviewer are in modules:
1. `eycars.cars`
2. `eycars.client`

There is available redoc or swagger
http://0.0.0.0:8000/api/redoc/

## Client Module

This module is responsible for communication with external APIs.\
The only responsibility is to fetch and parse data.

### Why marshmallow not DRF serializers and django related stuff?
It should be a standalone module without any coupling to the eycars project. Thanks to that we can also 
reuse it in not django projects. That should be separate app/project but for simplicity and because of time
restriction I left it in the project. 

If I had more time and there would be performance concern I could make this module `async` and use it with `async` 
django views, but it is time-consuming. I can elaborate about it more on interview.


## Cars module

* For the sake of time and simplicity I wasn't loading the full `Make` object from external API
* I choose name `CarModel` instead of `Model` to avoid name issues.

Regarding `Rating` model normally I would create more generic solution using `contenttype` module.
So that could be reused across application.


## Important
Everything should work as in requirements of the task.
As you can see there are no tests, and the app isn't deployed anywhere. I had other staff that I had to do during this 
weekend.

I can write beautiful `unit` and `ete` tests and deploy it on my app server on the first of april because this
is the first day of my holidays. Due to the current job load I won't be able to do it earlier. 
