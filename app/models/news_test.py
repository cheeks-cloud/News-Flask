
import unittest

from models import news

News = news.News

class NewsTest(unittest.TestCase):

  def setUp(self):
    self.newNews = News(1234,'TechCrunch','Elon\'s big week - TechCrunch',
      'https://techcrunch.com/wp-content/uploads/2019/07/DSCF2578.jpg?w=600',
      'TechCrunch Week in Review welcomes its new host, Greg Kumparak',
      'Greg Kumparak',"Aprill,20th 2022")
  

  def test_instance(self):
    self.assertTrue(isinstance(self.newNews,News))

  def test__init(self):
    self.assertEqual(self.newNews.id,1234)
    self.assertEqual(self.newNews.name,'Elon\'s big week - TechCrunch')
    self.assertEqual(self.newNews.title,"TechCrunch")
    self.assertEqual(self.newNews.image,"https://techcrunch.com/wp-content/uploads/2019/07/DSCF2578.jpg?w=600")
    self.assertEqual(self.newNews.description,'TechCrunch Week in Review welcomes its new host, Greg Kumparak')
    self.assertEqual(self.newNews.author,'Greg Kumparak')
    self.assertEqual(self.newNews.date,"Aprill,20th 2022")


 
   
    


if __name__ == '__main__':
  unittest.main()
