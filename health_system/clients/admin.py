from django.contrib import admin
from .models import HealthProgram, Client, Enrollment

class EnrollmentInline(admin.TabularInline):
    model = Enrollment
    extra = 1
    fields = ('program', 'notes')
    readonly_fields = ('enrollment_date',)
    autocomplete_fields = ['program']

class ClientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'date_of_birth', 'gender', 'phone_number', 'programs_list')
    list_filter = ('gender', 'programs')
    search_fields = ('first_name', 'last_name', 'phone_number', 'email')
    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'date_of_birth', 'gender')
        }),
        ('Contact Information', {
            'fields': ('address', 'phone_number', 'email')
        }),
    )
    inlines = [EnrollmentInline]
    
    def programs_list(self, obj):
        return ", ".join([p.name for p in obj.programs.all()])
    programs_list.short_description = 'Enrolled Programs'

class HealthProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'description_short', 'client_count')
    search_fields = ('name', 'description')
    
    def description_short(self, obj):
        return obj.description[:50] + '...' if len(obj.description) > 50 else obj.description
    description_short.short_description = 'Description'
    
    def client_count(self, obj):
        return obj.clients.count()
    client_count.short_description = 'Clients Enrolled'

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('client', 'program', 'enrollment_date')
    list_filter = ('program', 'enrollment_date')
    search_fields = ('client__first_name', 'client__last_name', 'program__name')
    autocomplete_fields = ['client', 'program']

admin.site.register(HealthProgram, HealthProgramAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)