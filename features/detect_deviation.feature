Feature: Pareamento de Motoristas

  Scenario: Encontrar um motorista disponível
    Given existem motoristas disponíveis
    When um passageiro solicita uma corrida
    Then um motorista deve ser pareado com ele

  Scenario: Nenhum motorista disponível
    Given não há motoristas disponíveis
    When um passageiro solicita uma corrida
    Then o sistema deve informar que não há motoristas disponíveis

  Scenario: O tempo médio de resposta deve ser inferior a 3 segundos
    Given existem motoristas disponíveis
    When um passageiro solicita uma corrida 40 vezes
    Then 99% das requisições devem ser atendidas em menos de 3 segundos
