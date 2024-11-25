from django.db import models


class KhagyurProjectCoverForm(models.Model):
    STATUS_CHOICES = [
        ('surzar', 'Surzar'),
        ('cover', 'Cover')
    ]

    form_type = models.CharField(
        max_length=100, choices=STATUS_CHOICES, default='surzar')
    accounts_head_expenditure = models.CharField(max_length=255)
    approval_request_income_expenditure = models.IntegerField()
    approval_request_expenditure_expenditure = models.IntegerField()
    approval_request_recommended_budget_expenditure = models.IntegerField()
    approval_request_sanctioned_budget_expenditure = models.IntegerField()
    accounts_head_income = models.CharField(max_length=255)
    approval_request_income_income = models.IntegerField()
    approval_request_expenditure_income = models.IntegerField()
    approval_request_recommended_budget_income = models.IntegerField()
    approval_request_sanctioned_budget_income = models.IntegerField()
    remarks = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100)

    def __str__(self):
        return self.accounts_head


class KhagyurProjectGyapjongExpenditureForm(models.Model):
    STATUS_CHOICES = [
        ('surzar', 'Surzar'),
        ('cover', 'Cover')
    ]

    form_type = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='surzar')
    accounts_head_expenditure = models.CharField(max_length=255)
    approved_budget_income = models.IntegerField()
    approved_budget_expenditure = models.IntegerField()
    actual_expenditure_income = models.IntegerField()
    actual_expenditure_expenditure = models.IntegerField()
    balance_income = models.IntegerField()
    balance_expenditure = models.IntegerField()
    khagyur_income_subtraction = models.IntegerField()
    khagyur_expenditure_subtraction = models.IntegerField()
    budget_approval_recommended_income = models.IntegerField()
    budget_approval_recommended_expenditure = models.IntegerField()
    remarks = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100)

    def __str__(self):
        return self.accounts_head_expenditure


class KhagyurProjectGyapjongIncomeForm(models.Model):
    STATUS_CHOICES = [
        ('surzar', 'Surzar'),
        ('cover', 'Cover')
    ]

    form_type = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='surzar')
    accounts_head_income = models.CharField(max_length=255)
    approved_budget_income = models.IntegerField()
    approved_budget_expenditure = models.IntegerField()
    actual_expenditure_income = models.IntegerField()
    actual_expenditure_expenditure = models.IntegerField()
    balance_income = models.IntegerField()
    balance_expenditure = models.IntegerField()
    khagyur_income_subtraction = models.IntegerField()
    khagyur_expenditure_subtraction = models.IntegerField()
    budget_approval_recommended_income = models.IntegerField()
    budget_approval_recommended_expenditure = models.IntegerField()
    remarks = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100)

    def __str__(self):
        return self.accounts_head_income


class KhagyurRecurringCoverForm(models.Model):
    accounts_head_expenditure = models.CharField(max_length=255)
    approval_request_expenditure = models.IntegerField()
    approval_recommended_expenditure = models.IntegerField()
    approval_sanctioned_expenditure = models.IntegerField()
    accounts_head_income = models.CharField(max_length=255)
    approval_request_income = models.IntegerField()
    approval_recommended_income = models.IntegerField()
    approval_sanctioned_income = models.IntegerField()
    remarks = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100)

    def __str__(self):
        return self.accounts_head_expenditure


class KhagyurRecurringGyapjongExpenditureForm(models.Model):

    accounts_head_expenditure = models.CharField(max_length=255)
    approved_budget_income = models.IntegerField()
    approved_budget_expenditure = models.IntegerField()
    actual_expenditure_income = models.IntegerField()
    actual_expenditure_expenditure = models.IntegerField()
    balance_income = models.IntegerField()
    balance_expenditure = models.IntegerField()
    khagyur_income_subtraction = models.IntegerField()
    khagyur_expenditure_subtraction = models.IntegerField()
    budget_approval_recommended_income = models.IntegerField()
    budget_approval_recommended_expenditure = models.IntegerField()
    remarks = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100)

    def __str__(self):
        return self.accounts_head_expenditure


class KhagyurRecurringGyapjongIncomeForm(models.Model):

    accounts_head_income = models.CharField(max_length=255)
    approved_budget_income = models.IntegerField()
    approved_budget_expenditure = models.IntegerField()
    actual_expenditure_income = models.IntegerField()
    actual_expenditure_expenditure = models.IntegerField()
    balance_income = models.IntegerField()
    balance_expenditure = models.IntegerField()
    khagyur_income_subtraction = models.IntegerField()
    khagyur_expenditure_subtraction = models.IntegerField()
    budget_approval_recommended_income = models.IntegerField()
    budget_approval_recommended_expenditure = models.IntegerField()
    remarks = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100)

    def __str__(self):
        return self.accounts_head_income
