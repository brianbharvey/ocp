from django.db import models

# Create your model here

class Guest(models.Model):
    active_consent = models.BooleanField(default=False)
    unique_id = models.CharField(max_length=6, unique=True, blank=True, null=True, help_text='Do not assign or alter Unique IDs.')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, help_text='Include any variations, including spelling, when unconfirmed.')
    gender = models.ForeignKey('Gender', on_delete=models.CASCADE, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    otherinfo = models.CharField(max_length=500, blank=True, null=True)
    first_intake = models.DateField(null=True, blank=True, help_text='Date of first intake.')
    intake_period = models.CharField(max_length=20, blank=True, null=True, help_text='Reporting period at first access.') #Period of guest's first intake
    most_recent_intake = models.DateField(null=True, blank=True, help_text='Most recent month and year of intake.')
    status = models.ForeignKey('Status', on_delete=models.CASCADE, null=True, blank=True)
    status_notes = models.TextField(max_length=1000, blank=True, null=True, help_text='Additonal Information pertaining to Status or otherwise, include dates')
    email = models.EmailField(max_length=254, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    other_contact = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ['last_name', 'first_name']
   
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()

class IntakeReason(models.Model):
    reason = models.CharField(max_length=200)

    def __str__(self):
        return self.reason

class TurnawayReason(models.Model):
    reason = models.CharField(max_length=200)

    def __str__(self):
        return self.reason

class DiversionSupport(models.Model):
    support = models.CharField(max_length=200)

    def __str__(self):
        return self.support

class TurnawayOutcome(models.Model):
    outcome = models.CharField(max_length=200)

    class Meta:
        ordering = ['outcome']

    def __str__(self):
        return self.outcome

class Intake(models.Model):
    date = models.DateField()
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    reason = models.ForeignKey(IntakeReason, on_delete=models.SET_NULL, null=True)
    other_info = models.TextField(max_length=500, blank=True, null=True)
    notes = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return f"Intake for {self.guest.full_name()} on {self.date}"

class Turnaway(models.Model):
    date = models.DateField()
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    time = models.TimeField()
    reason = models.ForeignKey(TurnawayReason, on_delete=models.SET_NULL, null=True)
    diversion_support = models.ForeignKey(DiversionSupport, on_delete=models.SET_NULL, null=True)
    outcome = models.ForeignKey(TurnawayOutcome, on_delete=models.SET_NULL, null=True)
    follow_up = models.BooleanField(default=False)
    notes = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return f"Turnaway for {self.guest.full_name()} on {self.date}"

class Gender(models.Model):
    gender = models.CharField(max_length=50)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ['gender']
    def __str__(self):
        return self.gender

class Status(models.Model):
    status = models.CharField(max_length=50)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Statuses'
        ordering = ['status']

    def __str__(self):
        return self.status
    
class HPP(models.Model):

    STATUS_CHOICES = (
        ('Experiencing Homelessness', 'Experiencing Homelessness'),
        ('At Risk', 'At Risk'),
    )
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    hifis_id = models.CharField(max_length=100, help_text='Do not assign or alter HIFIS IDs.')
    housing_status = models.CharField(max_length=100, choices=STATUS_CHOICES, blank=True, null=True, help_text='Housing status at program entry.')
    chronic_homeless = models.BooleanField(default=False, help_text='Chronically homeless 6+ months.')
    indigenous = models.BooleanField(default=False, help_text='Identifies as indigenous.')
    from_institution = models.BooleanField(default=False, help_text=
                                           'Transitioned from provincial institution immediately prior to entering the program.') 
 
    class Meta:
        verbose_name_plural = 'HPPs'
        ordering = ['guest']

    def __str__(self):
        return f"{self.guest.full_name()}: {self.hifis_id}"