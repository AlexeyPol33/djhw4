from django.contrib import admin
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError
from .models import Article, Scope, Tag

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            form.cleaned_data
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
            
        return super().clean()  # вызываем базовый код переопределяемого метода


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset

class ScopeAdmin(admin.ModelAdmin):
    model = Scope
    formset = ScopeInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

