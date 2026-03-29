"""Flask Counter Application."""
from flask import Flask

app = Flask(__name__)
COUNTERS = {}

from app import routes  # noqa: E402, F401
