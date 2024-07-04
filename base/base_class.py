class Base():

    def __init__(self, driver):
        self.dtiver = driver

    """Method Get Current Url"""
    def get_current_url(self):
        get_url = self.dtiver.current_url
        print(f'Current Url {get_url}')

    """ Method assert word"""
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print('Good Value Word')
