from app.models import Product, Category, User
from app import app
import hashlib


def load_categories():
    return Category.query.all()


def load_products(kw=None, cate_id=None):
    products = Product.query
    if kw:
        products = products.filter(Product.name.contains(kw))

    if cate_id:
        products = products.filter(Product.category_id.__eq__(cate_id))

    # if page:
    #     page = int(page)
    #     page_size = app.config['PAGE_SIZE']
    #     start = (page - 1) * page_size
    #     return products.slice(start, start + page_size)

    return products.all()


def get_user_by_id(user_id):
    return User.query.get(user_id)


def auth_user(username, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    return User.query.filter(User.username.__eq__(username.strip()), User.password.__eq__(password))
