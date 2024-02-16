from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker


# configs
engine = create_engine("mysql+pymysql://root:admin@localhost:3308/cinema")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Entidades
class Filme(Base):
    __tablename__ = "filmes"

    titulo = Column(String, primary_key=True)
    genero = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)

    def __repr__(self):
        return f"Filme (titulo={self.titulo}, ano={self.ano})"

# SQL

# Insert
data_insert = Filme(titulo="asdsadsd", genero="Acao", ano=1996)
session.add(data_insert)
session.commit()

# delete
session.query(Filme).filter(Filme.titulo == 'Dracula').delete()
session.commit()

# update
session.query(Filme).filter(Filme.genero == 'Drama').update({ "ano": 2000 })
session.commit()

# Select
data = session.query(Filme).all()
print(data)

session.close()
