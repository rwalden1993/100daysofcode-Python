#! /usr/bin/python

import webbrowser

import api

main_url = "https://talkpython.fm"

def main():
    keyword = input('Keyword of title search: ')
    results = api.search_keyword(keyword)

    print(f"There are {len(results)} episodes that match \"{keyword}\"")
    for number, e in enumerate(results, 1):
        print(f"{number}. {e.title}")

    if len(results) > 0:
        user_in = input("Select episode to view:")

        for number, e in enumerate(results, 1):
            if int(user_in) == number:
                my_url = e.url

        full_url = main_url + my_url
        webbrowser.open(full_url, new=2)


if __name__ == '__main__':
    main()