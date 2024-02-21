from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from infra.entities.filmes import Filmes
from infra.repository.filmes_repository import FilmesRepository

class ConnectionHandlerMock:
    def __init__(self):
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [
                        mock.call.query(Filmes),
                        mock.call.filter(Filmes.genero=="MMM"),
                    ],
                    [Filmes(titulo="Ola", genero="MMM", ano=12)],
                )
            ]
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

def test_select_drama_filmes():
    filmes_repository = FilmesRepository(ConnectionHandlerMock)
    response = filmes_repository.select_drama_filmes()
    print(response)
