from abc import ABC, abstractmethod
from custom_types import StatoRiparazione

class Device(ABC):
    '''La classe Device rappresenta un dispositivo elettronico generico preso in carico dal centro di assistenza.'''
    ids: list[int] = []

    def __init__(self, model : str, customer_name : str, purchase_year : int, status : StatoRiparazione):
        numeric_id : int = max(device_id for device_id in Device.ids) + 1 if Device.ids else 0
        self.id: str = f"d{numeric_id}"
        Device.ids.append(numeric_id)
        self.model = model
        self.customer_name = customer_name
        self.purchase_year = purchase_year
        self.status = status

    @abstractmethod
    def device_type(self) -> str:
        '''Implementato dalle sottoclassi per restituire il tipo di dispositivo'''
        pass

    @abstractmethod
    def base_diagnosis_time(self) -> int:
        '''Implementato nelle sottoclassi e deve restituire il tempo base di diagnosi in minuti (int)'''
        pass
    
    @abstractmethod
    def repair_complexity(self) -> int:
        '''Implementato nelle sottoclassi e restituire un indicatore (ad esempio un numero intero)
        che descrive la complessità media di riparazione di quel tipo di dispositivo.'''
        pass
    
    def info(self) -> dict[str, int|str|StatoRiparazione]: 
        '''Restituisce un dizionario con le informazioni principali del dispositivo'''

        return {
            "id": self.id,
            "device_type": self.device_type(),
            "model": self.model,
            "customer_name": self.customer_name,
            "purchase_year": self.purchase_year,
            "status": self.status.value,
            # più eventuali campi specifici delle sottoclassi
        }
    
    def estimated_total_time(self, factor: float = 1.0) -> int:
        '''Calcola un tempo stimato di lavorazione (diagnosi + riparazione).
        Restituisce un intero che rappresenta i minuti.'''
        return round(self.base_diagnosis_time() * factor + self.repair_complexity() * 30)
    


class Smartphone(Device):
    '''La classe Smartphone rappresenta uno smartphone e eredita da Device.'''
    def __init__(self, model : str, customer_name : str, purchase_year : int, status : StatoRiparazione, storage_gb: int, has_protective_case: bool = True):
        super().__init__(model, customer_name, purchase_year, status)
        self.has_protective_case = has_protective_case
        self.storage_gb = storage_gb

    def device_type(self) -> str:
        '''Restituisce il tipo di dispositivo'''
        return "smartphone"

    def base_diagnosis_time(self) -> int:
        '''Restituisce il tempo base di diagnosi in minuti'''
        return (2025 - self.purchase_year) + (self.has_protective_case * 2)

    def repair_complexity(self) -> int:
        '''Restituisce un intero che rappresenta la complessità'''
        return 2

    def info(self) -> dict[str, int|str|StatoRiparazione|bool]:
        '''Restituisce un dizionario con le informazioni principali del dispositivo'''
        phone_info: dict[str, int|str|StatoRiparazione|bool] = super().info()
        phone_info["has_protective_case"] = self.has_protective_case
        phone_info["storage_gb"] = self.storage_gb

        return phone_info

class Laptop(Device):
    '''La classe Laptop rappresenta un laptop e eredita da Device.'''
    def __init__(self, model : str, customer_name : str, purchase_year : int, status : StatoRiparazione, screen_size_inches : float, has_dedicated_gpu : bool = True):
        super().__init__(model, customer_name, purchase_year, status)
        self.has_dedicated_gpu = has_dedicated_gpu
        self.screen_size_inches = screen_size_inches

    def device_type(self) -> str:
        '''Restituisce il tipo di dispositivo'''
        return "laptop"

    def base_diagnosis_time(self) -> int:
        '''Restituisce il tempo base di diagnosi in minuti'''
        return (2025 - self.purchase_year) + (self.has_dedicated_gpu * 3)

    def repair_complexity(self) -> int:
        '''Restituisce un intero che rappresenta la complessità'''
        return 13

    def info(self) -> dict[str, int|str|StatoRiparazione|bool]:
        '''Restituisce un dizionario con le informazioni principali del dispositivo'''
        laptop_info: dict[str, int|str|StatoRiparazione|bool] = super().info()
        laptop_info["has_dedicated_gpu"] = self.has_dedicated_gpu
        laptop_info["screen_size_inches"] = self.screen_size_inches

        return laptop_info

class ServiceCenter:
    '''La classe ServiceCenter rappresenta il centro di assistenza, cioè il contenitore principale del sistema.'''
    devices : dict[str, Device]

    def __init__(self):
        self.devices : dict[str, Device] = dict()
    
    def add(self, device : Device) -> bool:
        '''Aggiunge un dispositivo al centro.
        Restituisce True se l’inserimento va a buon fine, False se l’id esiste già.'''
        if self.get(device.id) is None:
            self.devices[device.id] = device
            return True
        return False

    def get(self, device_id : str) -> Device|None:
        '''Restituisce l’oggetto Device corrispondente all’ID specificato oppure None se non esiste.'''
        if device_id in self.devices:
            return self.devices[device_id]
        return None
    
    def update(self, device_id : str, new_device : Device) -> bool:
        '''Sostituisce completamente il dispositivo con id device_id con new_device'''
        if self.get(device_id) is not None and self.get(new_device.id) is None:
            new_device.id = device_id
            self.devices[device_id] = new_device
            return True
        return False
    
    def patch_status(self, device_id : str, new_status : StatoRiparazione) -> bool:
        '''Aggiorna solo lo stato (status) del dispositivo specificato'''
        if self.get(device_id) is not None:
            self.devices[device_id].status = new_status
            return True
        return False
    
    def delete(self, device_id : str) -> bool:
        '''Rimuove il dispositivo dal dizionario.
        Restituisce True se l’eliminazione è andata a buon fine, False se il dispositivo non esiste.'''
        if self.get(device_id) is not None:
            self.devices.pop(device_id)
            Device.ids.remove(device_id)
            return True
        return False
    
    def list_all(self) -> list[dict[str, int|str|StatoRiparazione|bool]]:
        '''Restituisce una lista di tutti i dispositivi presenti nel centro'''
        return [device.info() for device in self.devices.values()]