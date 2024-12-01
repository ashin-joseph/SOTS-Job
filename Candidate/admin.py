from django.contrib import admin
from Candidate.models import *


admin.site.register(RolesTable)
admin.site.register(TagsTable)
admin.site.register(CandidateUserTable)
admin.site.register(CandidateRoleTable)
admin.site.register(CandidateTagTable)

