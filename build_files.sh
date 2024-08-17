#!/bin/bash

# Collect static files
python manage.py collectstatic --noinput

# Optionally, you can add other build steps here
