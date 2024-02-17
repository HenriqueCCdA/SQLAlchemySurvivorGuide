from configs.connection import DBConnectionHandler
from entities.filmes import Filmes
from sqlalchemy.orm.exc import NoResultFound


class FilmesRepository:
    def select(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Filmes).all()
            return data

    def select_drama_filmes(self):
        try:
            with DBConnectionHandler() as db:
                data = db.session.query(Filmes).filter(Filmes.genero == 'sDrama').one()
                return data
        except NoResultFound:
            return None
        except Exception as exception:
            db.session.rollback()
            raise exception

    def insert(self, titulo, genero, ano):
        try:
            with DBConnectionHandler() as db:
                data_insert = Filmes(titulo=titulo, genero=genero, ano=ano)
                db.session.add(data_insert)
                db.session.commit()
        except Exception as exception:
            db.session.rollback()
            raise exception

    def delete(self, titulo):
        with DBConnectionHandler() as db:
            db.session.query(Filmes).filter(Filmes.titulo == titulo).delete()
            db.session.commit()

    def update(self, titulo, ano):
        with DBConnectionHandler() as db:
            db.session.query(Filmes).filter(Filmes.titulo == titulo).update({'ano': ano})
            db.session.commit()
