from abc import abstractmethod, ABC

from enum import Enum
class Status(Enum):
    AVAILABLE = "Available"
    RENTED = "Rented"
    MAINTENANCE = "Maintenance"
    CLEANING = "Cleaning"
    RETIRED = "Retired"

class Vehicle(ABC):
    def __init__(self, plate_id: str, model: str, driver_name: str|None, registration_year: int, status: Status):
        self.plate_id = plate_id
        self.model = model
        self.driver_name = driver_name
        self.registration_year = registration_year
        self.status = status

    @abstractmethod
    def vehicle_type(self) -> str:
        '''Deve essere implementato nelle sottoclassi per restituire il tipo di veicolo (es. "car", "van").'''
        pass

    @abstractmethod
    def base_cleaning_time(self) -> int:
        '''Deve essere implementato nelle sottoclassi e restituire il tempo necessario per
        la pulizia ordinaria del veicolo espresso in minuti (int).'''
        pass

    @abstractmethod
    def wear_level(self) -> int:
        '''Deve essere implementato nelle sottoclassi e restituire un indicatore
        (ad esempio un numero intero) che descriva il livello medio di usura per quel tipo di veicolo (da 1 a 5).'''
        pass

    def info(self) -> dict[str, int|str|Status|bool]: 
        '''Restituisce un dizionario con le informazioni principali del veicolo.'''
        return {
            "id": self.plate_id,
            "model": self.model,
            "driver_name": self.driver_name,
            "veichle_type": self.vehicle_type(),
            "registration_year": self.registration_year,
            "status": self.status.value,
            # più eventuali campi specifici delle sottoclassi
        }

    def estimated_prep_time(self, factor: float = 1.0) -> int:
        '''Calcola un tempo stimato per preparare il veicolo (pulizia + controlli) prima di un nuovo noleggio, sulla base di:'''
        return int(self.base_cleaning_time() * factor + self.wear_level()*15)
    
class Car(Vehicle):
    def __init__(self, plate_id: str, model: str, driver_name: str|None, registration_year: int, status: Status, doors: int, is_cabrio: bool):
        super().__init__(plate_id, model, driver_name, registration_year, status)
        self.doors = doors
        self.is_cabrio = is_cabrio

    def vehicle_type(self) -> str:
        return "car"

    def base_cleaning_time(self) -> int:
        return 30

    def wear_level(self) -> int:
        return 1

    def info(self) -> dict[str, int|str|Status|bool]: 
        '''Restituisce un dizionario con le informazioni principali del veicolo.'''
        pre: dict[str, int|str|Status|bool] = super().info()
        pre["doors"] = self.doors
        pre["is_cabrio"] = self.is_cabrio
        return pre

class Van(Vehicle):
    def __init__(self, plate_id: str, model: str, driver_name: str|None, registration_year: int, status: Status, max_load_kg: int, require_special_license: bool):
        super().__init__(plate_id, model, driver_name, registration_year, status)
        self.max_load_kg = max_load_kg
        self.require_special_license = require_special_license

    def vehicle_type(self) -> str:
        return "van"

    def base_cleaning_time(self) -> int:
        return 60

    def wear_level(self) -> int:
        return 5

    def info(self) -> dict[str, int|str|Status|bool]: 
        '''Restituisce un dizionario con le informazioni principali del veicolo.'''
        pre: dict[str, int|str|Status|bool] = super().info()
        pre["max_load_kg"] = self.max_load_kg
        pre["require_special_license"] = self.require_special_license
        return pre

class FleetManager:
    def __init__(self):
        self.vehicles: dict[str, Vehicle] = dict()

    def add(self, vehicle: Vehicle) -> bool:
        '''Aggiunge un veicolo al sistema. 
        Restituisce True se l’inserimento va a buon fine, False se il veicolo esiste già.'''
        if vehicle.plate_id in self.vehicles.keys():
            return False
        self.vehicles[vehicle.plate_id] = vehicle
        return True

    def get(self, plate_id: str) -> Vehicle:
        '''Restituisce l’oggetto Vehicle corrispondente all’ID specificato oppure None se non esiste.'''
        return None if plate_id not in self.vehicles.keys() else self.vehicles[plate_id]

    def update(self, plate_id: str, new_vehicle: Vehicle) -> None:
        '''Sostituisce completamente il veicolo con id plate_id con new_vehicle (per simulare un PUT).'''
        if plate_id in self.vehicles.keys():
            self.vehicles.pop(plate_id)
        self.add(new_vehicle)

    def patch_status(self, plate_id: str, new_status: Status) -> bool:
        '''Aggiorna solo lo stato (status) del veicolo specificato con id plate_id (per simulare un PATCH).'''
        if plate_id in self.vehicles.keys() and new_status.value in [s.value for s in Status]:
            self.vehicles[plate_id].status = new_status
            return True
        return False

    def delete(self, plate_id: str) -> bool:
        '''Rimuove il veicolo dal dizionario.
        Restituisce True se l’eliminazione è andata a buon fine, False se il veicolo non esiste.'''
        if plate_id not in self.vehicles.keys():
            return False
        self.vehicles.pop(plate_id)
        return True

    def list_all(self) -> list[dict[str, int|str|Status|bool]]:
        '''restituisce una lista di tutte le info() di veicoli presenti nel sistema.'''
        return [v.info() for v in self.vehicles.values()]

if __name__ == "__main__":
    fm = FleetManager()

    # Crea veicoli
    car1 = Car(plate_id="ABC123", model="Fiat 500", driver_name="Alice", registration_year=2019, status=Status.AVAILABLE, doors=3, is_cabrio=False)
    van1 = Van(plate_id="XYZ789", model="Mercedes Sprinter", driver_name=None, registration_year=2021, status=Status.RENTED, max_load_kg=3500, require_special_license=True)
    fm.add(car1)
    fm.add(van1)

    print("Visualizza informazioni veicoli:")
    for vehicle_info in fm.list_all():
        print(vehicle_info)

    print("\nModifica lo stato:")
    fm.patch_status("ABC123", Status.RETIRED)
    updated_car = fm.get("ABC123")
    print(f"Stato del veicolo {updated_car.plate_id}: {updated_car.status.name}")