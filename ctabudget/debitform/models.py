from django.db import models
from user.models import User
# Create your models here.


class DebitForm(models.Model):

    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("REJECTED", "Rejected"),
        ("APPROVED", "Approved"),
    ]

    budget_category = models.CharField(max_length=255)
    budget_sub_category = models.CharField(max_length=255)
    settlement = models.CharField(max_length=255)
    receipt_number = models.CharField(max_length=255)
    date = models.DateField()
    accounts_head = models.CharField(max_length=255)
    budget_approval = models.IntegerField()
    note = models.TextField()
    bhargyal_approval = models.IntegerField(null=True)
    budget_final_approval = models.IntegerField()
    withdrawn_so_far = models.IntegerField()
    budget_approval_balance = models.IntegerField()
    withdraw_deposit = models.CharField(max_length=100, default="བཅུག།")
    withdraw_deposit_amount = models.IntegerField()
    balance = models.IntegerField()
    payment_mode = models.CharField(max_length=255)
    cheque_number = models.CharField(max_length=100, null=True, blank=True)
    respected_signature = models.CharField(max_length=100)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="PENDING")
    user = models.ForeignKey(User, related_name='debit_form',
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100)

    def __str__(self):
        return self.budget_category + '-' + self.budget_sub_category + '-' + self.accounts_head


class CreditForm(models.Model):

    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("REJECTED", "Rejected"),
        ("APPROVED", "Approved"),
    ]

    budget_category_income = models.CharField(max_length=255)
    budget_sub_category = models.CharField(max_length=255)
    settlement = models.CharField(max_length=255)
    receipt_number = models.CharField(max_length=255)
    date = models.DateField()
    accounts_head = models.CharField(max_length=255)
    budget_approval = models.IntegerField()
    note = models.TextField()
    bhargyal_approval_income = models.IntegerField(null=True)
    budget_final_approval = models.IntegerField()
    deposit_so_far = models.IntegerField()
    budget_approval_balance = models.IntegerField()
    actual_income = models.IntegerField()
    balance = models.IntegerField()
    payment_mode = models.CharField(max_length=255)
    cheque_number = models.CharField(max_length=100, null=True, blank=True)
    respected_signature = models.CharField(max_length=100)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="PENDING")
    user = models.ForeignKey(User, related_name='credit_form',
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100)

    def __str__(self):
        return self.budget_category_income + '-' + self.budget_sub_category + '-' + self.accounts_head
