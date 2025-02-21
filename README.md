## Empresa escolhida: Uber

Esta ponderada simula um sistema de pareamento de motoristas para passageiros da uber. Ele inclui um teste de performance para garantir que as corridas sejam atendidas dentro de um tempo limite.  

### Requisitos trabalhados

#### Requisito Funcional  
- O sistema deve encontrar um motorista disponível sempre que um passageiro solicitar uma corrida, desde que haja motoristas disponíveis.  
- Se não houver motoristas disponíveis, o sistema deve informar corretamente que não há carros no momento.  

#### Requisito Não Funcional  
- 99% das solicitações devem ser atendidas em menos de 3 segundos.  
- O tempo médio de resposta deve ser inferior a 3 segundos para garantir um serviço ágil.  

### Como Funciona  

1. Os motoristas disponíveis estão armazenados em uma lista.  
2. Quando um passageiro solicita uma corrida:  
   - O sistema verifica motoristas disponíveis.  
   - Se houver um disponível, ele é pareado e marcado como ocupado.  
   - Se não houver, a solicitação falha.  
3. Após uma corrida simulada de aproximadamente 5 segundos, o motorista fica disponível novamente.  
4. O teste de performance roda 1000 solicitações, verificando o tempo médio de resposta e a taxa de sucesso.  


### Exemplo de Saída  

```sh
Taxa de sucesso (respostas < 3.0s): 98.5%
Tempo médio de resposta: 2.1s
Solicitações falhas (sem motoristas disponíveis): 15
O requisito não funcional foi ATENDIDO!
```