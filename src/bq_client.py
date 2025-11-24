
from google.cloud import bigquery
from typing import Optional


def get_client(project: Optional[str] = None):
    """Retorna um cliente do BigQuery. Usa credenciais padrão do ambiente."""
    if project:
        return bigquery.Client(project=project)
    return bigquery.Client()


def run_query(client: bigquery.Client, query: str):
    job = client.query(query)
    return job.result().to_dataframe()
