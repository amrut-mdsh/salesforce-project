"""Compare every supplied query with its reference CSV, including numeric tolerance."""
import csv
import math
from run_analysis import ROOT, load_database, results

def matches(actual, expected):
    if actual is None:
        return expected == ''
    try:
        return math.isclose(float(actual), float(expected), rel_tol=1e-9, abs_tol=1e-6)
    except (ValueError, TypeError):
        return str(actual) == expected

def main():
    with load_database() as connection:
        for name, headers, rows in results(connection):
            with (ROOT / 'Analysis' / f'{name}.csv').open(newline='') as stream:
                expected = list(csv.reader(stream))
            assert headers == expected[0], f'{name}: header mismatch'
            assert len(rows) == len(expected) - 1, f'{name}: row count mismatch'
            for number, (actual, wanted) in enumerate(zip(rows, expected[1:]), 1):
                assert len(actual) == len(wanted), f'{name}: column count mismatch'
                assert all(matches(a, e) for a, e in zip(actual, wanted)), f'{name}: row {number} mismatch'
            print(f'PASS {name}: all {len(rows)} result rows match the supplied snapshot')
    print('PASS: snapshot reconciliation; not business sign-off or native dashboard validation.')

if __name__ == '__main__':
    main()
