from django.contrib import admin

from .models import Category, Comment, Genre, Review, Title


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    model = Title
    fields = ('name', 'year', 'description', 'category')
    search_fields = ('name', 'year', 'description', 'category')
    list_filter = ('name', 'year', 'description', 'category')
    empty_value_display = '-пусто-'


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    model = Genre
    fields = ('name', 'slug')
    search_fields = ('name', 'slug')
    list_filter = ('name', 'slug')
    empty_value_display = '-пусто-'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    fields = ('name', 'slug')
    search_fields = ('name', 'slug')
    list_filter = ('name', 'slug')
    empty_value_display = '-пусто-'


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    model = Review
    fields = ('title', 'text', 'author', 'score', 'pub_date')
    search_fields = ('title', 'text', 'author', 'score', 'pub_date')
    list_filter = ('title', 'text', 'author', 'score', 'pub_date')
    empty_value_display = '-пусто-'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    model = Comment
    fields = ('review', 'author', 'text', 'pub_date')
    search_fields = ('review', 'author', 'text', 'pub_date')
    list_filter = ('review', 'author', 'text', 'pub_date')
    empty_value_display = '-пусто-'
