import unittest
from synchSubtitles import Synchronize


class SynchronizeTest(unittest.TestCase):
    """Tests for synchSubtitles.py"""

    def setUp(self):
        """Set up a initial time and a delta time"""
        self.old_time = '00:00:28,000'
        self.delta = '00:00:10,000'
        
    def test_decrement(self):
        """Do object decrement the time"""
        synch = Synchronize(self.old_time)
        result = synch.decrement(self.delta)
        self.assertEqual(result, '00:00:18,000')
    
    def test_increment(self):
        """Do object increment the time"""
        synch = Synchronize(self.old_time)
        result = synch.increment(self.delta)
        self.assertEqual(result, '00:00:38,000')
        
unittest.main()
