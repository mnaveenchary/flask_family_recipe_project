from project import db

from sqlalchemy import Column, String, Integer

class Recipe(db.Model):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True)
    recipe_title = Column(String(255), nullable=False)
    recipe_description = Column(String(255), nullable=False)

    def __init__(self, title, description):
        self.recipe_title = title
        self.recipe_description = description

    def __repr__(self):
        return '<title {}'.format(self.name)