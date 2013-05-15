import unittest

from pegasus.service import app, db, config, migrations

class TestCase(unittest.TestCase):
    "This test case is for tests that just require the webapp"

    def setUp(self):
        config.set_debug(True)
        self.app = app.test_client()

class DBTestCase(TestCase):
    "This test case is for tests that require the database"

    def setUp(self):
        # Tests use an in-memory database
        config.set_dburi('sqlite://')
        migrations.create()

    def tearDown(self):
        db.session.remove()
        migrations.drop()

