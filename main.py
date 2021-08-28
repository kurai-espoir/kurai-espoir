#!/usr/bin/env python3

# Import dependencies
from colorama import Fore, init
from requests import get

# The request class
class Request:
  def __init__(self, url: str):
    self.url = url

# Initialize colorama
init()

# Utility functions
def debug(msg: str) -> None:
  return print(f"[{Fore.GREEN}Debug{Fore.RESET}]: {msg}")

def error(msg: str) -> None:
  return print(f"[{Fore.RED}Error{Fore.RESET}]: {msg}")

# Set the path for the request
targets = [
  Request("https://komarev.com/"),
  Request("https://img.shields.io/"),
  Request("https://github-readme-stats.vercel.app/")
]

# Loop over the `targets`
for target in targets:
  # Do a HTTP GET request
  debug(f"Current URL: {target.url}")
  req = get(target.url)
  
  # Check the status code
  debug(f"Status code: {req.status_code}")
  if req.status_code != 200:
    error(f"Status code: {req.status_code}")
    exit(1)

  print("\n", end="")