from gestione import *
from flask import Flask, jsonify, request

fm = FleetManager()

car1 = Car(plate_id="ABC123", model="Fiat 500", driver_name="Alice", registration_year=2019, status=Status.AVAILABLE, doors=3, is_cabrio=False)
van1 = Van(plate_id="XYZ789", model="Mercedes Sprinter", driver_name=None, registration_year=2021, status=Status.RENTED, max_load_kg=3500, require_special_license=True)
fm.add(car1)
fm.add(van1)

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "description" : "Welcome to Rent Service API",
        "_links" : {
            "Todo" : "TODO"
        }
    })

@app.route("/vehicles")
def list_all():
    res: dict[str, dict[str, int|str|Status|bool]] = dict()
    for k, v in fm.vehicles.items():
        res[k] = v.info()
    
    return jsonify(res)

@app.route("/vehicles/<string:id>")
def get_vehicle(id: str):
    res: Vehicle|None = fm.get(id)
    return (jsonify(res.info()), 200) if res else (jsonify({"error": "Vehicle not found"}), 404)

@app.route("/vehicles/<string:id>/prep-time/<float:factor>")
def get_prep_time(id: str, factor : float):
    res: Vehicle|None = fm.get(id)
    if res:
        return (jsonify(
            {
                "id" : res.plate_id,
                "vehicle_type" : res.vehicle_type(),
                "factor" : factor,
                "estimated_total_minutes" : res.estimated_prep_time(factor)
             }
        ), 200)
    else:
        return (jsonify({"error": "Vehicle not found"}), 404)
    
@app.route("/vehicles", methods=["POST"])
def post_vehicle():
    data = request.get_json()

    if "plate_id" not in data:
        return jsonify({"error": "Missing field: plate_id"}), 400

    if "model" not in data:
        return jsonify({"error": "Missing field: model"}), 400

    if "vehicle_type" not in data:
        return jsonify({"error": "Missing field: vehicle_type"}), 400

    if "registration_year" not in data:
        return jsonify({"error": "Missing field: registration_year"}), 400

    if "status" not in data:
        return jsonify({"error": "Missing field: status"}), 400

    if data["status"].lower() not in [s.value.lower() for s in Status]:
        return jsonify({'error': 'Invalid status value'}), 400

    plate_id = data["plate_id"]
    model = data["model"]
    driver_name = data["driver_name"] if "driver_name" in data else None
    registration_year = data['registration_year']
    status = data["status"]
    status = Status[status.upper()]

    match data["vehicle_type"].lower():
        case "car":
            if "doors" not in data:
                return jsonify({"error" : "Missing field: doors"}), 400

            if "is_cabrio" not in data:
                return jsonify({"error": "Missing field: is_cabrio"}), 400

            veh: Car = Car(plate_id, model, driver_name, registration_year, status, data["doors"], data["is_cabrio"])
        case "van":
            if "max_load_kg" not in data:
                return jsonify({"error" : "Missing field: max_load_kg"}), 400

            if "require_special_license" not in data:
                return jsonify({"error": "Missing field: require_special_license"}), 400

            veh: Van = Van(plate_id, model, driver_name, registration_year, status, data["max_load_kg"], data["require_special_license"])
        case _:
            return jsonify({"error" : "Vehicle type not recognized."}), 400

    # Aggiungiamo il veicolo
    if not fm.add(veh):
        return jsonify({'error': f"Vehicle with plate ID {plate_id} already exists."}), 400
    return jsonify(veh.info()), 201

@app.route("/vehicles/<string:id>", methods=["PUT"])
def put_vehicle(id: str):
    data = request.get_json()

    if "plate_id" not in data:
        return jsonify({"error": "Missing field: plate_id"}), 400

    if "model" not in data:
        return jsonify({"error": "Missing field: model"}), 400

    if "vehicle_type" not in data:
        return jsonify({"error": "Missing field: vehicle_type"}), 400

    if "registration_year" not in data:
        return jsonify({"error": "Missing field: registration_year"}), 400

    if "status" not in data:
        return jsonify({"error": "Missing field: status"}), 400

    if data["status"].lower() not in [s.value.lower() for s in Status]:
        return jsonify({'error': 'Invalid status value'}), 400

    plate_id = data["plate_id"]
    model = data["model"]
    driver_name = data["driver_name"] if "driver_name" in data else None
    registration_year = data['registration_year']
    status = data["status"]
    status = Status[status.upper()]

    match data["vehicle_type"].lower():
        case "car":
            if "doors" not in data:
                return jsonify({"error" : "Missing field: doors"}), 400

            if "is_cabrio" not in data:
                return jsonify({"error": "Missing field: is_cabrio"}), 400

            veh: Car = Car(plate_id, model, driver_name, registration_year, status, data["doors"], data["is_cabrio"])
        case "van":
            if "max_load_kg" not in data:
                return jsonify({"error" : "Missing field: max_load_kg"}), 400

            if "require_special_license" not in data:
                return jsonify({"error": "Missing field: require_special_license"}), 400

            veh: Van = Van(plate_id, model, driver_name, registration_year, status, data["max_load_kg"], data["require_special_license"])
        case _:
            return jsonify({"error" : "Vehicle type not recognized."}), 400

    # Put il veicolo
    fm.update(id, veh)
    return jsonify(veh.info()), 201
