import json
import os

REPORT = "/app/report.json"


def _load():
    assert os.path.exists(REPORT), f"{REPORT} does not exist"
    with open(REPORT) as f:
        return json.load(f)


def test_report_is_valid_json_object_with_expected_keys():
    # Success criterion 1: /app/report.json exists and is a single JSON
    # object with exactly the keys total_requests, unique_ips, top_path.
    data = _load()
    assert isinstance(data, dict)
    assert set(data.keys()) == {"total_requests", "unique_ips", "top_path"}


def test_total_requests():
    # Success criterion 2: total_requests equals the number of requests
    # in the log (6 non-empty lines).
    data = _load()
    assert data["total_requests"] == 6


def test_unique_ips():
    # Success criterion 3: unique_ips equals the number of distinct
    # client IP addresses in the log (192.168.0.1, 192.168.0.2, 10.0.0.5 -> 3).
    data = _load()
    assert data["unique_ips"] == 3


def test_top_path():
    # Success criterion 4: top_path equals the most frequently requested
    # path (/index.html, 3 hits).
    data = _load()
    assert data["top_path"] == "/index.html"
