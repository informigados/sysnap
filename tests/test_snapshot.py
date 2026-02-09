import unittest
from sysnap import snapshot
from sysnap import compare

class TestSysnap(unittest.TestCase):
    def test_create_snapshot_structure(self):
        """Test if snapshot has all required keys."""
        data = snapshot.create_snapshot()
        self.assertIn("meta", data)
        self.assertIn("system", data)
        self.assertIn("cpu", data)
        self.assertIn("memory", data)
        self.assertIn("disk", data)
        self.assertIn("network", data)
        
        # Check sub-keys
        self.assertIn("timestamp", data["meta"])
        self.assertIn("hostname", data["system"])
        self.assertIn("virtual_memory", data["memory"])

    def test_compare_snapshots_no_diff(self):
        """Test comparing identical snapshots."""
        data1 = {
            "system": {"hostname": "host1", "os": "Windows"},
            "memory": {"virtual_memory": {"total": 100, "free": 50, "total_human": "100B", "free_human": "50B"}},
            "disk": {"partitions": []}
        }
        diffs = compare.compare_snapshots(data1, data1)
        self.assertEqual(len(diffs), 0)

    def test_compare_snapshots_with_diff(self):
        """Test comparing different snapshots."""
        data1 = {
            "system": {"hostname": "host1"},
            "memory": {"virtual_memory": {"total": 100, "free": 50, "total_human": "100B", "free_human": "50B"}},
             "disk": {"partitions": []}
        }
        data2 = {
            "system": {"hostname": "host2"},
            "memory": {"virtual_memory": {"total": 200, "free": 50, "total_human": "200B", "free_human": "50B"}},
             "disk": {"partitions": []}
        }
        
        diffs = compare.compare_snapshots(data1, data2)
        self.assertTrue(any("Hostname" in d for d in diffs))
        self.assertTrue(any("RAM Total" in d for d in diffs))

if __name__ == '__main__':
    unittest.main()
