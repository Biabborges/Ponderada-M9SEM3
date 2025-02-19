import time
import random
import uuid

# Lista simulada de motoristas disponíveis
drivers = [
    {"id": str(uuid.uuid4()), "name": "Carlos", "location": (37.7749, -122.4194), "available": True},
    {"id": str(uuid.uuid4()), "name": "Ana", "location": (37.7750, -122.4195), "available": True},
    {"id": str(uuid.uuid4()), "name": "João", "location": (37.7751, -122.4196), "available": True},
]

def find_driver(pickup_location):
    """Simula o pareamento de um motorista disponível"""
    available_drivers = [driver for driver in drivers if driver["available"]]

    if not available_drivers:
        return None, None  # Retorna None caso não haja motoristas disponíveis

    # Simulação de tempo de busca (entre 0.5s e 2.5s)
    simulated_time = random.uniform(0.5, 2.5)
    time.sleep(simulated_time)  # Simula tempo de resposta

    # Escolhe o primeiro motorista disponível
    driver = available_drivers[0]
    driver["available"] = False  # Marca como ocupado

    return driver, simulated_time  # Retorna o tempo de resposta

def performance_test(runs=1000, max_time=3.0):
    """Executa múltiplas chamadas para find_driver e mede o tempo de resposta"""
    success_count = 0
    response_times = []
    failed_requests = 0  # Contador de falhas por falta de motoristas

    for _ in range(runs):
        start_time = time.time()
        driver, response_time = find_driver((37.7750, -122.4195))
        end_time = time.time()

        # Se não encontrou motorista, contabiliza erro e continua o loop
        if driver is None:
            failed_requests += 1
            continue

        elapsed_time = end_time - start_time
        response_times.append(elapsed_time)

        if elapsed_time <= max_time:
            success_count += 1

    total_requests = runs - failed_requests  # Considera apenas as bem-sucedidas

    if total_requests > 0:
        success_rate = (success_count / total_requests) * 100
        avg_response_time = sum(response_times) / total_requests
    else:
        success_rate = 0
        avg_response_time = 0

    print(f"Taxa de sucesso (respostas < {max_time}s): {success_rate:.2f}%")
    print(f"Tempo médio de resposta: {avg_response_time:.3f}s")
    print(f"Solicitações falhas (sem motoristas disponíveis): {failed_requests}")

    # Verifica se o sistema atende ao requisito (99% abaixo de 3s)
    if success_rate >= 99:
        print("O requisito não funcional foi ATENDIDO!")
    else:
        print("O requisito não funcional NÃO FOI ATENDIDO!")

# Executar o teste de performance
performance_test()
