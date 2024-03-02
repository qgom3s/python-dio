# Integrating Python with SQLite using SQLAlchemy
import sqlalchemy
from sqlalchemy.orm import declarative_base, relationship, Session

Base = declarative_base()


class User(Base):
    __tablename__ = "user_account"

    # Attributes
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    last_name = sqlalchemy.Column(sqlalchemy.String)

    addresses = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )


def __repr__(self):
    return "User(id={self.id}, name={self.name}, last_name={self.last_name})"


class Address(Base):
    __tablename__ = "address"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    email_address = sqlalchemy.Column(sqlalchemy.String(40), nullable=False)
    user_id = sqlalchemy.Column(
        sqlalchemy.Integer, sqlalchemy.ForeignKey("user_account.id"), nullable=False
    )

    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return f"Address(id={self.id}, email_address={self.email_address})"


# print(User.__tablename__)
# print(Address.__tablename__)

# Integrating with the database
engine = sqlalchemy.create_engine("sqlite://")

# Create the classes as tables in the database
Base.metadata.create_all(engine)

# Fetching data
inspect_engine = sqlalchemy.inspect(engine)
# print(inspect_engine.has_table("user_account"))

# Adding users
with Session(engine) as sess:
    vader = User(
        name="Anakin",
        last_name="Skywalker",
        addresses=[Address(email_address="vader@ordem.sith")],
    )

    luke = User(
        name="Luke",
        last_name="Skywalker",
        addresses=[Address(email_address="luke@ordem.jedi")],
    )

    leia = User(
        name="Leia",
        last_name="Organa/Skywalker",
        addresses=[
            Address(email_address="leia@ordem.jedi"),
            Address(email_address="leia@senado.rep"),
        ],
    )

    maul = User(name="Maul", last_name="Darth")

    # Sending to the database
    sess.add_all([vader, luke, leia, maul])
    sess.commit()

print("Retrieving users through filtering...")
stmt = sqlalchemy.select(User).where(User.name.in_(["Anakin", "Leia"]))

for user in sess.scalars(stmt):
    print(f"ID: {user.id}, Name: {user.name}, Last Name: {user.last_name}")

# stmt = sqlalchemy.select(User).where(User.name.in_(["Vader", "Luke", "Leia"]))

# # New session to interact with the database
# with Session(engine) as sess:
#     result = sess.execute(stmt)

#     for user in result.scalars():
#         print(user)

print("Retrieving user emails...")
stmt_add = sqlalchemy.select(Address).where(Address.user_id.in_([3]))

for add in sess.scalars(stmt_add):
    print(f"Name: {add.user.name}, E-Mail: {add.email_address}.")

print("Retrieving data in an ordered manner...")
stmt_sorting = sqlalchemy.select(User).order_by(User.last_name.desc())
for res in sess.scalars(stmt_sorting):
    print(res.last_name)

stmt_join = sqlalchemy.select(User.name, Address.email_address).join_from(Address, User)
connection = engine.connect()
result = connection.execute(stmt_join).fetchall()
for res in result:
    print(res)


count = Session(engine).query(sqlalchemy.func.count()).select_from(User).scalar()
print(count)

