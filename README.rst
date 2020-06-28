Flaskr
======

This example application it highly based on the basic blog app built in the Flask `tutorial`_ (upstream), but with some modifications.

.. _tutorial: http://flask.pocoo.org/docs/tutorial/


Install and run
---------------

**Instruction from the upstream** Run the following commands to install. ::

    $ git clone https://github.com/italovalcy/myapp-flask
    $ cd myapp-flask
    $ python3 -m venv venv
    $ . venv/bin/activate
    $ pip install -r requirements.txt


To run::

    $ export FLASK_APP=flaskr
    $ export FLASK_ENV=development
    $ flask init-db
    $ flask run

Open http://127.0.0.1:5000 in a browser.


Test
----

Run test and coverage report::

    $ coverage run -m pytest
    $ coverage report

To run acceptance tests::

    $ echo todo

Docker image
------------

To build the docker image::

    $ docker build -t myapp-flask:latest .

To run the the container::

    $ docker run -d -p 8080:8080 myapp-flask:latest
