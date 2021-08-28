#!/usr/bin/env bash

python3 main.py &> /dev/null

if [[ "$?" == "0" ]]; then
  git add .
  git commit -m "Update README" &> /dev/null
  git push origin main &> /dev/null

  exit 0
fi

exit 1