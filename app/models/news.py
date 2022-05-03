class News:

  def __init__(self,id,name,title,image,description,author,date):
    self.id = id
    self.name = name
    self.title = title
    self.image = image
    self.description = description
    self.author = author 
    self.date = date

class NewSource:

  def __init__(self,name,description,language,country):

    self.name=name 
    self.description=description 
    self.language=language 
    self.country=country