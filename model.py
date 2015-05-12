from datetime import datetime
import leancloud


leancloud_id = 'vz3hsizfxtqmlqtzjacnwcn47klhorssukkctpk912ggj7f3'
leancloud_key= 'm10uzdwdd9efp54v76xj944lopr5ds0dmvziecni1wxzigqv'

try:
    import config 
    leancloud_id = config.leancloud_id
    leancloud_key = config.leancloud_key
except:
    pass

leancloud.init(leancloud_id, leancloud_key)

from leancloud import Object
from leancloud import LeanCloudError
from leancloud import User
from leancloud import Query


class Data(Object):
    @property
    def title(self):
        return self.get('title')

    @classmethod
    def take(cls, id):
        query = Query(cls)
        return query.get(id)

class Question(Data):
    #title; author; 
    @classmethod
    def add(cls, title, author):
        question = Question(title=title, author=author)
        question.save()
        return question

    @property
    def options(self):
        query = Query(Option) 
        options = query.equal_to('question', self)
        query.descending('updatedAt')
        return query.find()

    @classmethod
    def hotest(self):
        query = Query(Question)
        query.descending('updatedAt')
        return query.limit(50).find()

    @property
    def new_option(self):
        return self.options and self.options[0] or None
    
class Option(Data):
    #title;author;link;question;
    @classmethod
    def add(cls, title, author, question, link=''):
        option = Option(title=title, author=author, question=question, link=link)
        option.save()
        question.set('updatedAt', datetime.now())
        question.save()
        return option

    @property
    def reviews(self):
        query = Query(Review)
        reviews = query.equal_to('option', self)
        query.ascending('updateAt')
        return query.find()

    @property 
    def new_review(self):
        return self.reviews and self.reviews[0] or None

    @property
    def question(self):
        return self.get('question')

class Review(Data):
    #title; author; kind; option
    @classmethod
    def add(cls, title, author, option):
        review = Review(title=title, author=author, option=option)
        review.save()
        return review






if __name__ == '__main__':
    #Question.add('haha', 'hehe')
    pass

