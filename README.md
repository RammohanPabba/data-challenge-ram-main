# Zepto Data Engineer Challenge

## Problem

You work as a data engineer for a company that operates a payments service for Ecommerce companies. Over the years, the application team has successfully scaled the payments service to handle a high volume of transactions. However, they have not yet transitioned away from an old data table that contains transaction information.

Every day, the payments service exports CSV files into a designated folder, and these files are then handed over to the data team. All this data is fictional (produced by Faker).

### Requirements

Your task is to implement a straightforward data pipeline/s that fulfil the following:
- Ingests the data from the CSV files
- Cleans and prepares the data
- Establishes foundational data models (to be used in future analytics data models)

The above requirements are fairly broad, so use this as an opportunity to demonstrate your interpretation and skills.

### Follow-up
After completing this task, the engineering team has requested your insights on the following points:
- What improvements could the application team make to improve the quality of the raw data?
- What considerations do we need to keep in mind for this pipeline if the number of transactions increases by a factor of 1000 and they are sent every 5 minutes?
- The new analytics data is becoming critical to our operations. How can we ensure that it accurately represents all the data in the transaction system?

## Setup

We have provided a folder with 7 days worth of transaction data.

For your convenience we have created a skeleton Python application with the following tools:

- [Docker](https://www.docker.com/) for an empty Postgres DB
- [Make](https://www.gnu.org/software/make/) for build tasks
- [Github Actions](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions) for CI

## Getting Started
Use `make install` to install dependencies
```
❯ make install

pip install poetry
poetry install
```
Use `make run` to execute the cli with the default data. There is a data/ directory with more example scenarios.
```
❯ make run

docker-compose up && \
poetry run python ./data_extractor/main.py
```

Use `make test` to run all tests.
```
❯ make test

poetry run pytest
```

Use `make lint` to check code for style issues.
```
❯ make lint
poetry run black .
```

## What we are looking for

**Communication**

At Zepto we are a remote first company so communication is very important. Help us to understand your thinking, concerns and any limitations of your solution.

Here are some of the tools at your disposal to help you do this:

- readme
- docs
- commit history
- code comments
- tests
- pull request description
- pull request comments

**Architecture**

We understand this exercise doesn't work on the same volume/complexity found in everyday work. However, some of the follow-up questions are positioned to offer the opportunity to demonstrate different tools/techniques that could be employed at scale.

**Reliability**

At Zepto the quality and security of the data is important to ensure we provide our customers with the critical information. Incorrect or lost data can have an immediate monetary impact on our customers. Testing and monitoring are high priorities for the engineering team at Zepto

## Requirements

- Submit your solution as a GitHub pull request so we can have a conversation with you
