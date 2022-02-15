from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from blog.models import Post, Category


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ['id', 'title', 'category', 'created_at', 'views']
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('category', 'created_at')
    save_on_top = True
    fields = ('title', 'category', 'content', 'photo')


    # def get_photo(self, obj):
    #     if obj.photo:
    #         return mark_safe(f'<img src="{obj.photo.url}" width="75">')
    #     else:
    #         return '-'

admin.site.register(Post, PostAdmin)
admin.site.register(Category)

admin.site.site_title = 'Управление Блогом'
admin.site.site_header = 'Управление Блогом'