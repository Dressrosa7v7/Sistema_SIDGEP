from django.contrib import admin

# Register your models here.

class PaymentFrequencyAdmin(admin.ModelAdmin):
    list_display = ['codigoP','Monthly','Weekly',]
    search_fields = ['codigoP']