import time
import random
import uuid
import threading

drivers = [
    {"id": str(uuid.uuid4()), "name": "Carlos", "location": (37.7749, -122.4194), "available": True},
    {"id": str(uuid.uuid4()), "name": "Ana", "location": (37.7750, -122.4195), "available": True},
    {"id": str(uuid.uuid4()), "name": "João", "location": (37.7751, -122.4196), "available": True},
]

def release_driver(driver, delay=5):
    """Simula o tempo de uma corrida e libera o motorista novamente após um tempo"""
    time.sleep(delay)
    driver["available"] = True

def find_driver(pickup_location, driver_list):
    """Simula o pareamento de um motorista disponível"""
    available_drivers = [driver for driver in driver_list if driver["available"]]

    if not available_drivers:
        return None, None

    simulated_time = random.uniform(0.5, 2.5)
    time.sleep(simulated_time)

    driver = random.choice(available_drivers)
    driver["available"] = False

    threading.Thread(target=release_driver, args=(driver,)).start()

    return driver, simulated_time

def performance_test(runs=1000, max_time=3.0):
    """Executa múltiplas chamadas para find_driver e mede o tempo de resposta"""
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

performance_test()
