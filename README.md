# Otimização de Carteira de Investimentos com Problema da Mochila

## Descrição do Projeto

Este projeto tem como objetivo a construção de um algoritmo de otimização de carteira de investimentos, baseado no problema clássico da mochila. O objetivo é maximizar o retorno esperado de uma carteira de ativos financeiros, respeitando um limite de risco (volatilidade) aceitável. Utilizamos bibliotecas como `numpy`, `pandas`, `scipy.optimize` para otimizar a carteira e `matplotlib`, `seaborn` para visualização dos resultados.

### Objetivo
A implementação otimiza uma carteira de ativos financeiros, maximizando o retorno total dado um nível aceitável de risco (volatilidade). O algoritmo segue três etapas:
1. **Modelagem Matemática**: Adapta o problema da mochila com itens sendo ativos financeiros.
2. **Otimização**: Utiliza métodos de otimização numérica para encontrar a melhor alocação de ativos.
3. **Visualização**: Gráficos que mostram a fronteira eficiente, alocação de ativos e desempenho da carteira.

## Instalação

Siga os passos abaixo para configurar o projeto localmente:

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio

2. Instale os pacotes necessários:
   ```bash
   pip install -r requirements.txt

3. Execute o script principal:
   ```bash
   python main.py

### Requisistos
Python 3.x
Bibliotecas: numpy, pandas, matplotlib, seaborn, yfinance, scipy.


### Estrutura do Projeto
```bash
├── main.py                # Script principal contendo o código da otimização e visualização
├── README.md              # Arquivo de descrição do projeto
├── requirements.txt       # Lista de dependências
└── assets/                # Pasta contendo imagens dos gráficos gerados
```
### Uso
Este projeto utiliza dados reais do Yahoo Finance, obtidos via API usando a biblioteca yfinance. O exemplo abaixo coleta dados de seis ações de grandes empresas de tecnologia para o ano de 2023 e realiza a otimização da carteira.

## Exemplo de Execução
### 1. Coleta de Dados
O código coleta dados de retorno diário ajustado dos seguintes ativos financeiros:

Ativos: AAPL, MSFT, GOOGL, AMZN, TSLA, NFLX.
Período: 01/01/2023 a 31/12/2023.
```python
tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'NFLX']
start_date = '2023-01-01'
end_date = '2023-12-31'
returns = get_data(tickers, start=start_date, end=end_date)
```

### 2. Pesos Ótimos da Carteira
Após otimizar a carteira com base no retorno alvo de 20% ao ano, obtivemos os seguintes pesos ótimos para cada ativo:

| Ativo | Peso (%) |
|-------|----------|
| AAPL  | 15.32%   |
| MSFT  | 18.76%   |
| GOOGL | 20.00%   |
| AMZN  | 12.47%   |
| TSLA  | 23.45%   |
| NFLX  | 10.00%   |

Esses pesos são calculados de forma a maximizar o retorno esperado, respeitando o limite de risco definido.

### 3. Fronteira Eficiente
O gráfico da fronteira eficiente mostra a relação entre risco (volatilidade) e retorno esperado para diferentes combinações de ativos. O ponto vermelho indica a alocação com o maior índice de Sharpe (melhor relação retorno/risco).

![Fronteira Eficiente](https://github.com/user-attachments/assets/c2b00ac3-264e-4c0e-b30b-0c6313f2ec89)

### 4. Alocação de Ativos
A alocação dos ativos na carteira otimizada é visualizada no gráfico abaixo:

![Alocação de Ativos](https://github.com/user-attachments/assets/c34955ca-1f8f-455f-b15c-51355db7c453)


### 5. Desempenho Histórico da Carteira
A evolução do retorno acumulado da carteira ao longo de 2023 está representada no gráfico a seguir:

![Desempenho Histórico da Carteira](https://github.com/user-attachments/assets/0559f170-c527-4795-ac62-254688e2ea3e)


## Visualizações
Os gráficos gerados são:

1. Fronteira Eficiente: Mostra o equilíbrio entre retorno e risco das carteiras.
2. Alocação de Ativos: Exibe os pesos ótimos de cada ativo na carteira.
3. Desempenho Histórico: Mostra a evolução do retorno acumulado da carteira ao longo do tempo.

### Gráficos Interativos
Os gráficos podem ser interativos usando bibliotecas como plotly, mas a versão atual utiliza matplotlib e seaborn para facilitar a implementação e visualização.

## Conclusão

Este projeto demonstra como otimizar uma carteira de investimentos utilizando o problema da mochila adaptado para finanças. Através da otimização de retornos e visualização da fronteira eficiente, foi possível construir uma carteira que maximiza o retorno esperado, respeitando um limite de risco predefinido.
