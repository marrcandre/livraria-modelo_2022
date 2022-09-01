from django.contrib import admin

# from core.models import Autor, Categoria, Editora, Livro
from core.models.categoria import Categoria
from core.models.editora import Editora

# admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Editora)
# admin.site.register(Livro)
