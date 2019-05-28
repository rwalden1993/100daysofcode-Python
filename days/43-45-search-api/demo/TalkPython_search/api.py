#! /usr/bin/python
from typing import List

import requests
import collections

Result = collections.namedtuple('Result', 'category, id, url, title, description')

main_url = "https://search.talkpython.fm"


def search_keyword(keyword: str) -> List[Result]:
    url = main_url + "/api/search"

    payload = {'q': keyword}

    resp = requests.get(url, params=payload)

    resp.raise_for_status()

    results = resp.json()

    results_list = []
    for r in results.get('results'):
        my_result = Result(**r)

        if my_result.category == 'Episode':
            results_list.append(my_result)

    return results_list
