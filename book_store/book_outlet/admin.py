from django.contrib import admin

from .models import Book, Author, Address, Country

# Register your models here.

# To configure the django admin app
# Add ClassAdmiin and add as a parameter in the admon.site.register()

class BookAdmin(admin.ModelAdmin):
    # readonly_fields =( "slug",)
    # para que funcione el preview no puede ser read-only
    # si quiero editarlo tengo que sacar el 'editable'=False
    # también puedo elimiar el save method que hace el override
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "rating")
    list_display = ("title", "author")

admin.site.register(Book,BookAdmin)
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Country)



