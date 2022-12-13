from django.contrib import admin
from .models import Snippet, Oprators, Plans, History
# Register your models here.


class EmpTable(admin.ModelAdmin):
    list_display = ('id', 'created', 'title', 'code', 'linenos')
admin.site.register(Snippet, EmpTable)


class OpratorTable(admin.ModelAdmin):
    list_display = ('oprator_name', 'created',  'oprator_code',
                    'oprator_type', 'oprator_state')
admin.site.register(Oprators, OpratorTable)


class PlansTable(admin.ModelAdmin):
    list_display = ('plan_price', 'plan_name', 'created', 'plan_state',
                    'plan_oprator', 'plan_category', 'plan_validity', 'plan_details')
admin.site.register(Plans, PlansTable)


class HistoryTable(admin.ModelAdmin):
    list_display = ('user_mobile', 'created', 'user_state', 'user_oprator', 'user_plan', 'status')


admin.site.register(History, HistoryTable)
