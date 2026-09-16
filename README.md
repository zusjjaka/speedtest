# Internet Speed Test

Простой CLI-скрипт для измерения скорости загрузки данных по HTTP.

Скрипт выполняет 10 последовательных запросов к указанному URL, дожидается полного скачивания файла и выводит:

- время каждого запроса;
- объём скачанных данных;
- среднее время запроса;
- общий объём скачанных данных;
- среднюю скорость загрузки в MB/s.

## Использование

Клонировать репозиторий:

```bash
git clone https://github.com/zusjjaka/speedtest
cd speedtest
```

Активировать виртуальное окружение:

```bash
py -m venv .venv
```

Скачать зависимости:

```bash
pip install -r tools\requirements\req.txt
```

Запустить скрипт по нужной ссылке:

```bash
py speedtest <url>
```

Рекоммендуется использовать следующие url:

- https://cdn.truefilesize.com/test/test-1mb.bin
- https://cdn.truefilesize.com/test/test-10mb.bin
- https://cdn.truefilesize.com/test/test-50mb.bin
