import unittest
from datetime import datetime

# Function to validate inputs
def validate_inputs(sym, chart, ts, start, end):
    # Validate Symbol: 1-7 alphabetic characters, capitalized
    if not re.match(r'^[A-Z]{1,7}$', sym):
        raise ValueError("Symbol must be 1 to 7 capitalized alphabetic characters")
    
    # Validate Chart Type: '1' or '2'
    if chart not in ['1', '2']:
        raise ValueError("Chart type must be '1' or '2'")
    
    # Validate Time Series: '1' to '4'
    if ts not in ['1', '2', '3', '4']:
        raise ValueError("Time series must be '1', '2', '3', or '4'")
    
    # Validate Start Date: MM-DD-YYYY format
    try:
        datetime.strptime(start, '%m-%d-%Y')  # Use MM-DD-YYYY format
    except ValueError:
        raise ValueError("Start date must be in the format MM-DD-YYYY")
    
    # Validate End Date: MM-DD-YYYY format
    try:
        datetime.strptime(end, '%m-%d-%Y')  # Use MM-DD-YYYY format
    except ValueError:
        raise ValueError("End date must be in the format MM-DD-YYYY")
    
    # Ensure start date is before end date
    if start > end:
        raise ValueError("Start date cannot be after end date")

# Unit Test Class
class TestInputValidation(unittest.TestCase):
    
    def test_sym_valid(self):
        self.assertIsNone(validate_inputs("GOOG", "1", "1", "01-01-2023", "12-31-2023"))
    
    def test_sym_invalid(self):
        with self.assertRaises(ValueError):
            validate_inputs("goog", "1", "1", "01-01-2023", "12-31-2023")
        with self.assertRaises(ValueError):
            validate_inputs("GO1234", "1", "1", "01-01-2023", "12-31-2023")
        with self.assertRaises(ValueError):
            validate_inputs("TOOLONGSYMBOL", "1", "1", "01-01-2023", "12-31-2023")

    def test_chart_valid(self):
        self.assertIsNone(validate_inputs("GOOG", "1", "1", "01-01-2023", "12-31-2023"))
        self.assertIsNone(validate_inputs("GOOG", "2", "1", "01-01-2023", "12-31-2023"))

    def test_chart_invalid(self):
        with self.assertRaises(ValueError):
            validate_inputs("GOOG", "3", "1", "01-01-2023", "12-31-2023")

    def test_ts_valid(self):
        self.assertIsNone(validate_inputs("GOOG", "1", "1", "01-01-2023", "12-31-2023"))
        self.assertIsNone(validate_inputs("GOOG", "1", "4", "01-01-2023", "12-31-2023"))

    def test_ts_invalid(self):
        with self.assertRaises(ValueError):
            validate_inputs("GOOG", "1", "5", "01-01-2023", "12-31-2023")

    def test_start_valid(self):
        self.assertIsNone(validate_inputs("GOOG", "1", "1", "01-01-2023", "12-31-2023"))

    def test_start_invalid(self):
        with self.assertRaises(ValueError):
            validate_inputs("GOOG", "1", "1", "31-12-2023", "12-31-2023")
        with self.assertRaises(ValueError):
            validate_inputs("GOOG", "1", "1", "2023-01-01", "12-31-2023")

    def test_end_valid(self):
        self.assertIsNone(validate_inputs("GOOG", "1", "1", "01-01-2023", "12-31-2023"))

    def test_end_invalid(self):
        with self.assertRaises(ValueError):
            validate_inputs("GOOG", "1", "1", "01-01-2023", "31-12-2023")
        with self.assertRaises(ValueError):
            validate_inputs("GOOG", "1", "1", "01-01-2023", "2023-12-31")

    def test_start_before_end(self):
        with self.assertRaises(ValueError):
            validate_inputs("GOOG", "1", "1", "12-31-2023", "01-01-2023")

if __name__ == "__main__":
    unittest.main()
