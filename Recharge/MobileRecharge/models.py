from django.db import models

# Create your models here.
oprator_ty = ['GSM', 'CDMA', 'GSM/CDMA']
ALL_OP = sorted([(item, item) for item in oprator_ty])

all_state = ['Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Delhi','Chhattisgarh','Goa','Gujarat','Haryana','Himachal Pradesh',
             'Jharkhand','Karnataka','Kerala','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland',
             'Odisha','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttarakhand','Uttar Pradesh','West Bengal']
ALL_ST = sorted([(item, item) for item in all_state])


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)

    class Meta:
        ordering = ['created']


class Oprators(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    oprator_name = models.CharField(max_length=100, blank=True, default='')
    oprator_code = models.CharField(max_length=100, blank=True, default='')
    oprator_type = models.TextField(choices=ALL_OP, blank=True, null=True)
    oprator_state = models.TextField(choices=ALL_ST, blank=True, null=True)
    # oprator_image = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ['created']


# Get all Operator Queryset
# all_opeators = Oprators.objects.all()

# AllOp = list(all_opeators.values_list('oprator_state', flat=True).distinct())
TupleState = sorted([(item, item) for item in all_state])

selected_items = list(set(Oprators.objects.values_list(
    'oprator_name', flat=True)))
# print(selected_items)
TupleOp = sorted([(item, item) for item in selected_items])

class Plans(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    plan_state = models.CharField(choices=TupleState, blank=True, null=True, max_length=100)
    plan_oprator = models.CharField(choices=TupleOp, blank=True, null=True, max_length=100)
    plan_name = models.CharField(max_length=100, blank=True, default='')
    plan_category = models.CharField(max_length=100, blank=True, default='')
    plan_price = models.CharField(max_length=100, blank=True, default='')
    plan_validity = models.CharField(max_length=100, blank=True, default='')
    plan_details = models.CharField(max_length=100, blank=True, default='')
    
    class Meta:
        ordering = ['created']

class History(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user_mobile = models.CharField(max_length=100, blank=True, default='')
    user_oprator = models.CharField(max_length=100, blank=True, default='')
    user_state = models.CharField(max_length=100, blank=True, default='')
    user_plan = models.CharField(max_length=100, blank=True, default='')
    amount = models.CharField(max_length=100, blank=True, default='')
    status = models.CharField(max_length=100, blank=True, default='')
    
    class Meta:
        ordering = ['created']
        
