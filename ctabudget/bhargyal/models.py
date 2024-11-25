from django.db import models
from user.models import User
# Create your models here.
from migsel.models import Form


class BhargyalProjectDetailForm(models.Model):
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

    BUDGET_TYPE_CHOICES = [
        ("དམིགས་བསལ།", "དམིགས་བསལ།"),
        ("ཟུར་བཀོལ།", "ཟུར་བཀོལ།"),
    ]

    RULE_CHOICES = [
        ("༥", "༥"),
        ("༨", "༨"),
    ]

    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("REJECTED", "Rejected"),
        ("APPROVED", "Approved"),
    ]

    form_name = models.ForeignKey(
        Form, related_name="bhargyal_project_details_form", on_delete=models.CASCADE
    )
    accounts_head = models.CharField(max_length=255)
    type_of_expenses = models.CharField(
        max_length=255, choices=EXPENSES_CHOICES, default="འཛིན་སྐྱོང་འགྲོ་གྲོན།"
    )
    budget_categories = models.CharField(
        max_length=255, choices=BUDGET_CHOICES, default="སྔོན་རྩིས་དམའ་དངུལ།"
    )
    sponsor_name = models.CharField(max_length=255)
    budget_type = models.CharField(
        max_length=255, choices=BUDGET_TYPE_CHOICES, default="དམིགས་བསལ།"
    )
    health_sector = models.BooleanField(default=False)
    local_chief_executive_office = models.BooleanField(default=False)
    budget_rule = models.CharField(
        max_length=255, choices=RULE_CHOICES, default="༥"
    )
    project_description = models.TextField()
    status = models.CharField(
        max_length=100, choices=STATUS_CHOICES, default="PENDING")
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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100)

    def __str__(self):
        return self.accounts_head


class BhargyalProjectSettlement(models.Model):

    bhargyal_project_detail = models.ForeignKey(
        BhargyalProjectDetailForm,
        related_name="bhargyal_project_settlement_details_form",
        on_delete=models.CASCADE
    )
    settlement_name = models.CharField(max_length=255)
    currency_categories = models.CharField(max_length=150)
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100)

    def __str__(self):
        return self.settlement_name


class BhargyalConstructionForm(models.Model):

    SIGNATURE_CHOICES = [
        ("ཡོད།", "ཡོད།"),
        ("མེད།", "མེད།"),
    ]
    accounts_head = models.CharField(max_length=255)
    department_name = models.CharField(max_length=200)
    project_name_location = models.TextField()
    need_of_project = models.TextField()
    kashag_and_core_development_committee_approval = models.CharField(
        max_length=255, choices=SIGNATURE_CHOICES
    )
    approval_description = models.TextField()
    project_total_budget = models.IntegerField()
    bhargyal_project_detail = models.ForeignKey(
        BhargyalProjectDetailForm,
        related_name="bhargyal_project_construction_form",
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100)

    def __str__(self):
        return self.department_name


class BhargyalFurnitureForm(models.Model):

    AVAILABILITY_CHOICES = [
        ("ཡོད།", "ཡོད།"),
        ("མེད།", "མེད།"),
    ]

    bhargyal_project_detail = models.ForeignKey(
        BhargyalProjectDetailForm,
        related_name="bhargyal_project_details_furniture_form",
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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100)

    def __str__(self):
        return self.department_name


class BhargyalQuotation(models.Model):
    STATUS_CHOICES = [
        ('CONSTRUCTION', 'Construction'),
        ('FURNITURE', 'Furniture'),
        ('LOBUR', 'Lobur')
    ]

    form_type = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='CONSTRUCTION')
    name = models.CharField(max_length=255)
    quotation = models.JSONField()
    bhargyal_project_detail = models.ForeignKey(
        BhargyalProjectDetailForm,
        related_name="bhargyal_quotation",
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class BhargyalLoburForm(models.Model):

    SOURCE_CHOICES = [
        ("ཡོད།", "ཡོད།"),
        ("མེད།", "མེད།"),
    ]

    bhargyal_project_detail = models.ForeignKey(
        BhargyalProjectDetailForm,
        related_name="bhargyal_project_details_lobour_form",
        on_delete=models.CASCADE
    )
    project_aims = models.TextField()
    project_description = models.TextField()
    fund_source = models.CharField(max_length=10, choices=SOURCE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100)

    def __str__(self):
        return self.project_aims


class BhargyalProjectFile(models.Model):
    bhargyal_project_detail = models.ForeignKey(
        BhargyalProjectDetailForm,
        related_name="bhargyal_project_files",
        on_delete=models.CASCADE
    )
    file_type = models.FileField(upload_to='bhargyal-project/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100)

    def __str__(self):
        return "File: " + str(self.file_type.name) if self.file_type else "No File"
