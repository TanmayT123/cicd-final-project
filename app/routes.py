"""Routes for the Counter application."""
from flask import jsonify, abort
from app import app, COUNTERS


@app.route("/")
def index():
    """Root endpoint."""
    return jsonify({"status": "OK", "message": "Counter App Running"})


@app.route("/counters/<name>", methods=["POST"])
def create_counter(name):
    """Create a counter."""
    if name in COUNTERS:
        abort(409, description=f"Counter '{name}' already exists.")
    COUNTERS[name] = 0
    return jsonify({name: COUNTERS[name]}), 201


@app.route("/counters/<name>", methods=["GET"])
def read_counter(name):
    """Read a counter."""
    if name not in COUNTERS:
        abort(404, description=f"Counter '{name}' not found.")
    return jsonify({name: COUNTERS[name]})


@app.route("/counters/<name>", methods=["PUT"])
def update_counter(name):
    """Increment a counter."""
    if name not in COUNTERS:
        abort(404, description=f"Counter '{name}' not found.")
    COUNTERS[name] += 1
    return jsonify({name: COUNTERS[name]})


@app.route("/counters/<name>", methods=["DELETE"])
def delete_counter(name):
    """Delete a counter."""
    if name not in COUNTERS:
        abort(404, description=f"Counter '{name}' not found.")
    del COUNTERS[name]
    return "", 204
