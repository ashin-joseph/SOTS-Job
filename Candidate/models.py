from django.db import models


class RolesTable(models.Model):
    RT_roles = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.RT_roles


class TagsTable(models.Model):
    TT_tags = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.TT_tags


class CandidateUserTable(models.Model):
    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Immediate Start', 'Immediate Start'),
        ('Inactive', 'Inactive'),
    ]
    CUT_first_name = models.CharField(max_length=100)  # Store first names up to 100 characters
    CUT_candidate_id = models.CharField(max_length=50, unique=True)
    CUT_roles = models.ManyToManyField(RolesTable, through='CandidateRoleTable')# Unique ID for each candidate
    CUT_status = models.CharField(max_length=20, null=True, blank=True,choices=STATUS_CHOICES)# active/inactive for each candidate
    CUT_display_summary = models.TextField(max_length=250)  # Short summary of 250 characters
    CUT_years_of_experience = models.PositiveIntegerField()  # Non-negative integer for years of experience
    CUT_location = models.CharField(max_length=100)  # Store current location up to 100 characters
    CUT_work_mode = models.CharField(max_length=50)  # Type of work (e.g., full-time, part-time)
    CUT_work_type = models.CharField(max_length=50)  # Additional type field
    CUT_hard_skills = models.TextField()  # Store hard skills in a long text field
    CUT_soft_skills = models.TextField()  # Store soft skills in a long text field
    CUT_tools = models.TextField()  # Tools the candidate is familiar with
    CUT_tags = models.ManyToManyField(TagsTable, through='CandidateTagTable')  # Tools the candidate is familiar with
    CUT_experience = models.TextField()  # Detailed experience summary
    CUT_educational = models.TextField()  # Educational background summary
    CUT_certifications = models.TextField()  # List of certifications
    CUT_note = models.TextField(blank=True, null=True)  # Optional additional notes

    def __str__(self):
        return f'{self.CUT_first_name} ({self.CUT_candidate_id})'


class CandidateRoleTable(models.Model):
    CRT_userId = models.ForeignKey(CandidateUserTable, on_delete=models.CASCADE)
    CRT_roleId = models.ForeignKey(RolesTable, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.CRT_userId.CUT_first_name} ({self.CRT_roleId.RT_roles})'


class CandidateTagTable(models.Model):
    CTT_tags = models.ForeignKey(CandidateUserTable, on_delete=models.CASCADE)
    CRT_tagId = models.ForeignKey(TagsTable, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.CTT_tags.CUT_first_name} ({self.CRT_tagId.TT_tags})'