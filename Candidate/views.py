from django.shortcuts import render, get_object_or_404, redirect
from Candidate.models import *

def index(request):
    return render(request,"candidate/index.html")

def profileIds(request):
    all_roles = RolesTable.objects.all()
    selected_role_id = request.GET.get('role_id')

    if selected_role_id:
        user_data = CandidateUserTable.objects.filter(candidateroletable__CRT_roleId=selected_role_id)
    else:
        user_data = CandidateUserTable.objects.all()

    user_details = []

    for user in user_data:
        user_roles = CandidateRoleTable.objects.filter(CRT_userId=user)
        user_tags = CandidateTagTable.objects.filter(CTT_tags=user)
        user_details.append({
            'user': user,
            'user_roles': user_roles,
            'user_tags': user_tags
        })

    context = {'user_details': user_details, 'all_roles': all_roles}
    return render(request, "candidate/jobProfiles.html", context)

def individualIds(request, user_id):
    user = CandidateUserTable.objects.get(id=user_id)

    user_roles = CandidateRoleTable.objects.filter(CRT_userId=user)
    user_tags = CandidateTagTable.objects.filter(CTT_tags=user)

    if user.CUT_hard_skills:
        h_skills = [t.strip() for t in user.CUT_hard_skills.split(',')]
        formatted_hSkills = ''.join(f'<li>{hs}</li>' for hs in h_skills)
        user.hard_skills_formatted = formatted_hSkills
    else:
        user.hard_skills_formatted = ""

    if user.CUT_soft_skills:
        s_skills = [t.strip() for t in user.CUT_soft_skills.split(',')]
        formatted_sSkills = ''.join(f'<li>{ss}</li>' for ss in s_skills)
        user.soft_skills_formatted = formatted_sSkills
    else:
        user.soft_skills_formatted = ""

    if user.CUT_tools:
        tool = [t.strip() for t in user.CUT_tools.split(',')]
        formatted_tools = ''.join(f'<li>{t}</li>' for t in tool)
        user.tool_formatted = formatted_tools
    else:
        user.tool_formatted = ""

    if user.CUT_experience:
        tool = [t.strip() for t in user.CUT_experience.split(',')]
        formatted_exp = ''.join(f'<li>{e}</li>' for e in tool)
        user.exp_formatted = formatted_exp
    else:
        user.exp_formatted = ""

    if user.CUT_educational:
        tool = [t.strip() for t in user.CUT_educational.split(',')]
        formatted_edu = ''.join(f'<li>{ed}</li>' for ed in tool)
        user.edu_formatted = formatted_edu
    else:
        user.edu_formatted = ""

    if user.CUT_certifications:
        tool = [t.strip() for t in user.CUT_certifications.split(',')]
        formatted_cert = ''.join(f'<li>{c}</li>' for c in tool)
        user.cert_formatted = formatted_cert
    else:
        user.cert_formatted = ""

    context = {
        'user': user,
        'user_roles': user_roles,
        'user_tags': user_tags,
        'hard_skills_formatted': user.hard_skills_formatted,
        'soft_skills_formatted': user.soft_skills_formatted,
        'tool_formatted': user.tool_formatted,
        'exp_formatted': user.exp_formatted,
        'edu_formatted': user.edu_formatted,
        'cert_formatted': user.cert_formatted,
    }

    return render(request, "candidate/jobIndividualProfile.html", context)

def filteroption(request):
    selected_role_id = request.GET.get('role_id')  # Get the selected role ID from the request
    all_roles = RolesTable.objects.all()
    if selected_role_id:
        filtered_candidates = CandidateUserTable.objects.filter(candidateroletable__CRT_roleId=selected_role_id)
    else:
        filtered_candidates = CandidateUserTable.objects.all()
    context = {
        'all_roles': all_roles,
        'filtered_candidates': filtered_candidates,
    }
    return render(request,"candidate/filterdprofiles.html",context)
def profile(request):
    user_data = CandidateUserTable.objects.all()
    all_roles = RolesTable.objects.all()
    user_details = []

    for user in user_data:
        user_roles = CandidateRoleTable.objects.filter(CRT_userId=user)
        user_tags = CandidateTagTable.objects.filter(CTT_tags=user)
        user_details.append({
            'user': user,
            'user_roles': user_roles,
            'user_tags': user_tags,
        })

    context = {'user_details': user_details,
               'all_roles': all_roles,
               }
    return render(request,"candidate/jobProfiles.html", context)