class Engine:
    def __init__(self, horsepower: int, oil_level: int = 100):
        self.horsepower = horsepower
        self.oil_level = oil_level
        self.is_running = False
        self.health = 100

    def start(self) -> None:
        self.is_running = True

    def stop(self) -> None:
        self.is_running = False

    def diagnose(self) -> dict:
        return {
            "horsepower": self.horsepower,
            "oil_level": self.oil_level,
            "is_running": self.is_running,
            "health": self.health,
        }


class FuelTank:
    def __init__(self, capacity: int, fuel_level: int):
        self.capacity = capacity
        self.fuel_level = fuel_level

    def consume(self, amount: int) -> None:
        self.fuel_level -= amount

    def refuel(self, amount: int) -> None:
        self.fuel_level = min(self.capacity, self.fuel_level + amount)

    def diagnose(self) -> dict:
        return {
            "capacity": self.capacity,
            "fuel_level": self.fuel_level,
        }


class BrakeSystem:
    def __init__(self, pad_wear: int = 0):
        self.pad_wear = pad_wear 

    def apply_brakes(self) -> None:
        print("Торможение выполнено.")

    def diagnose(self) -> dict:
        return {
            "pad_wear": self.pad_wear,
            "status": "ok" if self.pad_wear < 90 else "critical",
        }


class Car:
    def __init__(self,
                  brand: str,
                  model: str,
                  engine: Engine,
                  fuel_tank: FuelTank,
                  brakes: BrakeSystem
                ):
        self.brand = brand
        self.model = model
        self._engine = engine
        self._fuel_tank = fuel_tank
        self._brakes = brakes
        self.speed = 0

    # ----------------------------
    # Уровень абстракции для водителя
    # ----------------------------
    def start(self) -> None:
        self._engine.start()
        print(f"{self.brand} {self.model} заведен.")

    def drive(self, distance: int) -> None:
        fuel_needed = distance // 10 + 1
        self._fuel_tank.consume(fuel_needed)
        self.speed = 60
        print(f"Автомобиль проехал {distance} км.")

    def stop(self) -> None:
        self._brakes.apply_brakes()
        self.speed = 0
        self._engine.stop()
        print("Автомобиль остановлен.")

    def show_dashboard(self) -> str:
        return (
            f"Панель водителя: скорость={self.speed} км/ч, "
            f"топливо={self._fuel_tank.fuel_level} л"
        )

    # ----------------------------
    # Более низкий уровень абстракции для механика
    # ----------------------------
    def full_diagnostics(self) -> dict:
        return {
            "engine": self._engine.diagnose(),
            "fuel_tank": self._fuel_tank.diagnose(),
            "brakes": self._brakes.diagnose(),
        }

    def change_oil(self) -> None:
        self._engine.oil_level = 100
        print("Масло заменено.")

    def replace_brake_pads(self) -> None:
        self._brakes.pad_wear = 0
        print("Тормозные колодки заменены.")