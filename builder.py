from typing import Optional, Iterator, Callable

from functions import filter_query, unique_query, limit_query, map_query, sort_query, file_name_query, pattern_query

CMD_TO_FUNCTIONS: dict[str, Callable] = {
    'filter': filter_query,
    'unique': unique_query,
    'limit': limit_query,
    'map': map_query,
    'sort': sort_query,
    'file_name': file_name_query,
    'pattern': pattern_query
}


def read_file(file_name: str) -> Iterator[str]:
    with open(file_name) as file:
        for line in file:
            yield line


def build_query(cmd: str, value: str, file_name: str, data: Optional[list[str]]):
    if data is None:  # первый вызов - результат None, значит файл не читали
        prepared_data = read_file(file_name)
    else:
        prepared_data = data

    return list(CMD_TO_FUNCTIONS[cmd](value=value, data=prepared_data))
