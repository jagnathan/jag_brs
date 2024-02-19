import unittest
from unittest.mock import patch
from Analysis import Analysis

class TestAnalysis(unittest.TestCase):

  def setUp(self):
    self.analysis = Analysis("config.yaml")

  def test_load_data(self):
    # Test that data is loaded successfully
    self.analysis.load_data()
    self.assertIsNotNone(self.analysis.data)
