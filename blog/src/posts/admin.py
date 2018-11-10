from django.contrib import admin

# for using from another applictaion
# from products.models import Product

from .models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['__str__','slug']
    class Meta:
        model = Post 

admin.site.register(Post, PostAdmin)