from django import forms

from news.models import Category, News


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        labels = {
            "name": "Nome",
        }


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = "__all__"
        labels = {
            "title": "Título",
            "author": "Autor",
            "content": "Conteúdo",
            "category": "Categoria",
            "created_at": "Criado em",
            "image": "URL da imagem",
        }
        widgets = {
            "created_at": forms.DateInput(attrs={"type": "date"}),
            "content": forms.Textarea(attrs={"rows": 10}),
            "categories": forms.CheckboxSelectMultiple(),
        }
