#!/usr/bin/env bash
git init
git add .
git commit -m "initial commit"
{% if cookiecutter.has_remote|lower == 'y' %}
git remote add origin {{ cookiecutter.github_url }}
git remote -v
{% endif %}

