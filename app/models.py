class News:

  def __init__(self,id,name,title,image,description,author,date,news):
    self.id = id
    self.name = name
    self.title = title
    self.image = image
    self.news = news
    self.description = description
    self.author = author 
    self.date = date

class NewSource:

  def __init__(self,id,name,description,country):
    self.id = id
    self.name=name 
    self.description=description 
    self.country=country