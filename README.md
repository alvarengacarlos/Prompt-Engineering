# Coleção de Prompt Engineering
## Objetivo
Criar prompts para automatizar/testar a geração de conteúdo.

## Prompt Engineering
### O que é?
É uma maneira eficientemente de instruir os LLMs, de tal forma que diminua o impacto de suas limitações (janela de contexto, memoria, ...), obtendo assim uma melhor resposta.

### Parâmetros de configuração
Os mais comuns são:

- **Temperature**: Define o nível de criatividade. Quanto maior, mais criativo.
- **Top P**: Define o quão deterministico o modelo será. Quanto menor, mais deterministico.
- **Max Length**: O número total do tokens que serão gerados na resposta.

### Elementos do Prompt
Cada prompt é composto por pelo menos um destes elementos, sendo eles:

- **Instruction**: O que o modelo deve fazer.
- **Context**: Informações externas que ajudam o modelo a melhorar as respostas.
- **Input Data**: Um texto ou pergunta que se deseja obter a resposta.
- **Output Indicator**: Como deve ser o formato da resposta.

## Referências
[Prompt Engineering Guide](https://www.promptingguide.ai/)
