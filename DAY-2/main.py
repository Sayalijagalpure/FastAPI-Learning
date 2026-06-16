# full- in memory for a device resource
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI()

class Device(BaseModel):
    id: int
    name: str
    company: str

devices= []          # in-memory list

@app.get("/devices")                                                            # get all devices
def get_devices():
    return devices

@app.get("/devices/{device_id}")                                                # get device by id
def get_device(device_id: int):
    for device in devices:
        if device["id"]== device_id:
            return device
        
    raise HTTPException(status_code= 404, detail= "Device not found")

@app.post("/devices")                                                           # post method
def add_device(device: Device):
    devices.append(device.dict())
    return{
        "message":"Device added", 
        "device":device
    }

@app.put("/devices/{device_id}")                                                # put method
def update_device(device_id: int, updated_device: Device):
    for index, device in enumerate (devices):
        if device["id"]== device_id:
            devices[index]= updated_device.dict()
            return{
                "message": "Device updated",
                "device": updated_device
            }
    raise HTTPException (status_code= 404, detail= "Device not found")

@app.delete("/devices/{device_id}")                                             # delete method
def delete_device(device_id: int):
    for device in devices:
        if device["id"]== device_id:
            devices.remove(device)
            return{
                "message": "Device deleted"
            }
    raise HTTPException (status_code= 404, details= "Device not found")