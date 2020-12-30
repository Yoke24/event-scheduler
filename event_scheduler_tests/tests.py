import sys
import unittest

unit_tests = unittest.TestLoader().discover('event_scheduler_tests/unit_tests',
                                            '*tests.py',
                                            '.')

result = unittest.TextTestRunner().run(unit_tests)
sys.exit(not result.wasSuccessful())
