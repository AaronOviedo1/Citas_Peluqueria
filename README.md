# Citas_Peluqueria
Tarea de Patrones

# Sistema de Reservación de Citas para Barbería

Este proyecto es un sistema básico de reservación de citas para una barbería, desarrollado como parte de una práctica de patrones de diseño.

Se implementaron **cuatro patrones de diseño**: Factory Method, Observer, Facade y Singleton.

---

## 📌 Patrones de Diseño Usados

### 🏗️ 1. Factory Method (Creacional)

- **Problema de diseño:** Era necesario crear diferentes tipos de citas (corte, afeitado, paquete premium) sin depender directamente de clases concretas.
- **Razón de elección:** El patrón Factory Method permite encapsular la creación de objetos y facilitar su extensión.
- **Solución aplicada:** Se creó la clase `CitaFactory` que instancia el tipo de cita correcto dependiendo del string recibido.

CitaFactory.crear_cita("corte")

### 2. Observer

- **Problema de diseño:** Era necesario que los clientes recibieran una notificación automática al agendar, modificar o cancelar una cita.
- **Razón de elección:**  El patrón Observer permite que varios objetos (clientes) estén pendientes de los cambios en otro objeto (agenda de citas) y reaccionen en tiempo real.
- **Solución aplicada:** La clase `AgendaCitas` notifica a todos los clientes registrados mediante el método notificar(), y cada Cliente implementa el método actualizar() para recibir el mensaje.

Notificación para Pedro: Tu cita fue agendada: Cita para afeitado

### 3. Facade

- **Problema de diseño:** El flujo de reservar una cita involucraba múltiples pasos como validación, creación del objeto, registro de cliente y notificación, lo cual complicaba el uso externo del sistema.
- **Razón de elección:** El patrón Facade encapsula subsistemas complejos y proporciona una interfaz simple y clara para el usuario final.
- **Solución aplicada:**  Se creó la clase `CitaFacade` que centraliza todo el proceso de reservación en un solo método, ocultando la complejidad interna del sistema.

facade.reservar_cita(cliente, "afeitado")

### 4. Singleton

- **Problema de diseño:**  Debía existir una sola instancia compartida de la agenda de citas para mantener coherencia en el sistema.
- **Razón de elección:** El patrón Singleton garantiza que una clase solo tenga una instancia y proporcione un punto de acceso global a ella.
- **Solución aplicada:** La clase `AgendaCitas` se implementó como Singleton, asegurando que cada acceso devuelva la misma instancia.

a1 is a2  # True

-------------------------------------------------------------

# 🧪 Tecnologías utilizadas

## Python 3
## Programación orientada a objetos
## Patrones de diseño 

--------------------------------------------------------------

👨‍💻 Autor
Aaron Oviedo
Estudiante de Ingeniería en Tecnologías Computacionales
6° semestre – ITESM
Matrícula: a01253074
