import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
from scipy.optimize import minimize

# Função para coletar os dados dos ativos
def get_data(tickers, start, end):
    data = yf.download(tickers, start=start, end=end)['Adj Close']
    returns = data.pct_change().dropna()
    return returns

# Função objetivo: minimizar o risco (volatilidade) dado um retorno mínimo
def objective_function(weights, returns):
    portfolio_return = np.sum(returns.mean() * weights) * 252
    portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * 252, weights)))
    return portfolio_volatility

# Função para verificar se a soma dos pesos é 1 (restrição de carteira)
def check_sum(weights):
    return np.sum(weights) - 1

# Função para maximizar o retorno com base no limite de risco
def optimize_portfolio(returns, target_return):
    num_assets = len(returns.columns)
    constraints = ({'type': 'eq', 'fun': check_sum},   # Os pesos devem somar 1
                   {'type': 'ineq', 'fun': lambda w: np.sum(w * returns.mean()) * 252 - target_return})  # Retorno mínimo
    bounds = tuple((0, 1) for asset in range(num_assets))  # Limitar os pesos entre 0 e 1
    initial_guess = num_assets * [1. / num_assets]  # Chute inicial igual para todos os ativos

    result = minimize(objective_function, initial_guess, args=(returns,), method='SLSQP', bounds=bounds, constraints=constraints)
    return result

# Função para plotar a fronteira eficiente
def plot_efficient_frontier(returns, num_portfolios=10000):
    num_assets = len(returns.columns)
    results = np.zeros((3, num_portfolios))
    weights_record = []

    for i in range(num_portfolios):
        weights = np.random.random(num_assets)
        weights /= np.sum(weights)
        weights_record.append(weights)

        portfolio_return = np.sum(returns.mean() * weights) * 252
        portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * 252, weights)))
        results[0, i] = portfolio_volatility
        results[1, i] = portfolio_return
        results[2, i] = portfolio_return / portfolio_volatility

    max_sharpe_idx = np.argmax(results[2])
    sdp, rp = results[0, max_sharpe_idx], results[1, max_sharpe_idx]
    max_sharpe_allocation = pd.DataFrame(weights_record[max_sharpe_idx], index=returns.columns, columns=['allocation'])
    max_sharpe_allocation.allocation = [round(i*100, 2) for i in max_sharpe_allocation.allocation]

    plt.figure(figsize=(10, 7))
    plt.scatter(results[0, :], results[1, :], c=results[2, :], cmap='viridis', marker='o')
    plt.colorbar(label='Sharpe Ratio')
    plt.scatter(sdp, rp, marker='*', color='r', s=200, label='Max Sharpe Ratio')
    plt.title('Fronteira Eficiente')
    plt.xlabel('Risco (Volatilidade)')
    plt.ylabel('Retorno Esperado')
    plt.legend(labelspacing=0.8)
    plt.show()

    return max_sharpe_allocation

# Função para visualizar a alocação dos ativos
def plot_allocation(weights, tickers):
    plt.figure(figsize=(8, 6))
    plt.pie(weights, labels=tickers, autopct='%1.1f%%', startangle=90)
    plt.title("Alocação da Carteira")
    plt.show()

# Função para calcular o desempenho da carteira ao longo do tempo
def plot_portfolio_performance(returns, weights):
    # Calcula o retorno acumulado da carteira ao longo do tempo
    portfolio_returns = np.dot(returns, weights)
    cumulative_returns = (1 + portfolio_returns).cumprod()

    # Plotar o desempenho ao longo do tempo
    plt.figure(figsize=(10, 6))
    plt.plot(cumulative_returns, label='Retorno Acumulado da Carteira', color='b')
    plt.title('Histórico de Desempenho da Carteira')
    plt.xlabel('Data')
    plt.ylabel('Retorno Acumulado')
    plt.legend()
    plt.show()    

# Main
if __name__ == '__main__':
    # Lista de ações
    tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'NFLX']
    
    # Período de 2023
    start_date = '2023-01-01'
    end_date = '2023-12-31'

    # Coleta os dados
    returns = get_data(tickers, start=start_date, end=end_date)

    # Definir o retorno alvo
    target_return = 0.2  # Por exemplo, 20% anual

    # Otimização da carteira
    optimized_result = optimize_portfolio(returns, target_return)
    optimal_weights = optimized_result.x

    # Exibir os pesos ótimos
    print("Pesos ótimos da carteira:")
    print(pd.DataFrame(optimal_weights, index=tickers, columns=['Pesos']))

    # Visualizações
    max_sharpe_allocation = plot_efficient_frontier(returns)
    plot_allocation(optimal_weights, tickers)
    
    # Adicionar o gráfico de desempenho da carteira
    plot_portfolio_performance(returns, optimal_weights)