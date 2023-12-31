from sqlalchemy import Integer, Column, String, Float, Boolean, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app import db, app
from flask_login import UserMixin
import enum
from flask import url_for


class UserRole(enum.Enum):
    USER = 1
    ADMIN = 2


# Usermixin -> xac dinh model dung de chung thuc (authenticated)
class User(db.Model, UserMixin):
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(50), nullable=False)
    active = Column(Boolean, default=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    avatar = Column(String(50), default='./static/admin/image/default_useravt.jpg')
    user_role = Column(Enum(UserRole), default=UserRole.USER)

    def __str__(self):
        return self.name


class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return self.name


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    description = Column(String(255), nullable=False)
    price = Column(Float, default=0)
    image = Column(String(255))
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name


# if __name__ == "__main__":
#     with app.app_context():
#         db.create_all()
#         import hashlib
#
#         u = User(name="Admin",
#                  username="admin",
#                  password=str(hashlib.md5('Admin@123'.encode('utf-8')).hexdigest()),
#                  user_role=UserRole.ADMIN)
#         db.session.add(u)
#         db.session.commit()
#         # c1 = Category(name="Mobile")
#         # c2 = Category(name="Tablet")
#         # c3 = Category(name="Laptop")
#         #
#         # db.session.add(c1)
#         # db.session.add(c2)
#         # db.session.add(c3)
#         #
#         # db.session.commit()
#
#         # p1 = Product(name='Iphone 15 Pro', description='Iphone 15 Pro màu titanium thanh lịch, sang trọng vcl',
#         #              price=2400, image='./static/image/iphone15pro.jpg', category_id=1)
#         # p3 = Product(name='Iphone 15', description='Iphone 15 cũng được nhưng màu này đ đẹp :)', price=2000,
#         #              image='./static/image/iphone15.jpg', category_id=1)
#         # p4 = Product(name='Macbook Pro', description='Macbook pro sang trọng, ngồi code trên con này thì hết sẩy con bà bẩy', price=4000,
#         #              image='./static/image/macbookpro.jpg', category_id=3)
#         # p5 = Product(name='Ipad Pro 2021',
#         #              description='Ipad Pro 2021 cái này cũng đắt vl, đừng mua', price=3000,
#         #              image='./static/image/ipadpro.jpg', category_id=2)
#         # p6 = Product(name='Ipad Pro 2022',
#         #              description='Ipad Pro 2022 quá đắt, đừng mua phí tiền', price=3400,
#         #              image='./static/image/ipadpro2.jpg', category_id=2)
#         #
#         # db.session.add(p1)
#         # db.session.add(p3)
#         # db.session.add(p4)
#         # db.session.add(p5)
#         # db.session.add(p6)
#         #
#         # db.session.commit()
