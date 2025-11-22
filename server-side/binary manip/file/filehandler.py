import os

def extract_filename(filename: str) -> str:
    return os.path.splitext(filename)[0]

def add_excention(filename: str, extention: str) -> str:
    return extract_filename(filename) + extention
