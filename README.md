# piano-ninja

Django powered website to display piano listing information.

## Setup
```bash
# start server
python manage.py runserver
```
Goes to http://localhost:8000/pianos/

Dev guide
```shell
python manage.py shell
>>>from pianos.models import Pianos
>>>Pianos.objects.using("pianos").all() 
```

## Usage
```bash
```
