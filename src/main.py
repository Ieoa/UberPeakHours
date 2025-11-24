import argparse
from pathlib import Path
from bq_client import get_client, run_query
import pandas as pd
from viz import plot_line

QUERIES_DIR = Path(__file__).parent / "queries"


def load_query(name: str) -> str:
    p = QUERIES_DIR / name
    return p.read_text()


def run_and_save(client, query_path: str, params: dict, out_csv: Path, out_plot: Path, plot_args: dict):
    sql = load_query(query_path)
    # Substituir parâmetros via BigQuery Parameterized? Aqui vamos usar replace simples para simplicidade
    sql = sql.replace(
        "@start", f"'{params['start']}'").replace("@end", f"'{params['end']}'")
    df = run_query(client, sql)
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_csv, index=False)

    # configurar plot
    x = df.iloc[:, 0]
    y = df.iloc[:, 1]
    plot_line(x, y, **plot_args, out_path=str(out_plot))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--start', type=str, default='2019-01-01')
    parser.add_argument('--end', type=str, default='2019-12-31')
    parser.add_argument('--out', type=str, default='plots')
    parser.add_argument('--project', type=str, default=None)
    args = parser.parse_args()

    client = get_client(args.project)
    params = {'start': args.start, 'end': args.end}

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    # by_hour
    run_and_save(
        client,
        'by_hour.sql',
        params,
        out_csv=out_dir / 'rides_by_hour.csv',
        out_plot=out_dir / 'rides_by_hour.png',
        plot_args={'xlabel': 'Hour of Day', 'ylabel': 'Total Rides',
                   'title': 'Rides by Hour', 'xticks': list(range(0, 24))}
    )

    # by_weekday
    run_and_save(
        client,
        'by_weekday.sql',
        params,
        out_csv=out_dir / 'rides_by_weekday.csv',
        out_plot=out_dir / 'rides_by_weekday.png',
        plot_args={'xlabel': 'Weekday (1=Sun)', 'ylabel': 'Total Rides',
                   'title': 'Rides by Weekday', 'xticks': list(range(1, 8))}
    )

    # by_month
    run_and_save(
        client,
        'by_month.sql',
        params,
        out_csv=out_dir / 'rides_by_month.csv',
        out_plot=out_dir / 'rides_by_month.png',
        plot_args={'xlabel': 'Month', 'ylabel': 'Total Rides',
                   'title': 'Rides by Month', 'xticks': list(range(1, 13))}
    )

    print(f"Plots e CSVs gerados em: {out_dir.resolve()}")
