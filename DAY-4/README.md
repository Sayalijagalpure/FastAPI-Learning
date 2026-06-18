# Day 4 - FastAPI with MySQL

## Overview

Today I connected a FastAPI application to a MySQL database using SQLAlchemy. I configured the database connection using a `.env` file and created API endpoints to store and retrieve device readings from MySQL.

## Topics Covered

- SQLAlchemy ORM
- MySQL Connector
- Database Sessions
- Environment Variables (`.env`)
- Model-to-Table Mapping
- GET and POST Endpoints

## Task Completed

- Connected FastAPI to MySQL
- Created a `readings` table model
- Implemented a POST endpoint to save readings
- Implemented a GET endpoint to fetch readings
- Tested all endpoints using Swagger UI

## Outcome

Successfully built a FastAPI application that stores device readings in MySQL and retrieves them through API endpoints, making the data persistent across server restarts.