"""Run the supplied SQL against local CSVs; no services or external packages."""
from pathlib import Path
import argparse
import csv
import json
import math
import sqlite3

ROOT = Path(__file__).resolve().parents[1]

def load_database(root=ROOT):
    connection = sqlite3.connect(':memory:')
    config = json.loads((root / 'scripts/sources.json').read_text())
    for table, spec in config.items():
        fields = spec['fields']
        definitions = ['source_row INTEGER NOT NULL'] + [f'"{name}" {kind}' for _, name, kind in fields]
        connection.execute(f'CREATE TABLE "{table}" ({", ".join(definitions)})')
        with (root / spec['path']).open(encoding='utf-8-sig', newline='') as stream:
            reader = csv.DictReader(stream)
            missing = {src for src, _, _ in fields} - set(reader.fieldnames or [])
            if missing:
                raise ValueError(f'{spec["path"]}: missing columns {sorted(missing)}')
            for row_number, row in enumerate(reader, 1):
                values = [row_number]
                for src, _, kind in fields:
                    raw = row[src]
                    if raw is None or not raw.strip():
                        raise ValueError(f'{spec["path"]}: missing {src} at data row {row_number}')
                    value = raw if kind == 'TEXT' else float(raw)
                    if kind != 'TEXT' and not math.isfinite(value):
                        raise ValueError(f'{src}: non-finite value at data row {row_number}')
                    if kind == 'INTEGER':
                        if not value.is_integer():
                            raise ValueError(f'{src}: non-integer value at data row {row_number}')
                        value = int(value)
                    values.append(value)
                connection.execute(f'INSERT INTO "{table}" VALUES ({",".join("?" for _ in values)})', values)
    return connection

def results(connection, root=ROOT):
    for query in sorted((root / 'SQL').glob('Q[0-9][0-9].sql')):
        cursor = connection.execute(query.read_text())
        yield query.stem, [d[0] for d in cursor.description], cursor.fetchall()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT / 'artifacts')
    args = parser.parse_args()
    # Keep the supplied evidence snapshots immutable.
    if args.output.resolve() == (ROOT / 'Analysis').resolve():
        parser.error('Choose an output directory other than the supplied Analysis snapshots.')
    args.output.mkdir(parents=True, exist_ok=True)
    with load_database() as connection:
        for name, headers, rows in results(connection):
            with (args.output / f'{name}.csv').open('w', newline='') as stream:
                writer = csv.writer(stream)
                writer.writerow(headers)
                writer.writerows(rows)
            print(f'{name}: {len(rows)} rows')

if __name__ == '__main__':
    main()
