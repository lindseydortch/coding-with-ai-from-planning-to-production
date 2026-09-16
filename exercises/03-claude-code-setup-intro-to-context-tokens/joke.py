#!/usr/bin/env python3
"""Fetch Chuck Norris jokes from api.chucknorris.io, interactively."""

import json
import sys
import time
import urllib.error
import urllib.request

from config import RESET, BOLD, CYAN, YELLOW, GREEN, RED, CATEGORIES

API_BASE = "https://api.chucknorris.io"
HEADERS = {"User-Agent": "Mozilla/5.0"}


def _fetch(url):
    request = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(request) as response:
        return json.load(response)


def get_categories():
    return _fetch(f"{API_BASE}/jokes/categories")


def get_joke(category=None):
    url = f"{API_BASE}/jokes/random"
    if category:
        url += f"?category={category}"
    return _fetch(url)["value"]


def type_out(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def choose_category(categories):
    print(f"{YELLOW}Categories: {', '.join(categories)}{RESET}")
    while True:
        choice = input(f"{YELLOW}Pick a category (or press Enter for random): {RESET}").strip().lower()
        if not choice:
            return None
        if choice in categories:
            return choice
        print(f"{RED}Unknown category '{choice}', try again.{RESET}")


def prompt_yes_no(prompt):
    answer = input(prompt).strip().lower()
    return answer in ("y", "yes")


def main():
    try:
        categories = get_categories()
    except (urllib.error.URLError, urllib.error.HTTPError):
        print(f"{RED}Couldn't reach the joke API to load categories — using the built-in list.{RESET}")
        categories = CATEGORIES

    while True:
        category = choose_category(categories) if categories else None
        try:
            joke = get_joke(category)
        except (urllib.error.URLError, urllib.error.HTTPError) as exc:
            print(f"{RED}Couldn't fetch a joke right now ({exc}). Try again?{RESET}")
        else:
            print(f"{BOLD}{GREEN}Here's your joke:{RESET}")
            type_out(f"{CYAN}{joke}{RESET}")

        if not prompt_yes_no(f"{YELLOW}Hear another joke? (y/n): {RESET}"):
            print(f"{GREEN}Catch you later!{RESET}")
            break


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print(f"\n{GREEN}Catch you later!{RESET}")
