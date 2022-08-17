import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser


@allure.tag('web')
@allure.severity(Severity.MINOR)
@allure.feature('Задача проверки Issue')
@allure.story('Проверяем Issue в нашем репозитории')
@allure.link('https://github.com', name='Test')
@allure.title('Title')
@allure.issue('urlIssue', name='Issue')
@allure.label('Owner', 'Test')
@allure.description('Description')
@allure.description_html('<h3>Description test</h3>')
@allure.parent_suite('Test')
@allure.sub_suite('Subsuite')
@allure.suite('Suite')
@allure.testcase('Test case')
def test_guihub_selen():
    browser.config.window_width = 1900
    browser.config.window_height = 1100
    browser.open('https://github.com')
    browser.config.hold_browser_open = True

    browser.element('.header-search-input').click()
    browser.element('.header-search-input').send_keys('eroshenkoam/allure-example')
    browser.element('.header-search-input').submit()

    browser.element(by.link_text('eroshenkoam/allure-example')).click()

    browser.element('#issues-tab').click()

    browser.element(by.partial_text('#76')).should(be.visible)


@allure.tag('web')
@allure.severity(Severity.MINOR)
@allure.feature('Задача проверки Issue')
@allure.story('Проверяем Issue в нашем репозитории')
@allure.link('https://github.com', name='Test')
@allure.title('Title')
@allure.issue('urlIssue', name='Issue')
@allure.label('Owner', 'Test')
@allure.description('Description')
@allure.description_html('<h3>Description test</h3>')
@allure.parent_suite('Test')
@allure.sub_suite('Subsuite')
@allure.suite('Suite')
@allure.testcase('Test case')
def test_dynamic_steps():
    with allure.step('Открываем главную страницу'):
        browser.config.window_width = 1900
        browser.config.window_height = 1100
        browser.open('https://github.com')
        browser.config.hold_browser_open = True

    with allure.step('Ищем репозиторий'):
        browser.element('.header-search-input').click()
        browser.element('.header-search-input').send_keys('eroshenkoam/allure-example')
        browser.element('.header-search-input').submit()

    with allure.step('Переходим по ссылке репозитория'):
        browser.element(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Открываем таб Issues'):
        browser.element('#issues-tab').click()

    with allure.step('Проверяем наличие Issues под номером #76'):
        browser.element(by.partial_text('#76')).should(be.visible)


@allure.tag('web')
@allure.severity(Severity.MINOR)
@allure.feature('Задача проверки Issue')
@allure.story('Проверяем Issue в нашем репозитории')
@allure.link('https://github.com', name='Test')
@allure.title('Title')
@allure.issue('urlIssue', name='Issue')
@allure.label('Owner', 'Test')
@allure.description('Description')
@allure.description_html('<h3>Description test</h3>')
@allure.parent_suite('Test')
@allure.sub_suite('Subsuite')
@allure.suite('Suite')
@allure.testcase('Test case')
def test_decorator_steps():
    open_main_page()
    search_for_repository('eroshenkoam/allure-example')
    go_to_repository('eroshenkoam/allure-example')
    open_issue_tab()
    should_see_issue_with_number('#76')


@allure.step('Открываем главную страницу')
def open_main_page():
    browser.config.window_width = 1900
    browser.config.window_height = 1100
    browser.open('https://github.com')
    browser.config.hold_browser_open = False


@allure.step('Ищем репозиторий {repo}')
def search_for_repository(repo):
    browser.element('.header-search-input').click()
    browser.element('.header-search-input').send_keys(repo)
    browser.element('.header-search-input').submit()


@allure.step('Переходим по ссылке репозитория {repo}')
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step('Открываем таб Issues')
def open_issue_tab():
    browser.element('#issues-tab').click()


@allure.step('Проверяем наличие Issues под номером {repo}')
def should_see_issue_with_number(repo):
    browser.element(by.partial_text(repo)).should(be.visible)