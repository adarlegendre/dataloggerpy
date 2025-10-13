#!/bin/bash
# Test email with TODAY's data

cd /home/admin/dataloggerpy
source loggervenv/bin/activate

echo "========================================"
echo "  Testing Email with TODAY's Data"
echo "========================================"
echo ""

# Get today's date in YYYY-MM-DD format
TODAY=$(date +%Y-%m-%d)

echo "Testing with date: $TODAY"
echo ""

# Run the test command with today's date
python manage.py test_summary_email --date "$TODAY"

echo ""
echo "========================================"
echo ""
echo "If you want to preview JSON without sending:"
echo "  python manage.py test_summary_email --date $TODAY --preview"
echo ""
echo "If you want to test with yesterday's data:"
echo "  python manage.py test_summary_email"
echo ""

deactivate

