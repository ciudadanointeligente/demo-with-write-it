demo-with-write-it
==================

Demo using write-it as a django-app, this is intended to be just an example of using write-it as an embeded app. Write-it still has some logic very coupled to it.

Installation
------------

For installing this very simple app, we need to run the following


Create a virtualenv
`virtualenv demo`

Install the requirements


`pip install -r requirements.txt`

Install demo data

`python manage.py loaddata example_data.yaml`

Run the server

`python manage.py runserver`

Bugs and suggestions 
--------------------

Please report us any suggestions or bugs at the [write-it repo](https://github.com/ciudadanointeligente/write-it/issues).