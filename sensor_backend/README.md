# Sensor Monitoring Backend

## Overview

This project is a FastAPI backend developed for an IoT Sensor Monitoring System. The backend receives sensor readings from an ESP32 device, stores them in a MySQL database using SQLAlchemy, and provides API endpoints to retrieve the stored data.

The system is designed to act as the bridge between the hardware layer (ESP32) and future client applications that consume the sensor data.

---

## Technologies Used

* FastAPI
* MySQL
* SQLAlchemy
* Pydantic
* Python

---

## Features

* Store sensor readings in a MySQL database
* Retrieve stored readings through REST APIs
* Database integration using SQLAlchemy ORM
* Request validation using Pydantic models

---

## Database Schema

### readings

| Column      | Type                  |
| ----------- | --------------------- |
| id          | Integer (Primary Key) |
| device_id   | String                |
| temperature | Float                 |
| humidity    | Float                 |

---

## API Endpoints

### POST /readings

Stores a new sensor reading in the database.

Example Request:

```json
{
  "device_id": "ESP32_001",
  "temperature": 29.5,
  "humidity": 65.2
}
```

### GET /readings

Returns all stored sensor readings.

---

## My Contribution

* Designed and developed the FastAPI backend.
* Connected FastAPI with MySQL using SQLAlchemy.
* Created database models and Pydantic schemas.
* Implemented POST and GET endpoints for sensor readings.
* Tested API functionality and database persistence.

---

## Team Collaboration

The ESP32 Simulator used for generating and sending sensor data was developed by a teammate for integration testing. My responsibility was to build the backend and database layer that receives, validates, stores, and serves the sensor data.

---

## Outcome

Successfully created a backend system capable of receiving sensor readings from an ESP32-based device (via simulator during development), storing them in MySQL, and exposing the data through REST API endpoints.
