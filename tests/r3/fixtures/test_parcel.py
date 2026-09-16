import unittest

from parcel import EXIT_CODES, report_rows, status_label


class ParcelTests(unittest.TestCase):
    def test_labels(self):
        self.assertEqual(status_label("ok"), "Success")
        self.assertEqual(status_label("failed"), "Failed")
        self.assertEqual(status_label("pending"), "Pending")
        self.assertEqual(status_label("paused"), "paused")

    def test_structured_status_and_order(self):
        events = [
            {"id": "b", "status": "pending"},
            {"id": "a", "status": "paused"},
            {"id": "b", "status": "ok"},
        ]
        self.assertEqual(report_rows(events), [events[1], events[2]])
        self.assertEqual(report_rows([]), [])
        self.assertEqual(EXIT_CODES, {"ok": 0, "failed": 1, "pending": 2})


if __name__ == "__main__":
    unittest.main()
