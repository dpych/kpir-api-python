import kpir
from test_base import BaseTestCase

__author__ = 'Dawid Pych <dawidpych@gmail.com>'
__date__ = '19.07.15'


class MyTestCase(BaseTestCase):

    def create_app(self):
        return kpir.core.app

    def test_config_file_url_exists(self):
        url = kpir.core.config.file
        self.assertIsNotNone(url)

    def test_config_file_exists(self):
        url = kpir.core.config.file
        self.assertTrue(kpir.core.os.path.isfile(url))

    def test_database_uri(self):
        uri = kpir.core.config.SQLALCHEMY_DATABASE_URI
        self.assertIsNotNone(uri)

    def test_database_migrate_dir(self):
        dir = kpir.core.config.SQLALCHEMY_MIGRATE_REPO
        self.assertIsNotNone(dir)

    def test_is_sqllite_file_url(self):
        pass


if __name__ == '__main__':
    unittest.main()
