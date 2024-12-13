from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

# Создаём бд
engine = create_engine("postgresql+psycopg2://kurram:0000@localhost/cash")

# Базовый класс для всех моделей
Base = declarative_base()

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # Связь с таблицей Product
    products = relationship("Product", back_populates="category", cascade="all, delete-orphan")

    def __repr__(self):
        return f"Category(id={self.id}, name='{self.name}')"


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'))

    # Связь с таблицей Category
    category = relationship("Category", back_populates="products")

    def __repr__(self):
        return f"Product(id={self.id}, name='{self.name}', price={self.price}, category_id={self.category_id})"

# Создаём таблицы в базе данных
Base.metadata.create_all(engine)

# Создаём сессию для работы с базой данных
Session = sessionmaker(bind=engine)
session = Session()

# CRUD-операции

# Создание категории
def create_category(name):
    category = Category(name=name)
    session.add(category)
    session.commit()
    print(f"Category created: {category}")
    return category

# Создание продукта
def create_product(name, price, category_id):
    product = Product(name=name, price=price, category_id=category_id)
    session.add(product)
    session.commit()
    print(f"Product created: {product}")
    return product

# Чтение продуктов по категории
def get_products_by_category(category_id):
    category = session.query(Category).filter_by(id=category_id).first()
    if category:
        print(f"Products in category '{category.name}':")
        for product in category.products:
            print(product)
    else:
        print("Category not found.")

# Обновление категории у продукта
def update_product_category(product_id, new_category_id):
    product = session.query(Product).filter_by(id=product_id).first()
    if product:
        product.category_id = new_category_id
        session.commit()
        print(f"Product updated: {product}")
    else:
        print("Product not found.")

# Удаление категории и всех связанных продуктов
def delete_category(category_id):
    category = session.query(Category).filter_by(id=category_id).first()
    if category:
        session.delete(category)
        session.commit()
        print(f"Category deleted: {category}")
    else:
        print("Category not found.")


# Пример использования
if __name__ == "__main__":
    # Создаём категории
    category1 = create_category("Обувь")
    category2 = create_category("Украшения")

    # Создаём продукты
    product1 = create_product("Кольцо", 2000, category2.id)
    product2 = create_product("Галоши", 500, category1.id)
    product3 = create_product("Лапти", 50, category2.id)

    # Чтение продуктов по категории
    get_products_by_category(category1.id)
    get_products_by_category(category2.id)

    # Обновление категории у продукта
    update_product_category(product3.id, category1.id)

    # Удаление категории и всех связанных продуктов
    delete_category(category1.id)