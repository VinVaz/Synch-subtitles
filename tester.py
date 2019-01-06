import unittest
from lib.timeMethods import Synchronize


class SynchronizeTest(unittest.TestCase):
    """Tests for synchSubtitles.py"""

    def setUp(self):
        """Set up a initial time and a delta time"""
        self.old_time = '00:00:28,000'
        self.delta = '00:00:10,000'
        # initializes the class 
        self.synch = Synchronize(self.old_time)
        
    def test_decrement(self):
        """Do object decrement time"""
        result = self.synch.decrement(self.delta)
        self.assertEqual(result, '00:00:18,000')
    
    def test_increment(self):
        """Do object increment time"""
        result = self.synch.increment(self.delta)
        self.assertEqual(result, '00:00:38,000')
    
    def test_apply_delta_time(self):
        """Do object increment and decrement time"""
        result1 = self.synch.add('00:00:10,000')
        self.assertEqual(result1, '00:00:38,000')
        
        result2 = self.synch.add('-00:00:10,000')
        self.assertEqual(result2, '00:00:18,000')
        
unittest.main()
