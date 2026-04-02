import re


def convert_to_markdown(text):
    lines = text.split("\n")  # Split text into lines
    md = []
