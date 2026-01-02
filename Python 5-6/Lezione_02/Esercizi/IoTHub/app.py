from classi import *
from flask import Flask, jsonify, url_for, request

iotHub = IoTHub()
bulb = SmartBulb("BULB001", "Philips", "Living Room", 2022, Status.ONLINE, 800, True)
iotHub.add(bulb)
camera = SecurityCamera("CAM001", "Ring", "Entrance", 2021, Status.OFFLINE, "1080p", True)
iotHub.add(camera)
bulb2 = SmartBulb("BULB002", "Bicchieri", "Living Room", 2019, Status.ERROR, 350, False)
iotHub.add(bulb2)

app: Flask = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "description" : "Smart Home Hub API",
        "links" : {
            "device list" : url_for("device_list"),
            "get single device" : url_for("get_single_device", serial_number="CAM001"),
            "diagnostic of a device" : url_for("get_diagnostic_device", serial_number="CAM001", factor="1.0"),
            "add new device to the system" : url_for("add_device"),
            "put a device" : url_for("set_device", serial_number="CAM001")
        }
    }), 200

@app.route("/devices")
def device_list():
    res = dict()
    for dev in iotHub.list_all():
        res[dev["serial_number"]] = dev

    return jsonify(
        res
    ), 200

@app.route("/devices/<string:serial_number>")
def get_single_device(serial_number : str):
    res = iotHub.get(serial_number)

    if res is not None:
        return jsonify(res.info()), 200

    return jsonify({"error" : "Not found"}), 404

@app.route("/devices/<string:serial_number>/diagnostic/<float:factor>")
def get_diagnostic_device(serial_number : str, factor : float):
    res = iotHub.get(serial_number)

    if res is not None:
        return jsonify({
            "id": res.serial_number,
            "device_type" : res.device_type(),
            "factor" : factor,
            "diagnostic_seconds" : res.diagnostici_time()
    }), 200
    
    return jsonify({"error" : "Not found"}), 404

def _validate_and_create_device(data : dict) -> tuple[dict, int]|SmartDevice:
    if "serial_number" not in data:
        return {"error" : "Missing field \"serial_number\"."}

    if "brand" not in data:
        return {"error" : "Missing field \"brand\"."}

    if "room" not in data:
        return {"error" : "Missing field \"room\"."}

    if "installation_year" not in data:
        return {"error" : "Missing field \"installation_year\"."}

    if "status" not in data:
        return {"error" : "Missing field \"status\"."}

    if data["status"].lower() not in [s.value.lower() for s in Status]:
        return {"error" : "Invalid value for field \"status\"."}

    if "type" not in data:
        return {"error" : "Missing field \"type\"."}

    match data["type"].lower():
        case "smartbulb":
            if "brightness_lumens" not in data:
                {"error" : "Missing field \"brightness_lumens\"."}

            if "color_capability" not in data:
                {"error" : "Missing field \"color_capability\"."}
        
            # Creation
            return SmartBulb(data["serial_number"], data["brand"], data["room"], data["installation_year"], Status[data["status"].upper()], data["brightness_lumens"], data["color_capability"])

        case "camera":
            if "resolution" not in data:
                {"error" : "Missing field \"resolution\"."}

            if "night_vision" not in data:
                {"error" : "Missing field \"night_vision\"."}

            # Creation
            return SecurityCamera(data["serial_number"], data["brand"], data["room"], data["installation_year"], Status[data["status"].upper()], data["resolution"], data["night_vision"])


        case _:
            return {"error" : "Invalid value for field \"type\"."}
        
@app.route("/devices", methods=["POST"])
def add_device():
    res = _validate_and_create_device(request.get_json())

    if isinstance(res, SmartDevice):
        if iotHub.add(res):
            return jsonify(res.info()), 201
        return jsonify({"error" : "Duplicate \"serial_number\"."}), 404
    return jsonify(res), 400

@app.route("/devices/<string:serial_number>", methods=["PUT"])
def set_device(serial_number : str):
    res = _validate_and_create_device(request.get_json())

    if isinstance(res, SmartDevice):
        iotHub.update(serial_number, res)
        return jsonify(res.info()), 201
    return jsonify(res), 400

@app.route("/devices/<string:serial_number>", methods=["PATCH"])
def change_status(serial_number : str):
    data = request.get_json()

    if "status" not in data:
        return {"error" : "Missing field \"status\"."}
    
    if data["status"].lower() not in [s.value.lower() for s in Status]:
        return {"error" : "Invalid value for field \"status\"."}

    if iotHub.patch_status(serial_number, Status[data["status"].upper()]):
        return jsonify(iotHub.get(serial_number).info()), 200
    return jsonify({"error" : "Not found"}), 404

@app.route("/devices/<string:serial_number>", methods=["DELETE"])
def delete_device(serial_number : str):
    if iotHub.delete(serial_number):
        return jsonify({
            "deleted" : True,
            "serial_number" : serial_number
        }), 204
    return jsonify({"error" : "Not found"}), 404