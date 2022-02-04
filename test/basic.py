import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'../src/lib')))

import Telegram2RSS

class TestTelegramParsing(unittest.TestCase):

    def test_number_articles(self):
        articles = Telegram2RSS.Telegram(html=os.path.abspath(os.path.join(
            os.path.dirname(__file__),'files/postillion.html')))
        self.assertEqual(articles.length, 20)

    def test_content_first_article(self):
        articles = Telegram2RSS.Telegram(html=os.path.abspath(os.path.join(
            os.path.dirname(__file__),'files/postillion.html')))
        self.assertEqual(articles.to_list()[0].content()[:30],
                         'Sonntagsfrage: Was sagen Sie d')

    def test_time_first_article(self):
        articles = Telegram2RSS.Telegram(html=os.path.abspath(os.path.join(
            os.path.dirname(__file__),'files/postillion.html')))
        self.assertEqual(articles.to_list()[0].time().isoformat(),
                         '2022-01-30T10:27:43+00:00')
        
if __name__ == '__main__':
    unittest.main()
