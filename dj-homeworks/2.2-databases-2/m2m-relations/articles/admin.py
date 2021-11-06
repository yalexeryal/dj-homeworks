from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope


class ScopesInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            if form.cleaned_data:
                if form.cleaned_data['is_main']:
                    count += 1
        if count < 1:
            raise ValidationError('Укажите основной раздел')
        if count > 1:
            raise ValidationError('Основным может быть только один раздел')
        return super().clean()


class RelationshipInline(admin.TabularInline):
    model = Scope
    formset = ScopesInlineFormset


@admin.register(Article)
class ObjectAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]