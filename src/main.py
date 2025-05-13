from abc import ABC, abstractmethod

# Clase base
class Cita(ABC):
    @abstractmethod
    def descripcion(self):
        pass

# Tipos de citas concretas
class CorteCabello(Cita):
    def descripcion(self):
        return "Cita para corte de cabello"

class Afeitado(Cita):
    def descripcion(self):
        return "Cita para afeitado"

class PaquetePremium(Cita):
    def descripcion(self):
        return "Cita para paquete premium (corte + afeitado + facial)"
    

class CitaFactory:
    @staticmethod
    def crear_cita(tipo):
        if tipo == "corte":
            return CorteCabello()
        elif tipo == "afeitado":
            return Afeitado()
        elif tipo == "premium":
            return PaquetePremium()
        else:
            raise ValueError("Tipo de cita no válido")
        
# Interfaces del patrón Observer
class Observador(ABC):
    @abstractmethod
    def actualizar(self, mensaje: str):
        pass

class Sujeto(ABC):
    @abstractmethod
    def agregar_observador(self, observador: Observador):
        pass

    @abstractmethod
    def eliminar_observador(self, observador: Observador):
        pass

    @abstractmethod
    def notificar(self, mensaje: str):
        pass

class Cliente(Observador):
    def __init__(self, nombre: str):
        self.nombre = nombre

    def actualizar(self, mensaje: str):
        print(f"Notificación para {self.nombre}: {mensaje}")

class AgendaCitas(Sujeto):
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(AgendaCitas, cls).__new__(cls)
            cls._instancia._init_instancia()
        return cls._instancia

    def _init_instancia(self):
        self.observadores = []

    def agregar_observador(self, observador: Observador):
        if observador not in self.observadores:
            self.observadores.append(observador)

    def eliminar_observador(self, observador: Observador):
        self.observadores.remove(observador)

    def notificar(self, mensaje: str):
        for observador in self.observadores:
            observador.actualizar(mensaje)

    def crear_cita(self, cliente: Cliente, tipo: str):
        cita = CitaFactory.crear_cita(tipo)
        self.notificar(f"Tu cita fue agendada: {cita.descripcion()}")



class CitaFacade:
    def __init__(self):
        self.agenda = AgendaCitas()

    def registrar_cliente(self, cliente: Cliente):
        self.agenda.agregar_observador(cliente)

    def reservar_cita(self, cliente: Cliente, tipo: str):
        try:
            self.registrar_cliente(cliente)
            self.agenda.crear_cita(cliente, tipo)
        except ValueError as e:
            print(f"Error al reservar la cita: {e}")


if __name__ == "__main__":
    tipos = ["corte", "afeitado", "premium", "otro"]

    for tipo in tipos:
        try:
            cita = CitaFactory.crear_cita(tipo)
            print(f"{tipo.capitalize()}: {cita.descripcion()}")
        except ValueError as e:
            print(f"{tipo.capitalize()}: Error -> {e}")

    print("\n--- Probando Observer ---")
    agenda = AgendaCitas()

    cliente1 = Cliente("Aaron")
    cliente2 = Cliente("Luis")

    agenda.agregar_observador(cliente1)
    agenda.agregar_observador(cliente2)

    agenda.crear_cita(cliente1, "corte")

    print("\n--- Probando Facade ---")
    facade = CitaFacade()

    cliente3 = Cliente("Pedro")
    facade.reservar_cita(cliente3, "afeitado")
    facade.reservar_cita(cliente3, "invalid-type")  # caso con error

    print("\n--- Probando Singleton ---")
    a1 = AgendaCitas()
    a2 = AgendaCitas()

    print(f"Misma instancia: {a1 is a2}")  # debe imprimir True




