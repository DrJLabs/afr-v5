import unittest

from export_csv import render_csv


class ExportTests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(render_csv([]), "id,status\n")

    def test_distinct_rows(self):
        events = [{"id": "2", "status": "failed"}, {"id": "10", "status": "ok"}]
        self.assertEqual(render_csv(events), "id,status\n10,ok\n2,failed\n")

    def test_quoted_id(self):
        self.assertEqual(
            render_csv([{"id": "a,b", "status": "paused"}]),
            'id,status\n"a,b",paused\n',
        )


if __name__ == "__main__":
    unittest.main()
