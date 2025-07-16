import unittest
import sys
import os

# Add the src directory to the path so we can import our module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from videoProcessing import videoProcessing

class TestVideoProcessing(unittest.TestCase):
    
    def test_example_case(self):
        """Test the provided example case"""
        N = 4
        videos = [
            ["v1", 3, 1],
            ["v2", 1, 2], 
            ["v3", 4, 1],
            ["v4", 2, 2]
        ]
        expected = ["v2", "v4", "v1", "v3"]
        result = videoProcessing(N, videos)
        self.assertEqual(result, expected)
    
    def test_single_video(self):
        """Test with only one video"""
        N = 1
        videos = [["video1", 5, 3]]
        expected = ["video1"]
        result = videoProcessing(N, videos)
        self.assertEqual(result, expected)
    
    def test_same_priority_different_times(self):
        """Test videos with same priority but different processing times"""
        N = 3
        videos = [
            ["slow", 10, 1],
            ["fast", 2, 1],
            ["medium", 5, 1]
        ]
        expected = ["fast", "medium", "slow"]  # sorted by processing time
        result = videoProcessing(N, videos)
        self.assertEqual(result, expected)
    
    def test_same_time_different_priorities(self):
        """Test videos with same processing time but different priorities"""
        N = 3
        videos = [
            ["low", 5, 1],
            ["high", 5, 3],
            ["medium", 5, 2]
        ]
        expected = ["high", "medium", "low"]  # sorted by priority desc
        result = videoProcessing(N, videos)
        self.assertEqual(result, expected)
    
    def test_complex_case(self):
        """Test more complex case with multiple priorities and times"""
        N = 6
        videos = [
            ["a", 8, 1],
            ["b", 3, 3],
            ["c", 1, 2],
            ["d", 5, 1],
            ["e", 2, 3],
            ["f", 4, 2]
        ]
        # Priority 3: e(2), b(3) 
        # Priority 2: c(1), f(4)
        # Priority 1: d(5), a(8)
        expected = ["e", "b", "c", "f", "d", "a"]
        result = videoProcessing(N, videos)
        self.assertEqual(result, expected)
    
    def test_edge_case_max_priority(self):
        """Test with maximum priority values"""
        N = 4
        videos = [
            ["v1", 1, 10],
            ["v2", 2, 10],
            ["v3", 1, 9],
            ["v4", 3, 10]
        ]
        expected = ["v1", "v2", "v4", "v3"]  # Priority 10 first, then 9
        result = videoProcessing(N, videos)
        self.assertEqual(result, expected)
    
    def test_large_processing_times(self):
        """Test with large processing times"""
        N = 3
        videos = [
            ["big", 100, 1],
            ["small", 1, 1],
            ["medium", 50, 1]
        ]
        expected = ["small", "medium", "big"]
        result = videoProcessing(N, videos)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    # Run all tests
    unittest.main(verbosity=2)