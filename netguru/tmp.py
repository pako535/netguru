from .app.models import Movie, Comments, AssociateTable

Movie.objects.create(title="Czterej Pancerni", year_of_release=1999, page=1, rank=2)
Movie.objects.create(title="To", year_of_release=1999, page=1, rank=2)
Movie.objects.create(title="Film", year_of_release=1999, page=1, rank=2)

movie = Movie.objects.all()
comment = Comments.objects.all()
AssociateTable.objects.create(movie=movie[0], comments=comment[0])
AssociateTable.objects.create(movie=movie[0], comments=comment[1])
AssociateTable.objects.create(movie=movie[0], comments=comment[2])
AssociateTable.objects.create(movie=movie[1], comments=comment[3])
AssociateTable.objects.create(movie=movie[2], comments=comment[4])
