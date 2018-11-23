import unittest
import os
import sqlalchemy

from os.path import join, dirname, abspath
from dotenv import load_dotenv

parent_dir = abspath(join(dirname(__file__), os.pardir))
dotenv_path = join(parent_dir, '.env')
load_dotenv(dotenv_path)

class TestDB(unittest.TestCase):
    def test_setUp(self):
        url = os.getenv("DATABASE_URL") + os.getenv("APP_DB")
        if not url:
            self.skipTest("No database URL set")
        self.engine = sqlalchemy.create_engine(url, isolation_level="AUTOCOMMIT")
        self.connection = self.engine.connect()

    def test_tearDown(self):
        self.connection.execute("DROP DATABASE testdb")


if __name__ == '__main__':
    unittest.main()