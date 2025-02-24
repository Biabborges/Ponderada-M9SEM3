## Empresa escolhida: Uber

Esta ponderada simula um sistema de pareamento de motoristas para passageiros da Uber. O sistema implementa dois requisitos principais:
- **Funcional:** Parear motoristas disponíveis quando um passageiro solicita uma corrida e informar corretamente quando não há motoristas disponíveis.
- **Não Funcional:** Garantir um desempenho ágil, com 99% das solicitações respondidas em menos de 3 segundos.

### Requisitos Trabalhados

#### Requisito Funcional  
- O sistema deve encontrar um motorista disponível sempre que um passageiro solicitar uma corrida, desde que haja motoristas disponíveis.
- Se não houver motoristas disponíveis, o sistema deve informar que não há carros no momento.

#### Requisito Não Funcional  
- 99% das solicitações devem ser atendidas em menos de 3 segundos.
- O tempo médio de resposta deve ser inferior a 3 segundos para assegurar um serviço ágil.

### Como Funciona

1. **Lista de Motoristas:**  
   Os motoristas disponíveis estão armazenados em uma lista.

2. **Solicitação de Corrida:**  
   Quando um passageiro solicita uma corrida:
   - O sistema verifica a disponibilidade dos motoristas.
   - Se houver um motorista disponível, ele é pareado e marcado como ocupado.
   - Se não houver motoristas disponíveis, a solicitação falha.

3. **Simulação da Corrida e Liberação do Motorista:**  
   - Em condições normais, após ser pareado, o motorista fica indisponível por 5 segundos (simulando o tempo de uma corrida) e, em seguida, é liberado.
   - No teste de desempenho, o parâmetro de liberação (`release_delay`) é definido como 0, fazendo com que o motorista seja liberado imediatamente para não interferir no tempo de resposta.

4. **Teste de Performance:**  
   O teste de desempenho executa 40 solicitações e mede:
   - O tempo de resposta de cada requisição.
   - A taxa de sucesso, que deve ser de pelo menos 99% das solicitações respondidas em menos de 3 segundos.

### Exemplo de Saída

```sh
Taxa de sucesso (respostas < 3.0s): 99.50%
Tempo médio de resposta: 2.1s
Solicitações falhas (sem motoristas disponíveis): 0
O requisito não funcional foi ATENDIDO!
```
