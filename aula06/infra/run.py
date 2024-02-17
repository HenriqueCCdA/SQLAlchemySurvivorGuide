from repository.atores_repository import AtoresRepository
from repository.filmes_repository import FilmesRepository

# repo = AtoresRepository()
# response = repo.select()
# print(response)

# repo2 = FilmesRepository()
# response2 = repo2.select()
# filme = response2[0]
# print(filme)
# print(filme.atores)

repo2 = FilmesRepository()
response2 = repo2.select_drama_filmes()
print(response2)
