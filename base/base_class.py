import datetime


class Base():

    def __init__(self, driver):
        self.dtiver = driver

    """Method Get Current Url"""
    def get_current_url(self):
        get_url = self.dtiver.current_url
        print(f'Current Url {get_url}')

    """Method assert word"""
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print('Good Value Word')

    """Method screenshot"""
    def get_screenshot(self):
        now_date = datetime.datetime.now(datetime.UTC)
        name_screenshot = 'screenshot' + str(now_date) + '.png'
        self.dtiver.save_screenshot(f'screen/{name_screenshot}')

    """ Method assert URL"""
    def assert_url(self, result):
        get_url = self.dtiver.current_url
        assert get_url == result
        print('Get Value URL')


