from abc import ABC, abstractmethod
from enum import Enum

class Status(Enum):
    ONLINE = "online"
    OFFLINE = "offline"
    UPDATING = "updating"
    ERROR = "error"

class SmartDevice(ABC):
    def __init__(self, serial_number: str, brand : str, room : str, installation_year : int, status : Status):
        self.serial_number = serial_number
        self.brand = brand
        self.room = room
        self.installation_year = installation_year
        self.status = status

    @abstractmethod
    def device_type(self) -> str:
        '''Deve essere implementato nelle sottoclassi per restituire il tipo del dispositivo (es. "bulb", "camera").'''
        pass

    @abstractmethod
    def energy_consumption(self) -> float:
        '''Deve essere implementato nelle sottoclassi e restituisce il consumo medio di energia in Watt del dispositivo
        (può essere un intero o un float).'''
        pass

    @abstractmethod
    def connection_quality(self) -> int:
        '''Deve essere implementato nelle sottoclassi e restituire un indicatore (ad esempio un numero intero)
        che descriva la qualità della connessione richiesta dal dispositivo (intero da 1 a 10).'''
        pass

    def info(self) -> dict[str, int | str]: 
        '''Restituisce un dizionario con le informazioni principali del dispositivo.'''

        return {
            "serial_number": self.serial_number,
            "brand": self.brand,
            "room": self.room,
            "installation_year": self.installation_year,
            "status": self.status.value
            # più eventuali campi specifici delle sottoclassi
        }

    def diagnostici_time(self, factor: float = 1.0) -> float:
        '''Calcola un tempo stimato per eseguire una diagnostica completa.
        Restituisce, in secondi, il tempo stimato per eseguire una diagnostica completa (valore intero).'''
        return self.energy_consumption() * factor + self.connection_quality()*10
    
class SmartBulb(SmartDevice):
    '''La classe SmartBulb rappresenta una lampadina intelligente ed eredita da SmartDevice.'''
    def __init__(self, serial_number : str, brand : str, room : str, installation_year : int, status : Status, brightness_lumens: int, color_capability : bool):
        super().__init__(serial_number, brand, room, installation_year, status)
        self.brightness_lumens = brightness_lumens
        self.color_capability = color_capability

    def device_type(self) -> str:
        return "bulb"

    def energy_consumption(self) -> float:
        '''Restituisce il consumo medio di energia in Watt (float o int).
        Per questa tipologia di dispositivo il consumo è basso, tipicamente 9 o 15 Watt.'''
        return float(12)

    def connection_quality(self) -> int:
        '''Restituisce un indicatore (ad esempio un numero intero) che descriva la qualità della connessione 
        richiesta dal dispositivo (intero da 1 a 10), tipicamente un valore basso/medio (es. tra 2 e 4), poiché le lampadine richiedono poca banda.'''
        return 2

    def info(self) -> dict[str, float | str | bool]:
        res = super().info()
        res["brightness_lumens"] = self.brightness_lumens
        res["color_capability"] = self.color_capability
        return res
    
class SecurityCamera(SmartDevice):
    '''La classe SecurityCamera rappresenta una telecamera di sicurezza ed eredita da SmartDevice.'''
    def __init__(self, serial_number : str, brand : str, room : str, installation_year : int, status : Status, resolution: str, night_vision : bool):
        super().__init__(serial_number, brand, room, installation_year, status)
        self.resolution = resolution
        self.night_vision = night_vision

    def device_type(self) -> str:
        return "camera"

    def energy_consumption(self) -> float:
        '''Restituisce il consumo medio di energia in Watt (float o int).
        I modelli di dispositivi motorizzati hanno tipicamente un consumo più elevato, quindi verrà restituito un valore più alto (es. 50 Watt).'''
        return float(50)

    def connection_quality(self) -> int:
        '''Restituisce un indicatore (ad esempio un numero intero) che descriva la qualità della connessione
        richiesta dal dispositivo (intero da 1 a 10). Per questo tipo di dispositivo sarà un valore alto (es. tra 8 e 10),
        poiché lo streaming video richiede tipicamente molta banda.'''
        return 9

    def info(self) -> dict[str, float | str | bool]:
        res = super().info()
        res["resolution"] = self.resolution
        res["night_vision"] = self.night_vision
        return res

class IoTHub:
    '''La classe IoTHub rappresenta il sistema di gestione di dispositivi intelligenti, cioè il database principale del sistema.'''
    def __init__(self):
        self.devices: dict[str, SmartDevice] = dict()

    def add(self, device: SmartDevice) -> bool:
        '''Aggiunge un dispositivo al sistema. 
        Restituisce True se l’inserimento va a buon fine, False se il numero seriale è già presente nel sistema.'''
        if self.get(device.serial_number) is None:
            self.devices[device.serial_number] = device
            return True
        return False

    def get(self, serial_number: str) -> SmartDevice | None : 
        '''Restituisce l’oggetto SmartDevice corrispondente all’ID specificato oppure None se non esiste.'''
        if serial_number in self.devices:
            return self.devices[serial_number]

    def update(self, serial_number: str, new_device: SmartDevice) -> None:
        '''Sostituisce completamente il dispositivo con numero seriale serial_number con new_device (per simulare un PUT).'''
        self.delete(serial_number)
        self.add(new_device)

    def patch_status(self, serial_number: str, new_status: Status) -> bool:
        '''Aggiorna solo lo stato (status) del dispositivo con numero seriale serial_number (per simulare un PATCH).'''
        if self.get(serial_number) is not None:
            self.get(serial_number).status = new_status
            return True
        return False

    def delete(self, serial_number: str) -> bool:
        '''Rimuove il dispositivo con numero seriale serial_number dal dizionario.
        Restituisce True se l’eliminazione è andata a buon fine, False se il dispositivo non esiste.'''
        if self.get(serial_number) is not None:
            self.devices.pop(serial_number)
            return True
        return False

    def list_all(self) -> list[dict[str, float | int | str]]: 
        '''Restituisce una lista di tutte le info() dei dispositivi presenti nel sistema'''
        return [dev.info() for dev in self.devices.values()]

if __name__ == "__main__":
    iotHub = IoTHub()
    bulb = SmartBulb("BULB001", "Philips", "Living Room", 2022, Status.ONLINE, 800, True)
    iotHub.add(bulb)
    camera = SecurityCamera("CAM001", "Ring", "Entrance", 2021, Status.OFFLINE, "1080p", True)
    iotHub.add(camera)

    print("Lista dispositivi")
    for dev in iotHub.list_all():
        print("serial_number : " + dev["serial_number"])

    iotHub.patch_status("CAM001", Status.ONLINE)

    print()
    print(f"Diagnostici lampadina: {bulb.diagnostici_time()}sec")
    print(f"Diagnostici telecamera: {camera.diagnostici_time(factor=1.2)}sec")
