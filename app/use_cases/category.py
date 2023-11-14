from app.db.models import Category as CategoryModel
from app.schemas.category import Category


class CategoryUseCases:
    def __init__(self, db_session):
        self.db_session = db_session

    def add_category(self, category: Category):
        category_model = CategoryModel(**category.dict())
        self.db_session.add(category_model)
        self.db_session.commit()

    def list_category(self, category: Category):
        categories = self.db_session.query(CategoryModel).all()
        category_model = CategoryModel(**category.dict())
        self.db_session.add(category_model)
        self.db_session.commit()