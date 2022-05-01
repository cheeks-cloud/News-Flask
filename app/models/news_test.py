from tkinter import N
import unittest

from models import news

News = news.News

class NewsTest(unittest.TestCase):

  def setUp(self):
    self.newNews = News('TechCrunch','Elon\'s big week - TechCrunch',
      'https://techcrunch.com/wp-content/uploads/2019/07/DSCF2578.jpg?w=600',
      'TechCrunch Week in Review welcomes its new host, Greg Kumparak',
      'Greg Kumparak')
  

  def test_instance(self):
    self.assertTrue(isinstance(self.newNews,News))

  # def test__init(self):
  #   self.assertEqual


if __name__ == '__main__':
  unittest.main()
