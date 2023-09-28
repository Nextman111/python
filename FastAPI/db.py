from datetime import datetime
import sqlalchemy as sa
import databases
from settings import settings

# set db config
DATABASE_URL = settings.DATABASE_URL
database = databases.Database(DATABASE_URL)

metadata = sa.MetaData()
engine = sa.create_engine(DATABASE_URL)

# tables
# • Таблица пользователей должна содержать следующие поля:
# id (PRIMARY KEY), имя, фамилия, адрес электронной почты и пароль.
users = sa.Table(
    "users",
    metadata,
    sa.Column(
        "id",
        sa.Integer,
        primary_key=True,
    ),
    sa.Column(
        "name",
        sa.String(32),
    ),
    sa.Column(
        "email",
        sa.String(128),
    ),
    sa.Column(
        "password",
        sa.String(8),
    ),
)

# • Таблица товаров должна содержать следующие поля:
# id (PRIMARY KEY), название, описание и цена.
products = sa.Table(
    "porducts",
    metadata,
    sa.Column(
        "id",
        sa.Integer,
        primary_key=True,
    ),
    sa.Column(
        "name",
        sa.String(32),
    ),
    sa.Column(
        "description",
        sa.String(128),
    ),
    sa.Column(
        "price",
        sa.DECIMAL(),
    ),
)

# • Таблица заказов должна содержать следующие поля:
# id (PRIMARY KEY), id пользователя (FOREIGN KEY), id товара (FOREIGN KEY), дата заказа и статус заказа.
orders = sa.Table(
    "orders",
    metadata,
    sa.Column(
        "id",
        sa.Integer,
        primary_key=True,
    ),
    sa.Column(
        "user_id",
        sa.ForeignKey("users.id"),
        nullable=False,
    ),
    sa.Column(
        "product_id",
        sa.ForeignKey("products.id"),
        nullable=False,
    ),
    sa.Column(
        "date",
        sa.Date
    ),
    sa.Column(
        "order_date",
        sa.String(64),
        nullable=False,
        default=datetime.now().strftime("%d/%m/%y, %H:%M:%S"),
        onupdate=datetime.now().strftime("%d/%m/%y, %H:%M:%S")),

    sa.Column(
        "status",
        sa.String(128),
        nullable=False,
    ),
)


metadata.create_all(engine)
