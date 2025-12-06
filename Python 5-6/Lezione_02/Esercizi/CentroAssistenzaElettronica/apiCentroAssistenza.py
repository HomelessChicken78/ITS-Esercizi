from main import *
from custom_types import StatoRiparazione
from flask import Flask, jsonify, url_for, request

app = Flask(__name__)
sc = ServiceCenter()
p = Smartphone("iPhone 14", "Giacomo Coccodrillini", 2022, StatoRiparazione.received, storage_gb=128, has_protective_case=True)
l = Laptop("Hp", "Drago Anonimo", 2020, StatoRiparazione.diagnosing, screen_size_inches=15.6, has_dedicated_gpu=True)
sc.add(p)
sc.add(l)

@app.route("/")
def home():
    return jsonify(
        {
            "description" : "Welcome to Service Center API",
            "endpoints": {
                url_for("get_all_devices") :
                {
                    "methods": ["GET", "PUT"],
                    "description": "Returns a json containing all devices or add a new device."
                },

                url_for("get_single_device", device_id="d1") :
                {
                    "methods": ["GET", "POST", "PATCH", "PUT", "DELETE"],
                    "description": "Returns a single device, allow to create a new one or modify/remove an existing one."
                },

                url_for("get_estimate", device_id = "d0", factor = 1.5) :
                {
                    "methods": ["GET"],
                    "description": "Returns the estimate time to repair a device."
                },
            },
        }
    ), 200

@app.route("/devices", methods=["GET"])
def get_all_devices():
    list_infos: dict[str, dict[str, int|str|StatoRiparazione|bool]] = dict()

    for d_id, device in sc.devices.items():
        list_infos[d_id] = device.info()
    
    return jsonify(list_infos), 200

@app.route("/devices/<string:device_id>", methods=['GET'])
def get_single_device(device_id : str):
    found_device : Device|None = sc.get(device_id)

    if found_device is not None:
        return jsonify(found_device.info()), 200
    return jsonify({"error": "Device not found"}), 404

@app.route("/devices/<string:device_id>/estimate", methods=['GET'])
def get_estimate_default(device_id : str):
    found_device : Device|None = sc.get(device_id)

    if found_device is not None:
        return jsonify(
                {
                    "id" : found_device.id,
                    "device_type": found_device.device_type(),
                    "factor": 1.0,
                    "estimated_total_minutes" : found_device.estimated_total_time()
                }
            ), 200
    return jsonify({"error": "Device not found"}), 404
@app.route("/devices/<string:device_id>/estimate/<float:factor>", methods=['GET'])
def get_estimate(device_id : str, factor : float):
    found_device : Device|None = sc.get(device_id)

    if found_device is not None:
        return jsonify(
                {
                    "id" : found_device.id,
                    "device_type": found_device.device_type(),
                    "factor": factor,
                    "estimated_total_minutes" : found_device.estimated_total_time(factor)
                }
            ), 200
    return jsonify({"error": "Device not found"}), 404
@app.route("/devices/<string:device_id>/estimate/<int:factor>", methods=['GET'])
def get_estimate_int(device_id : str, factor : int):
    found_device : Device|None = sc.get(device_id)

    if found_device is not None:
        return jsonify(
                {
                    "id" : found_device.id,
                    "device_type": found_device.device_type(),
                    "factor": float(factor),
                    "estimated_total_minutes" : found_device.estimated_total_time(float(factor))
                }
            ), 200
    return jsonify({"error": "Device not found"}), 404

@app.route("/devices", methods=["POST"])
def post_device():
    data = request.get_json()
    new_device: Device

    # Controlla tutti i parametri generici
    if "device_type" not in data:
        return jsonify({"error" : "missing 'device_type' field in the payload."}), 400
    
    if "model" not in data:
        return jsonify({"error" : "missing 'model' field in the payload."}), 400

    if "customer_name" not in data:
        return jsonify({"error" : "missing 'customer_name' field in the payload."}), 400
    
    if "purchase_year" not in data:
        return jsonify({"error" : "missing 'purchase_year' field in the payload."}), 400
    
    if "status" not in data:
        return jsonify({"error" : "missing 'status' field in the payload."}), 400
    
    status = data['status']

    # Controlla i parametri specifici
    if status not in [stato.value for stato in StatoRiparazione]:
        return jsonify({"error" : "invalid value for 'status' in the payload."}), 400
    
    match data["device_type"]:
        case "smartphone":
            if "storage_gb" not in data:
                return jsonify({"error" : "missing 'storage_gb' field in the payload."}), 400
            
            if len(data) > 7:
                return jsonify({"error" : "Too many fields in the payload."}), 400

            new_device = Smartphone(
                model=data["model"],
                customer_name=data["customer_name"],
                purchase_year=data["purchase_year"],
                status=StatoRiparazione(status),
                storage_gb=data["storage_gb"],
                has_protective_case=data["has_protective_case"] if "has_protective_case" in data else True
            )
        
        case "laptop":
            if "screen_size_inches" not in data:
                return jsonify({"error" : "missing 'screen_size_inches' field in the payload."}), 400
            
            if len(data) > 7:
                return jsonify({"error" : "Too many fields in the payload."}), 400
            
            new_device = Laptop(
                model=data["model"],
                customer_name=data["customer_name"],
                purchase_year=data["purchase_year"],
                status=StatoRiparazione(status),
                screen_size_inches=data["screen_size_inches"],
                has_dedicated_gpu=data["has_dedicated_gpu"] if "has_dedicated_gpu" in data else True
            )
        
        case _:
            return jsonify({"error" : "invalid value for 'device_type' field in the payload."}), 400
    
    sc.add(new_device)
    return jsonify(new_device.info()), 201

@app.route("/devices/<string:device_id>", methods=["DELETE"])
def delete_device(device_id: str):
    if sc.delete(device_id):
        return jsonify({"deleted": True, "id": device_id}), 204
    return jsonify({"error": "Device not found"}), 404

@app.route("/devices/<string:device_id>", methods=["PUT"])
def put_device(device_id : str):
    data = request.get_json()
        # Controlla tutti i parametri generici
    if "device_type" not in data:
        return jsonify({"error" : "missing 'device_type' field in the payload."}), 400
    
    if "model" not in data:
        return jsonify({"error" : "missing 'model' field in the payload."}), 400

    if "customer_name" not in data:
        return jsonify({"error" : "missing 'customer_name' field in the payload."}), 400
    
    if "purchase_year" not in data:
        return jsonify({"error" : "missing 'purchase_year' field in the payload."}), 400
    
    if "status" not in data:
        return jsonify({"error" : "missing 'status' field in the payload."}), 400
    
    status = data['status']

    # Controlla i parametri specifici
    if status not in [stato.value for stato in StatoRiparazione]:
        return jsonify({"error" : "invalid value for 'status' in the payload."}), 400
    
    match data["device_type"]:
        case "smartphone":
            if "storage_gb" not in data:
                return jsonify({"error" : "missing 'storage_gb' field in the payload."}), 400
            
            if len(data) > 7:
                return jsonify({"error" : "Too many fields in the payload."}), 400
            
            new_device = Smartphone(
                model=data["model"],
                customer_name=data["customer_name"],
                purchase_year=data["purchase_year"],
                status=StatoRiparazione(status),
                storage_gb=data["storage_gb"],
                has_protective_case=data["has_protective_case"] if "has_protective_case" in data else True
                )
        
        case "laptop":
            if "screen_size_inches" not in data:
                return jsonify({"error" : "missing 'screen_size_inches' field in the payload."}), 400
            
            if len(data) > 7:
                return jsonify({"error" : "Too many fields in the payload."}), 400
            
            new_device = Laptop(
                model=data["model"],
                customer_name=data["customer_name"],
                purchase_year=data["purchase_year"],
                status=StatoRiparazione(status),
                screen_size_inches=data["screen_size_inches"],
                has_dedicated_gpu=data["has_dedicated_gpu"] if "has_dedicated_gpu" in data else True
                )
        
        case _:
            return jsonify({"error" : "invalid value for 'device_type' field in the payload."}), 400

    if not sc.update(device_id, new_device):
        sc.add(new_device)

@app.route("/devices/<string:device_id>", methods=['PATCH'])
def patch_device_status(device_id: str):
    data = request.get_json()

    if sc.get(device_id) is None:
        return jsonify({"error": "Device not found"}), 404

    if "status" not in data:
        return jsonify({"error": "missing 'status' field in the payload."}), 400

    status = data['status']
    
    if status not in [stato.value for stato in StatoRiparazione]:
        return jsonify({"error" : "invalid value for 'status' in the payload."}), 400

    if sc.patch_status(device_id, StatoRiparazione(status)):
        return jsonify(sc.get(device_id).info()), 200