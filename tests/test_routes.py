"""Unit tests for Counter App."""
import unittest
from app import app, COUNTERS


class TestCounterApp(unittest.TestCase):
    """Test cases for counter routes."""

    def setUp(self):
        """Set up test client."""
        self.client = app.test_client()
        COUNTERS.clear()

    def test_index(self):
        """Test root endpoint."""
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)

    def test_create_counter(self):
        """Test creating a counter."""
        resp = self.client.post("/counters/test")
        self.assertEqual(resp.status_code, 201)

    def test_read_counter(self):
        """Test reading a counter."""
        self.client.post("/counters/mycount")
        resp = self.client.get("/counters/mycount")
        self.assertEqual(resp.status_code, 200)

    def test_update_counter(self):
        """Test incrementing a counter."""
        self.client.post("/counters/hits")
        resp = self.client.put("/counters/hits")
        self.assertEqual(resp.status_code, 200)

    def test_delete_counter(self):
        """Test deleting a counter."""
        self.client.post("/counters/temp")
        resp = self.client.delete("/counters/temp")
        self.assertEqual(resp.status_code, 204)

    def test_read_missing_counter(self):
        """Test reading counter that does not exist."""
        resp = self.client.get("/counters/missing")
        self.assertEqual(resp.status_code, 404)

    def test_duplicate_counter(self):
        """Test creating duplicate counter returns 409."""
        self.client.post("/counters/dup")
        resp = self.client.post("/counters/dup")
        self.assertEqual(resp.status_code, 409)


if __name__ == "__main__":
    unittest.main()
