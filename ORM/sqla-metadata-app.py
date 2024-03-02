import sqlalchemy
from sqlalchemy.orm import declarative_base, relationship, Session

Base = declarative_base()

class User(Base):
    __tablename__ = "user_account"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    last_name = sqlalchemy.Column(sqlalchemy.String)

    addresses = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, last_name={self.last_name})"


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

engine = sqlalchemy.create_engine("sqlite:///:memory:")

Base.metadata.create_all(engine)

with Session(engine) as session:
    user1 = User(name="Anakin", last_name="Skywalker")
    user2 = User(name="Luke", last_name="Skywalker")
    user3 = User(name="Leia", last_name="Organa")
    address1 = Address(email_address="anakin@jedi.org", user=user1)
    address2 = Address(email_address="luke@jedi.org", user=user2)
    address3 = Address(email_address="leia@rebels.org", user=user3)

    session.add_all([user1, user2, user3, address1, address2, address3])
    session.commit()

# Usar a metadata para imprimir informações sobre as tabelas
metadata = sqlalchemy.MetaData()
metadata.reflect(bind=engine)

print("Tabelas no banco de dados:")
for table in metadata.tables.values():
    print(f"Nome: {table.name}")
    print("Colunas:")
    for column in table.c:
        print(f"  {column.name}: {column.type}")
    print()
