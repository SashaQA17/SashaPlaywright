import json
import os
from typing import Any
from playwright.sync_api import sync_playwright

import pytest


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="test")


@pytest.fixture(scope="session")
def env(pytestconfig) -> str:
    return pytestconfig.getoption("env")


def read_json_from_file(path: str) -> Any:
    f = open(path)
    # returns JSON object as a dictionary
    data = json.load(f)
    # Closing file
    f.close()

    return data


@pytest.fixture(scope='module', autouse=True)
def before_module(request):
    print('*----* Before module INITIALIZATION')

    # Opening JSON file
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    COMMON_CONFIG_FILE_PATH = os.path.join(ROOT_DIR, '..', 'config', 'common.json')
    ENV_COMMON_CONFIG_FILE_PATH = os.path.join(ROOT_DIR, '..', 'config', request.config.getoption("--env"),
                                               'common.json')

    data = read_json_from_file(COMMON_CONFIG_FILE_PATH)
    env_data = read_json_from_file(ENV_COMMON_CONFIG_FILE_PATH)
    data.update(env_data)

    pytest.test_data = data

    with sync_playwright() as p:
        browser = None
        if pytest.test_data['browser'] == 'chromium':
            browser = p.chromium.launch(
                headless=pytest.test_data['headless'],
                args=["--start-maximized" if pytest.test_data['maximize'] else None]
            )
        elif pytest.test_data['browser'] == 'firefox':
            browser = p.firefox.launch(
                headless=pytest.test_data['headless'],
                args=["--start-maximized" if pytest.test_data['maximize'] else None]
            )
        else:
            raise Exception("Неверный тип браузера")

        # create a new incognito browser context.
        context = browser.new_context(no_viewport=True)
        # create a new page in a pristine context.
        page = context.new_page()

        yield page

        browser.close()
        print('*----* After module END')


@pytest.fixture(autouse=True)
def before_each():
    """
        Действия выполняемые перед запуском каждого теста
    :return:
    """
    print('*-* Before each INITIALIZATION')

    try:
        yield

    except Exception as e:
        print(e)
    print('*-* After each END')


def pytest_configure(config):
    """
    Allows plugins and conftest files to perform initial configuration.
    This hook is called for every plugin and initial conftest
    file after command line options have been parsed.
    """
    print("*-* pytest_configure")


def pytest_sessionstart(session):
    """
    Called after the Session object has been created and
    before performing collection and entering the run test loop.
    """
    print("*-* pytest_sessionstart")


def pytest_sessionfinish(session, exitstatus):
    """
    Called after whole test run finished, right before
    returning the exit status to the system.
    """
    print("*-* pytest_sessionfinish")


def pytest_unconfigure(config):
    """
    called before test process is exited.
    """
    print("*-* pytest_unconfigure")
