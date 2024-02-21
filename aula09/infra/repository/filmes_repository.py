from infra.entities.filmes import Filmes
from sqlalchemy.orm.exc import NoResultFound


class FilmesRepository:

    def __init__(self, ConnectionHandler):
        self.__ConnectionHandler = ConnectionHandler

    def select(self):
        with self.__ConnectionHandler() as db:
            data = db.session.query(Filmes).all()
            return data

    def select_drama_filmes(self):
        try:
            with self.__ConnectionHandler() as db:
                data = db.session.query(Filmes).filter(Filmes.genero == 'sDrama').one()
                return data
        except NoResultFound:
            return None
        except Exception as exception:
            db.session.rollback()
            raise exception

    def insert(self, titulo, genero, ano):
        try:
            with self.__ConnectionHandler() as db:
                data_insert = Filmes(titulo=titulo, genero=genero, ano=ano)
                db.session.add(data_insert)
                db.session.commit()
        except Exception as exception:
            db.session.rollback()
            raise exception

    def delete(self, titulo):
        with self.__ConnectionHandler() as db:
            db.session.query(Filmes).filter(Filmes.titulo == titulo).delete()
            db.session.commit()

    def update(self, titulo, ano):
        with self.__ConnectionHandler() as db:
            db.session.query(Filmes).filter(Filmes.titulo == titulo).update({'ano': ano})
            db.session.commit()
