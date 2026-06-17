#  Day 2 - FastAPI CRUD API

##  Overview

Today I learned the fundamentals of building APIs using FastAPI and implemented a complete CRUD (Create, Read, Update, Delete) application for managing devices.

The project uses an in-memory Python list as temporary storage and demonstrates how APIs handle data through different HTTP methods.

---

##  Topics Covered

* Pydantic Models
* Request Bodies
* GET Requests
* POST Requests
* PUT Requests
* DELETE Requests
* HTTPException
* 404 Error Handling
* Swagger UI Testing

---

##  Project: Device Management API

A simple CRUD API that allows users to:

* Add a new device
* View all devices
* View a device by ID
* Update device details
* Delete a device

---

##  Device Model

```python
class Device(BaseModel):
    id: int
    name: str
    company: str
```

---

##  API Endpoints

### GET `/devices`

Returns all available devices.

### GET `/devices/{device_id}`

Returns a specific device using its ID.

### POST `/devices`

Creates a new device.

### PUT `/devices/{device_id}`

Updates an existing device.

### DELETE `/devices/{device_id}`

Removes a device from the list.

---

##  Testing

All endpoints were tested using FastAPI's built-in Swagger UI.

Swagger URL:

```text
http://127.0.0.1:8000/docs
```

---

##  Running the Project

Start the server using:

```bash
uvicorn main:app --reload
```

---

##  Key Learnings

* Understanding CRUD operations
* Working with Path Parameters
* Creating Request Bodies using Pydantic Models
* Handling API errors using HTTPException
* Testing APIs using Swagger UI
* Building RESTful endpoints with FastAPI

---

##  Technologies Used

* Python
* FastAPI
* Pydantic
* Uvicorn

---

##  Status

Completed Day 2 FastAPI CRUD Practice and successfully tested all endpoints in Swagger UI.
