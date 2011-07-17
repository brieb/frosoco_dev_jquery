#!/usr/bin/python

import json

users = [
  {
    "name": "John Smith",
    "email": "john@stanford.edu",
    "house": "Schiff",
    "room": "219",
    "id": 5
  },
  {
    "name": "John Smith",
    "email": "john@stanford.edu",
    "house": "Schiff",
    "room": "219",
    "id": 6
  },
  {
    "name": "John Smith",
    "email": "john@stanford.edu",
    "house": "Schiff",
    "room": "219",
    "id": 7
  },
  {
    "name": "John Smith",
    "email": "john@stanford.edu",
    "house": "Schiff",
    "room": "219",
    "id": 8
  }
]

print "Content-Type: application/json\n"
print json.dumps(users)