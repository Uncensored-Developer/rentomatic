import pytest
from rentomatic.app import create_app
from rentomatic.flask_settings import DevConfig


@pytest.yield_fixture(scope='function')
def app():
    return create_app(DevConfig)


def pytest_addoption(parser):
    parser.addoption("--integration", action="store_true",
        help="run integration tests")


def pytest_runtest_setup(item):
    if 'integration' in item.keywords and not item.config.getvalue("integration"):
        pytest.skip("need --integration option to run")


@pytest.fixture(scope='session')
def db_setup():
    return {
        'postgres': {
            'dbname': 'rentomatic',
            'user': '<username>',
            'password': '<password>',
            'host': 'localhost:5432'
        }
    }
