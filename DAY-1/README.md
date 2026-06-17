# Day 1 - FastAPI Fundamentals

## Overview

Today I started learning FastAPI and explored the basic concepts required to build APIs. I learned how to set up a FastAPI project, create a virtual environment, run the development server, and test APIs using Swagger UI.

The focus of this session was understanding how FastAPI works and creating simple GET endpoints using path and query parameters.

---

## Topics Covered

* Virtual Environment (venv)
* FastAPI Installation
* Uvicorn Server
* FastAPI Project Structure
* GET Requests
* Path Parameters
* Query Parameters
* JSON Responses
* Python Type Hints
* Swagger UI Documentation

---

## Concepts Learned

### Virtual Environment

Created and activated a virtual environment to manage project dependencies separately from the system Python installation.

### FastAPI Setup

Installed FastAPI and Uvicorn and created the first FastAPI application.

### GET Endpoints

Learned how to create endpoints that respond to GET requests.

### Path Parameters

Used path parameters to pass values through the URL and access specific resources.

Example:

```python
@app.get("/students/{student_id}")
```

### Query Parameters

Used query parameters to send additional information through the URL.

Example:

```python
@app.get("/search")
def search_student(name: str):
```

### JSON Responses

Returned Python dictionaries as JSON responses from API endpoints.

### Swagger UI

Tested API endpoints using FastAPI's automatically generated Swagger documentation.

---

## Practice Project

Built a simple API with multiple GET endpoints to understand routing and parameter handling.

Features included:

* Home endpoint
* Path parameter endpoint
* Query parameter endpoint

---

## Running the Project

Start the server using:

```bash
uvicorn main:app --reload
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

## Key Learnings

* How APIs work
* How FastAPI routes requests
* Difference between Path Parameters and Query Parameters
* Returning JSON responses
* Testing APIs using Swagger UI
* Importance of Python type hints in FastAPI

---

## Technologies Used

* Python
* FastAPI
* Uvicorn

---

## Status

Completed FastAPI fundamentals, endpoint creation, path parameters, query parameters, and API testing using Swagger UI.

