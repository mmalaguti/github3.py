import github3
from unittest import TestCase
from .utils import mock


class TestAPI(TestCase):
    def setUp(self):
        self.mock = mock.patch('github3.api.gh', autospec=github3.GitHub)
        self.gh = self.mock.start()

    def tearDown(self):
        self.mock.stop()

    def test_zen(self):
        github3.zen()
        assert self.gh.zen.called is True
