import time
import sys

import requests


REQUEST_COUNT = 10
MB = 1024 * 1024


def handle_request(url: str) -> tuple[float, int]:
    START_TIME = time.perf_counter()

    with requests.get(url, stream=True, timeout=30) as response:
        response.raise_for_status()

        downloaded_bytes: int = 0

        for chunk in response.iter_content(chunk_size=MB):
            if chunk:
                downloaded_bytes += len(chunk)

    END_TIME = time.perf_counter()

    return END_TIME - START_TIME, downloaded_bytes


def main() -> None:
    if len(sys.argv) != 2:
        print(f'Usage: py {sys.argv[0]} <url>')
        sys.exit(1)

    url: str = sys.argv[1]

    total_bytes: int = 0
    total_time: float = 0


    for idx in range(REQUEST_COUNT):
        elapsed, downloaded_bytes = handle_request(url)

        total_time += elapsed
        total_bytes += downloaded_bytes

        downloaded_mb = downloaded_bytes / MB

        print(
            f'Request {idx+1:2}: '
            f'{elapsed:.2f} s | '
            f'{downloaded_mb:.2f} MB'
        )

    average_time = total_time / REQUEST_COUNT
    total_mb = total_bytes / MB
    average_speed = total_mb / total_time

    print()
    print('=' * 16 + ' RESULT ' + '=' * 16)
    print(f'Average request time: {average_time:.2f} s')
    print(f'Downloaded:           {total_mb:.2f} MB')
    print(f'Average speed:        {average_speed:.2f} MB/s')
    print('=' * 40)


if __name__ == '__main__':
    main()
