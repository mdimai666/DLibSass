# DLibSass

This lib default compress and append css source_map

## Install 
copy file

## Usage

> Full Tutorial HERE https://django-assets.readthedocs.io/en/latest/#quickstart

```
from mynamespace.DLibSass import DLibSass

scss_output = '../static/css/bundle.css'

sass = Bundle('../assets/css/style.scss',
            depends=["../assets/css/**/*.scss", "../assets/css/*.scss"],
            filters=DLibSass, output=scss_output)
register('css_all', sass)
```
