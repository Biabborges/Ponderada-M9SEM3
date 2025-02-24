import time
import random
import uuid
import threading
from functools import wraps

class CircuitBreaker:
    def __init__(self, failure_threshold=5, recovery_time=10):
        self.failure_threshold = failure_threshold
        self.recovery_time = recovery_time
        self.failure_count = 0
        self.last_failure_time = None
        self.state = "CLOSED"

    def _can_attempt(self):
        if self.state == "OPEN":
            elapsed_time = time.time() - self.last_failure_time
            if elapsed_time >= self.recovery_time:
                self.state = "HALF-OPEN"
                return True
            return False
        return True

    def call(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not self._can_attempt():
                print("Circuit Breaker ABERTO! Tentando novamente mais tarde...")
                return None, None

            result, response_time = func(*args, **kwargs)
            
            if result is None:
                self.failure_count += 1
                if self.failure_count >= self.failure_threshold:
                    self.state = "OPEN"
                    self.last_failure_time = time.time()
                    print("Circuit Breaker ativado! Muitas falhas consecutivas.")
            else:
                self.failure_count = 0
                if self.state == "HALF-OPEN":
                    self.state = "CLOSED"
                    print("Circuit Breaker voltou ao estado FECHADO.")
            
            return result, response_time
        
        return wrapper

circuit_breaker = CircuitBreaker(failure_threshold=3, recovery_time=5)

drivers = [
    {"id": str(uuid.uuid4()), "name": "Carlos", "location": (37.7749, -122.4194), "available": True},
    {"id": str(uuid.uuid4()), "name": "Ana", "location": (37.7750, -122.4195), "available": True},
    {"id": str(uuid.uuid4()), "name": "João", "location": (37.7751, -122.4196), "available": True},
]

def release_driver(driver, delay=5):
    time.sleep(delay)
    driver["available"] = True

@circuit_breaker.call
def find_driver(pickup_location, driver_list, max_wait_time=5, release_delay=5):
    start_time = time.time()
    while time.time() - start_time < max_wait_time:
        available_drivers = [driver for driver in driver_list if driver["available"]]
        if available_drivers:
            simulated_time = random.uniform(0.5, 2.5)
            time.sleep(simulated_time)
            
            driver = random.choice(available_drivers)
            driver["available"] = False
            if release_delay > 0:
                threading.Thread(target=release_driver, args=(driver, release_delay)).start()
            else:
                driver["available"] = True
            return driver, simulated_time
        time.sleep(0.5)
    return None, None

def performance_test(runs=40, max_time=3.0):
    success_count = 0
    response_times = []
    failed_requests = 0

    for _ in range(runs):
        start_time = time.time()
        driver, response_time = find_driver((37.7750, -122.4195), drivers)
        end_time = time.time()

        if driver is None:
            failed_requests += 1
            continue

        elapsed_time = end_time - start_time
        response_times.append(elapsed_time)

        if elapsed_time <= max_time:
            success_count += 1

    total_requests = runs - failed_requests
    
    if total_requests > 0:
        success_rate = (success_count / total_requests) * 100
        avg_response_time = sum(response_times) / total_requests
    else:
        success_rate = 0
        avg_response_time = 0

    print(f"Taxa de sucesso (respostas < {max_time}s): {success_rate:.2f}%")
    print(f"Tempo médio de resposta: {avg_response_time:.3f}s")
    print(f"Solicitações falhas (sem motoristas disponíveis): {failed_requests}")
    
    if success_rate >= 99:
        print("O requisito não funcional foi ATENDIDO!")
    else:
        print("O requisito não funcional NÃO FOI ATENDIDO!")

if __name__ == "__main__":
    performance_test()
