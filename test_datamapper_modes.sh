#!/bin/bash
# Test script for datamapper_detections_json.py - run each mode to verify
# Run from project root: ./test_datamapper_modes.sh

echo "=== 1. Preview (no POST) - show 1 pending record payload ==="
python datamapper_detections_json.py --preview

echo ""
echo "=== 2. Preview 3 records (no POST) ==="
python datamapper_detections_json.py --preview 3

echo ""
echo "=== 3. Test: process 1 record (POST to API) ==="
python datamapper_detections_json.py --once --test

echo ""
echo "=== 4. Limit: process 5 records ==="
python datamapper_detections_json.py --once --limit 5

echo ""
echo "=== 5. Force-new + Test: reset and process 1 record ==="
python datamapper_detections_json.py --once --test --force-new

echo ""
echo "=== All tests complete. Watch mode: python datamapper_detections_json.py ==="
