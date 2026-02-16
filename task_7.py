import pytest


@pytest.fixture
def user_api():
    return UserApi()


class TestUserApi:

    def test_create_user(self, user_api):


    def test_get_user(self, user_api):
        pass

    def test_block_user(self, user_api):
        pass

    def test_get_not_existing_user(self, user_api):
        pass

    def test_block_not_existing_user(self, user_api):
        pass
