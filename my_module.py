"""Dummy module to show how rq works"""
import requests


def count_words_at_url(url):
    resp = requests.get(url)
    return len(resp.text.split())
