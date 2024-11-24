from django.db import models
from users.models import User
# Create your models here.


class Form(models.Model):
    name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class MangyulProjectDetailForm(models.Model):

    EXPENSES_CHOICES = [
        ("འཛིན་སྐྱོང་འགྲོ་གྲོན།", "འཛིན་སྐྱོང་འགྲོ་གྲོན།"),
        ("འཛུགས་སྐྲུན་ལས་གཞི།", "འཛུགས་སྐྲུན་ལས་གཞི།"),
        ("འཚོ་སྣོན་དང་སློབ་ཡོན།", "འཚོ་སྣོན་དང་སློབ་ཡོན།"),
        ("གཟབ་ལྗོངས་དང་ཚོངས་འདུས།", "གཟབ་ལྗོངས་དང་ཚོངས་འདུས།"),
        ("ཅ་དངོས་དང་འཕྲུལ་ཆས་གསར་ཉོ།", "ཅ་དངོས་དང་འཕྲུལ་ཆས་གསར་ཉོ།"),
        ("གཞན།", "གཞན།"),
    ]

    BUDGET_CHOICES = [
        ("སྔོན་རྩིས་དམའ་དངུལ།", "སྔོན་རྩིས་དམའ་དངུལ།"),
        ("ཟུར་བཀོལ།", "ཟུར་བཀོལ།"),
    ]

    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("REJECTED", "Rejected"),
        ("APPROVED", "Approved"),
    ]

    form_name = models.ForeignKey(
        Form,
        related_name="mangyul_project_details_form",
        on_delete=models.CASCADE
    )
    accounts_head = models.CharField(max_length=150)
    type_of_expenses = models.CharField(
        max_length=200, choices=EXPENSES_CHOICES, default="འཛིན་སྐྱོང་འགྲོ་གྲོན།"
    )
    budget_categories = models.CharField(
        max_length=200, choices=BUDGET_CHOICES, default="སྔོན་རྩིས་དམའ་དངུལ།"
    )
    sponsor_name = models.CharField(max_length=50)
    project_title = models.CharField(max_length=255)
    project_aims = models.TextField()
    project_details = models.TextField()
    project_duration = models.CharField(max_length=255)
    project_total_budget = models.IntegerField()
    fund_source = models.CharField(max_length=255)
    project_status_expenditure = models.CharField(max_length=255)
    project_activities_financial_year = models.TextField()
    receivable_amount_financial_year = models.IntegerField()
    expenditure_during_financial_year = models.IntegerField()
    date = models.DateField()
    user = models.ForeignKey(User,
                             related_name='mangyul_project_details', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100)

    def __str__(self):
        return self.accounts_head


class MangyulProjectSettlement(models.Model):

    mangyul_project_detail = models.ForeignKey(
        MangyulProjectDetailForm,
        related_name="mangyul_project_settlement_form",
        on_delete=models.CASCADE
    )
    settlement_name = models.CharField(max_length=255)
    currency_categories = models.CharField(max_length=150)
    amount = models.IntegerField()
    user = models.ForeignKey(User, related_name='mangyul_project_settlement',
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100)

    def __str__(self):
        return self.settlement_name


class MangyulConstructionForm(models.Model):

    SIGNATURE_CHOICES = [
        ("ཡོད།", "ཡོད།"),
        ("མེད།", "མེད།"),
    ]
    department_name = models.CharField(max_length=200)
    project_name_location = models.TextField()
    need_of_project = models.TextField()
    kashag_and_core_development_committee_approval = models.CharField(
        max_length=255, choices=SIGNATURE_CHOICES
    )
    approval_description = models.TextField()
    project_total_budget = models.IntegerField()
    mangyul_project_detail = models.ForeignKey(
        MangyulProjectDetailForm,
        related_name="mangyul_project_construction_form",
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(User, related_name='mangyul_project_construction_form',
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100)

    def __str__(self):
        return self.department_name


class MangyulConstructionQuotation(models.Model):
    name = models.CharField(max_length=100)
    quotation = models.JSONField()
    mangyul_project_detail = models.ForeignKey(
        MangyulProjectDetailForm,
        related_name="mangyul_project_construction_quotation",
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MangyulFurnitureForm(models.Model):

    AVAILABILITY_CHOICES = [
        ("ཡོད།", "ཡོད།"),
        ("མེད།", "མེད།"),
    ]

    mangyul_project_detail = models.ForeignKey(
        MangyulProjectDetailForm,
        related_name="mangyul_project_furniture_form",
        on_delete=models.CASCADE
    )
    department_name = models.CharField(max_length=255)
    furniture_equipment = models.CharField(max_length=255)
    nature_needs = models.TextField()
    furniture_or_equipment_availability = models.CharField(
        max_length=10, choices=AVAILABILITY_CHOICES
    )
    availability_description = models.TextField()
    total_project_budget = models.IntegerField()
    date = models.DateField()
    user = models.ForeignKey(related_name='mangyul_project_furniture',
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100)

    def __str__(self):
        return self.department_name + '-' + self.furniture_equipment


class MangyulFurnitureQuotation(models.Model):

    name = models.CharField(max_length=100)
    quotation = models.JSONField()
    mangyul_project_detail = models.ForeignKey(
        MangyulProjectDetailForm,
        related_name="mangyul_furniture_quotation",
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MangyulProjectFile(models.Model):

    mangyul_project_detail = models.ForeignKey(
        MangyulProjectDetailForm,
        related_name="mangyul_project_files",
        on_delete=models.CASCADE
    )
    file_type = models.FileField(upload_to='migsel/')
    user = models.ForeignKey(related_name='mangyul_project_file',
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100)

    def __str__(self):
        return "File: " + str(self.file_type.name) if self.file_type else "No File"


class MangyulProjectSurzarForm(models.Model):
    project_head = models.CharField(max_length=255)
    accounts_head = models.CharField(max_length=255)
    two_years_prior_approved_budget = models.IntegerField()
    two_years_prior_actual_income = models.IntegerField()
    two_years_prior_balance = models.IntegerField()
    previous_year_final_sanctioned_budget = models.IntegerField()
    estimate_expenditure = models.IntegerField()
    recommended_budget = models.IntegerField()
    sanctioned_budget = models.IntegerField()
    remarks = models.TextField()
    date = models.DateField()
    user = models.ForeignKey(User, related_name='mangyul_project_surzar_form',
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100)

    def __str__(self):
        return self.accounts_head


class MangyulProjectCoverForm(models.Model):
    accounts_head = models.CharField(max_length=255)
    two_years_prior_approved_budget = models.IntegerField()
    two_years_prior_actual_income = models.IntegerField()
    two_years_prior_balance = models.IntegerField()
    previous_year_final_sanctioned_budget = models.IntegerField()
    estimate_expenditure = models.IntegerField()
    recommended_budget = models.IntegerField()
    sanctioned_budget = models.IntegerField()
    remarks = models.TextField()
    date = models.DateField()
    user = models.ForeignKey(related_name='mangyul_project_cover_form',
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100)

    def __str__(self):
        return self.accounts_head


class MangyulRecurringDetailForm(models.Model):
    EXPENSES_CHOICES = [
        ("འཛིན་སྐྱོང་འགྲོ་གྲོན།", "འཛིན་སྐྱོང་འགྲོ་གྲོན།"),
        ("འཛུགས་སྐྲུན་ལས་གཞི།", "འཛུགས་སྐྲུན་ལས་གཞི།"),
        ("འཚོ་སྣོན་དང་སློབ་ཡོན།", "འཚོ་སྣོན་དང་སློབ་ཡོན།"),
        ("གཟབ་ལྗོངས་དང་ཚོངས་འདུས།", "གཟབ་ལྗོངས་དང་ཚོངས་འདུས།"),
        ("ཅ་དངོས་དང་འཕྲུལ་ཆས་གསར་ཉོ།", "ཅ་དངོས་དང་འཕྲུལ་ཆས་གསར་ཉོ།"),
        ("གཞན།", "གཞན།"),
    ]

    BUDGET_CHOICES = [
        ("སྔོན་རྩིས་དམའ་དངུལ།", "སྔོན་རྩིས་དམའ་དངུལ།"),
        ("ཟུར་བཀོལ།", "ཟུར་བཀོལ།"),
    ]

    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("REJECTED", "Rejected"),
        ("APPROVED", "Approved"),
    ]

    form_name = models.ForeignKey(
        Form,
        related_name="mangyul_recurring_detail_form",
        on_delete=models.CASCADE
    )
    accounts_head = models.CharField(max_length=255)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="PENDING")
    type_of_expenses = models.CharField(
        max_length=255, choices=EXPENSES_CHOICES, default="འཛིན་སྐྱོང་འགྲོ་གྲོན།"
    )
    budget_categories = models.CharField(
        max_length=255, choices=BUDGET_CHOICES, default="སྔོན་རྩིས་དམའ་དངུལ།"
    )
    date = models.DateField()
    user = models.ForeignKey(User, related_name='mangyul_recurring_detail_form',
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100)

    def __str__(self):
        return self.recurring_head


class MangyulRecurringAccountsHead(models.Model):
    accounts_head = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name='mangyul_recurring_accounts_head',
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.accounts_head


class MangyulRecurringForm(models.Model):
    accounts_head = models.ForeignKey(
        MangyulRecurringAccountsHead,
        related_name="mangyul_recurring_form",
        on_delete=models.CASCADE
    )
    budget_amount = models.IntegerField()
    note = models.CharField(max_length=255)
    date = models.DateField()
    user = models.ForeignKey(User, related_name='mangyul_recurring_form',
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100)

    def __str__(self):
        return self.budget_amount + "-" + self.note
