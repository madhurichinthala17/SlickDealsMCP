from src.Helpers.utils import extract_posted_date
import pytest
from datetime import datetime, timedelta

class TestExtractPostedDate:

    def test_today_posted_date(self):
        raw_text = "htp182 | Staff posted Today 08:32 PM"
        expected_date = datetime.now()
        extracted_date = extract_posted_date(raw_text)
        assert extracted_date.date() == expected_date.date()

    def test_yesterday_posted_date(self):
        raw_text = "htp182 | Staff posted Yesterday 07:20 AM"
        expected_date = datetime.now() - timedelta(days=1)
        extracted_date = extract_posted_date(raw_text)
        assert extracted_date.date() == expected_date.date()

    def test_specific_date(self):
        raw_text = "htp182 | Staff posted Apr 11, 2026 09:49 PM"
        expected_date = datetime(2026, 4, 11, 21, 49)
        extracted_date = extract_posted_date(raw_text)
        assert extracted_date == expected_date

    def test_no_posted_date(self):
        raw_text = "htp182 | Staff posted"
        extracted_date = extract_posted_date(raw_text)
        assert extracted_date is None

    def test_empty_string(self):
        raw_text = ""
        extracted_date = extract_posted_date(raw_text)
        assert extracted_date is None   
    
    def test_none_input(self):
        raw_text = None
        extracted_date = extract_posted_date(raw_text)
        assert extracted_date is None

    def test_unrecognized_format(self):
        raw_text = "htp182 | Staff posted some time ago"
        extracted_date = extract_posted_date(raw_text)
        assert extracted_date is None
    
    def test_hours_ago(self):
        raw_text = "htp182 | Staff posted 3 hours ago"
        expected_date = datetime.now() - timedelta(hours=3)
        extracted_date = extract_posted_date(raw_text)
        assert abs((extracted_date - expected_date).total_seconds()) < 60  # Allow 1 minute difference

    def test_minutes_ago(self):
        raw_text = "htp182 | Staff posted 45 mins ago"
        expected_date = datetime.now() - timedelta(minutes=45)
        extracted_date = extract_posted_date(raw_text)
        assert abs((extracted_date - expected_date).total_seconds()) < 60  # Allow 1 minute difference

    def test_invalid_time_format(self):
        raw_text = "htp182 | Staff posted Today 25:61 PM"
        extracted_date = extract_posted_date(raw_text)
        assert extracted_date is None
    
    