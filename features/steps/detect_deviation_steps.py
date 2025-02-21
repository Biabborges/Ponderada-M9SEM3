from behave import given, when, then
import time
import random
import uuid
from src.services.AverageWaitingTime import find_driver

@given("existem motoristas disponíveis")
def step_given_drivers_available(context):
    """Preenche a lista de motoristas disponíveis"""
    context.drivers = [
        {"id": str(uuid.uuid4()), "name": "Carlos", "location": (37.7749, -122.4194), "available": True},
        {"id": str(uuid.uuid4()), "name": "Ana", "location": (37.7750, -122.4195), "available": True},
        {"id": str(uuid.uuid4()), "name": "João", "location": (37.7751, -122.4196), "available": True},
    ]

@given("não há motoristas disponíveis")
def step_given_no_drivers_available(context):
    """Lista vazia de motoristas disponíveis"""
    context.drivers = []

@when("um passageiro solicita uma corrida")
def step_when_passenger_requests_ride(context):
    """Chama a função de pareamento de motorista e mede o tempo"""
    start_time = time.time()
    context.driver, context.response_time = find_driver((37.7750, -122.4195), context.drivers)
    end_time = time.time()
    
    context.response_time = end_time - start_time

@then("um motorista deve ser pareado com ele")
def step_then_driver_is_paired(context):
    """Verifica se um motorista foi encontrado"""
    assert context.driver is not None, "Nenhum motorista foi pareado!"

@then("o sistema deve informar que não há motoristas disponíveis")
def step_then_no_drivers_available(context):
    """Verifica se a resposta foi None"""
    assert context.driver is None, "O sistema encontrou um motorista quando não deveria!"

@when("um passageiro solicita uma corrida 1000 vezes")
def step_when_performance_test(context):
    """Executa 1000 testes e mede os tempos de resposta"""
    context.success_count = 0
    context.response_times = []
    context.failed_requests = 0
    max_time = 3.0

    for _ in range(1000):
        start_time = time.time()
        driver, response_time = find_driver((37.7750, -122.4195), context.drivers)
        end_time = time.time()

        elapsed_time = end_time - start_time

        if driver is None:
            context.failed_requests += 1
            continue

        context.response_times.append(elapsed_time)

        if elapsed_time <= max_time:
            context.success_count += 1

@then("99% das requisições devem ser atendidas em menos de 3 segundos")
def step_then_performance_requirement(context):
    """Valida se o tempo médio de resposta atende o requisito"""
    total_requests = 1000 - context.failed_requests

    if total_requests > 0:
        success_rate = (context.success_count / total_requests) * 100
        avg_response_time = sum(context.response_times) / total_requests
    else:
        success_rate = 0
        avg_response_time = 0

    print(f"Taxa de sucesso (respostas < 3s): {success_rate:.2f}%")
    print(f"Tempo médio de resposta: {avg_response_time:.3f}s")

    assert success_rate >= 99, "O sistema não atingiu 99% das respostas em menos de 3s!"
