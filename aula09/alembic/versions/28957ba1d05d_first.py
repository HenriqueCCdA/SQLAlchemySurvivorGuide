"""first

Revision ID: 28957ba1d05d
Revises:
Create Date: 2024-02-21 17:17:07.725538

"""
from infra.repository.filmes_repository import FilmesRepository


# revision identifiers, used by Alembic.
revision = '28957ba1d05d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    filmes_repository = FilmesRepository()
    filmes_repository.insert('Ola', 'Mundo', 123)


def downgrade() -> None:
    filmes_repository = FilmesRepository()
    filmes_repository.delete('Ola')
