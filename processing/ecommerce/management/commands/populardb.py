# seu_projeto/seu_app/management/commands/populardb.py

from django.core.management.base import BaseCommand
from ecommerce.models import Livro, Autor


class Command(BaseCommand):
    help = "Popula o banco de dados com livros e autores."

    def handle(self, *args, **options):
        # Criando autores
        autor1 = Autor.objects.create(nome="Nietzsche")
        autor2 = Autor.objects.create(nome="Schopenhauer")
        autor3 = Autor.objects.create(nome="Darwin")

        # Criando livros e associando aos autores
        livro1 = Livro.objects.create(
            autor=autor1,
            nome="Além do bem e do mal",
            paginas=200,
            pub_date="2023-01-01",
            resumo="Lorem Ipsum",
        )
        livro2 = Livro.objects.create(
            autor=autor2,
            nome="O Mundo como Vontade e Representação",
            paginas=155,
            pub_date="2023-02-01",
            resumo="Lorem Ipsum",
        )
        livro3 = Livro.objects.create(
            autor=autor1,
            nome="Assim falava Zaratrusta",
            paginas=322,
            pub_date="2023-03-01",
            resumo="Lorem Ipsum",
        )
        livro4 = Livro.objects.create(
            autor=autor1,
            nome="O anticristo",
            paginas=200,
            pub_date="2023-01-01",
            resumo="Lorem Ipsum",
        )
        livro5 = Livro.objects.create(
            autor=autor3,
            nome="A origem das espécies",
            paginas=200,
            pub_date="2023-01-01",
            resumo="Lorem Ipsum",
        )

        self.stdout.write(self.style.SUCCESS("Banco de dados populado com sucesso!"))
