### Hexlet tests and linter status:
[![Actions Status](https://github.com/Osayanny/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Osayanny/python-project-52/actions)
[![Maintainability](https://qlty.sh/badges/42954886-5c52-4a2b-8061-721d468bfa59/maintainability.svg)](https://qlty.sh/gh/Osayanny/projects/python-project-52)
[![Code Coverage](https://qlty.sh/badges/42954886-5c52-4a2b-8061-721d468bfa59/test_coverage.svg)](https://qlty.sh/gh/Osayanny/projects/python-project-52)


# Task Manager

Task Manager is a web application for organizing work tasks. You need to register before using it. Users can create tasks, assign an executor to them, and assign specific labels to these tasks.

## Demo

Demo on render.com

[![Task Manager](https://python-project-52-eyl8.onrender.com/)](https://python-project-52-eyl8.onrender.com/)


## Tech Stack

**python:** >3.10

**django:** >=5.1.5



## Run Locally

Clone the project

```bash
  git clone git@github.com:Osayanny/python-project-52.git
```

Go to the project directory

```bash
  cd python-project-52
```

Install dependencies

```bash
  make build
```

Start the server

```bash
  make start
```


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`DEBUG` - True or False

`SECRET_KEY` - your secret key

`ACCESS_TOKEN` - for integrate rollbar

