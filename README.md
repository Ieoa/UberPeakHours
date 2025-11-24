# Mapear Horários de Pico do Uber (NYC Taxi)

Projeto que consulta o dataset público de corridas de táxi (NYC) no BigQuery e gera análises e gráficos dos horários de pico.

## O que tem aqui
- Queries SQL para agrupar corridas por hora, dia da semana e mês.
- `main.py` em Python que executa as queries, baixa resultados e gera gráficos.
- Estrutura pronta para subir no GitHub com instruções.

## Pré-requisitos
1. Conta Google Cloud com BigQuery habilitado.
2. Projeto no GCP (não obrigatório para acessar datasets públicos, mas necessário para cotas e execução local).
3. `gcloud` instalado (opcional) e variáveis de ambiente de credenciais configuradas.

## Instalação
```bash
python -m venv .venv
source .venv/bin/activate  # mac/linux
.venv\Scripts\activate     # windows
pip install -r requirements.txt
