from Core.models import *


# Create your models here.
class Reseller(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now_add=True)
    percentage_on_first = models.FloatField(default=0.0)
    percentage_on_renewal = models.FloatField(default=0.0)
    allow_negative_balance = models.BooleanField(default=False)
    max_negative_balance = models.FloatField(default=0.0)
    credit = models.FloatField(default=0)

    def __str__(self):
        return self.user.username

    def calculate_credit(self):
        credit = 0
        for x in ResellerTransaction.objects.filter(reseller=self.user):
            credit += x.amount
        return credit


class Service(models.Model):
    name = models.CharField(max_length=128)
    months_to_add = models.IntegerField(default=1)
    allowed_size = models.FloatField(default=2)
    price = models.FloatField(default=0.0)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Offers(models.Model):
    name = models.CharField(max_length=128)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    for_new_customers = models.BooleanField(default=True)
    for_renewal = models.BooleanField(default=True)

    def __str__(self):
        return self.name + ' - ' + self.service.name


class CustomerTransaction(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    instance = models.ForeignKey(Instance, on_delete=models.SET_NULL, null=True)
    amount = models.FloatField(default=0.0)
    done_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ['-id']


class ResellerTransaction(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    reseller = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    customer_transaction = models.ForeignKey(CustomerTransaction, on_delete=models.CASCADE, null=True)
    amount = models.FloatField(default=0, verbose_name='Amount')
    comment = models.TextField(null=True, verbose_name='Comment', blank=True)

    def __str__(self):
        return str(self.id)

    def discount(self):
        return self.customer_transaction.amount + self.amount

    class Meta:
        ordering = ['-id']
