
from django.db import models
from user.models import User
from migsel.models import Form


class SurkolProjectDetailForm(models.Model):
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

    SURKOL_CHOICES = [
        ("ལས་འཆར་འགྲོ་གྲོན།", "ལས་འཆར་འགྲོ་གྲོན།"),
        ("འཛུཌ་སྐྲུན།", "འཛུཌ་སྐྲུན།"),
        ("འཛིན་ཆས་དང་འཕྲུལ་ཆས་གསར་ཉོ།", "འཛིན་ཆས་དང་འཕྲུལ་ཆས་གསར་ཉོ།"),
        ("ཉམས་གསོ།", "ཉམས་གསོ།"),
        ("སྤྱི་ཚོགས་འཕྲོད་བསྟེན་ལས་གཞི།", "སྤྱི་ཚོགས་འཕྲོད་བསྟེན་ལས་གཞི།"),
        ("ལས་འཆར་མིན་པའི་འགྲོ་གྲོན།", "ལས་འཆར་མིན་པའི་འགྲོ་གྲོན།"),
        ("རྒྱུན་གྲོན།", "རྒྱུན་གྲོན།"),
        ("འབབ་གྲོན་གཞན།", "འབབ་གྲོན་གཞན།"),
        ("རང་བདག་མ་དངུལ།", "རང་བདག་མ་དངུལ།"),
    ]

    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("REJECTED", "Rejected"),
        ("APPROVED", "Approved"),
    ]

    form_name = models.ForeignKey(
        Form,
        related_name="surkol_project_details_form",
        on_delete=models.CASCADE
    )
    accounts_head = models.CharField(max_length=255)
    type_of_expenses = models.CharField(
        max_length=100, choices=EXPENSES_CHOICES, default="འཛིན་སྐྱོང་འགྲོ་གྲོན།"
    )
    budget_categories = models.CharField(
        max_length=200, choices=BUDGET_CHOICES, default="སྔོན་རྩིས་དམའ་དངུལ།"
    )
    sponsor_name = models.CharField(max_length=255)
    surkol_categories = models.CharField(
        max_length=200, choices=SURKOL_CHOICES, default="འཛིན་སྐྱོང་འགྲོ་གྲོན།"
    )
    health_sector = models.BooleanField(default=False)
    local_chief_executive_office = models.BooleanField(default=False)
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
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="PENDING")
    date = models.DateField()
    user = models.ForeignKey(User, related_name='surkol_project_detail',
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100)

    def __str__(self):
        return self.accounts_head


class SurkolProjectSettlement(models.Model):

    surkol_project_detail = models.ForeignKey(
        SurkolProjectDetailForm,
        related_name="surkol_project_settlement_details_form",
        on_delete=models.CASCADE
    )
    settlement_name = models.CharField(max_length=255)
    currency_categories = models.CharField(max_length=150)
    amount = models.IntegerField()
    date = models.DateField()
    user = models.ForeignKey(User, related_name='surkol_project_settlement',
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100)

    def __str__(self):
        return self.settlement_name


class SurkolConstructionForm(models.Model):

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
    surkol_project_detail = models.ForeignKey(
        SurkolProjectDetailForm,
        related_name="surkol_project_construction_form",
        on_delete=models.CASCADE
    )
    date = models.DateField()
    user = models.ForeignKey(User, related_name='surkol_project_construction_form',
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100)

    def __str__(self):
        return self.department_name


class SurkolConstructionQuotation(models.Model):

    name = models.CharField(max_length=100)
    quotation = models.JSONField()
    surkol_project_detail = models.ForeignKey(
        SurkolProjectDetailForm,
        related_name="surkol_project_construction_quotation",
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SurkolFurnitureForm(models.Model):

    AVAILABILITY_CHOICES = [
        ("ཡོད།", "ཡོད།"),
        ("མེད།", "མེད།"),
    ]

    surkol_project_detail = models.ForeignKey(
        SurkolProjectDetailForm,
        related_name="surkol_project_furniture_form",
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
    user = models.ForeignKey(User, related_name='surkol_project_furniture',
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100)

    def __str__(self):
        return self.department_name + '-' + self.furniture_equipment


class SurkolFurnitureQuotation(models.Model):

    name = models.CharField(max_length=255)
    quotation = models.JSONField()
    surkol_project_detail = models.ForeignKey(
        SurkolProjectDetailForm,
        related_name="surkol_project_construction_quotation",
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SurkolProjectFile(models.Model):

    surkol_project_detail = models.ForeignKey(
        SurkolProjectDetailForm,
        related_name="surkol_project_project_files",
        on_delete=models.CASCADE
    )
    file_type = models.FileField(upload_to='surkol-project/')
    date = models.DateField()
    user = models.ForeignKey(User, related_name='surkol_project_file',
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100)

    def __str__(self):
        return "File: " + str(self.file_type.name) if self.file_type else "No File"


class SurkolProjectSurzarForm(models.Model):
    project_head = models.CharField(max_length=255)
    accounts_head = models.CharField(max_length=255)
    three_years_prior_opening_balance = models.IntegerField()
    two_years_prior_actual_income = models.IntegerField()
    two_years_prior_actual_expenditure = models.IntegerField()
    two_years_prior_balance = models.IntegerField()
    previous_year_final_approval_estimated_income = models.IntegerField()
    previous_year_final_approval_estimated_expenditure = models.IntegerField()
    estimated_income = models.IntegerField()
    estimate_expenditure = models.IntegerField()
    recommended_budget = models.IntegerField()
    sanctioned_budget = models.IntegerField()
    remarks = models.TextField()
    date = models.DateField()
    user = models.ForeignKey(User, related_name='surkol_project_surzar_form',
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100)

    def __str__(self):
        return self.accounts_head


class SurkolRecurringDetailForm(models.Model):
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

    SURKOL_CHOICES = [
        ("ལས་འཆར་འགྲོ་གྲོན།", "ལས་འཆར་འགྲོ་གྲོན།"),
        ("འཛུཌ་སྐྲུན།", "འཛུཌ་སྐྲུན།"),
        ("འཛིན་ཆས་དང་འཕྲུལ་ཆས་གསར་ཉོ།", "འཛིན་ཆས་དང་འཕྲུལ་ཆས་གསར་ཉོ།"),
        ("ཉམས་གསོ།", "ཉམས་གསོ།"),
        ("སྤྱི་ཚོགས་འཕྲོད་བསྟེན་ལས་གཞི།", "སྤྱི་ཚོགས་འཕྲོད་བསྟེན་ལས་གཞི།"),
        ("ལས་འཆར་མིན་པའི་འགྲོ་གྲོན།", "ལས་འཆར་མིན་པའི་འགྲོ་གྲོན།"),
        ("རྒྱུན་གྲོན།", "རྒྱུན་གྲོན།"),
        ("འབབ་གྲོན་གཞན།", "འབབ་གྲོན་གཞན།"),
        ("རང་བདག་མ་དངུལ།", "རང་བདག་མ་དངུལ།"),
    ]

    form_name = models.ForeignKey(
        Form,
        related_name="surkol_folder_detail_recurring_detail",
        on_delete=models.CASCADE
    )
    accounts_head = models.CharField(max_length=255)
    type_of_expenses = models.CharField(
        max_length=255, choices=EXPENSES_CHOICES, default="འཛིན་སྐྱོང་འགྲོ་གྲོན།"
    )
    budget_categories = models.CharField(
        max_length=255, choices=BUDGET_CHOICES, default="སྔོན་རྩིས་དམའ་དངུལ།"
    )
    health_sector = models.BooleanField(default=False)
    local_chief_executive_office = models.BooleanField(default=False)
    surkol_categories = models.CharField(
        max_length=200, choices=SURKOL_CHOICES, default="འཛིན་སྐྱོང་འགྲོ་གྲོན།"
    )
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="PENDING")
    date = models.DateField()
    user = models.ForeignKey(User, related_name='surkol_recurring_details',
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100)

    def __str__(self):
        return self.recurring_head


class SurkolRecurringSettlement(models.Model):
    surkol_recurring_detail = models.ForeignKey(
        SurkolProjectDetailForm,
        related_name="surkol_recurring_settlement_form",
        on_delete=models.CASCADE
    )
    settlement_name = models.CharField(max_length=255)
    currency_categories = models.CharField(max_length=150)
    amount = models.IntegerField()
    date = models.DateField()
    user = models.ForeignKey(User, related_name='surkol_recurring_settlement',
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100)

    def __str__(self):
        return self.settlement_name


class SurkolRecurringAccountsHead(models.Model):
    accounts_head = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name='surkol_recurring_accounts_head',
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.accounts_head


class SurkolRecurringForm(models.Model):
    accounts_head = models.ForeignKey(
        SurkolRecurringAccountsHead,
        related_name="surkol_recurring_form",
        on_delete=models.CASCADE
    )
    budget_amount = models.IntegerField()
    note = models.CharField(max_length=255)
    date = models.DateField()
    user = models.ForeignKey(User, related_name='surkol_recurring_form',
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100)

    def __str__(self):
        return self.budget_amount + "-" + self.note
