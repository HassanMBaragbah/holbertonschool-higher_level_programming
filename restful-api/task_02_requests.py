#!/usr/bin/python3
"""
Fetch and print/save posts from a REST API endpoint.
"""
import csv
import requests


def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get('title'))


def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()
        structured_posts = [
            {
                'id': post.get('id'),
                'title': post.get('title'),
                'body': post.get('body')
            }
            for post in posts
        ]
        filename = "posts.csv"
        with open(
            filename, mode='w', encoding='utf-8', newline=''
        ) as csv_file:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(
                csv_file, fieldnames=fieldnames
            )
            writer.writeheader()
            for post in structured_posts:
                writer.writerow(post)
