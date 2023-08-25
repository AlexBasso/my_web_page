from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from django.utils.translation import gettext_lazy as _



class IndexView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "mypage/index.html"

    def get(self, request: Request) -> Response:
        # print('printing request: ', request)
        # print('printing request.LANGUAGE_CODE : ', request.LANGUAGE_CODE)
        # print('printing request.data: ', request.data)
        data = request.data
        data["data1"] = 'Some text'
        programing_skills = [["Python"], ["Django", "DRF"], ["HTML", "CSS", "Bootstrap", "Ajax", "Postman"],
                             ["Flask", "API", "Docker", "Swagger", "Aiogram"], ["SQLite", "MySQL", "PostgreSQL"],
                             ["Git","GitHub", "GitLab"], ["NumPy", "Pandas", "Agile", "Odoo"], ["OOP", "DRY", "SOLID", "CRUD", "KISS"]]
        # programing_skills = "Python, Django, DRF, Git, API, SQLite, MySQL, PostgreSQL, Flask, HTML, CSS, Bootstrap, Aiogram, Docker, Swagger, OOP, DRY, SOLID CRUD KISS principles, Ajax, NumPy, Pandas, Agile, Postman, GitHub, GitLab, Odoo framework "
        data["programing_skills"] = programing_skills
        other_skills = ["Team player", "Project Management", "Time management", "Administration", "Accounting"]
        data["other_skills"] = other_skills
        language_skills = ["English", "Russian", "Romanian", "Italian"]
        data["language_skills"] = language_skills
        project_one = ["Python", "Django", "DRF", "API", "SQLite", "HTML", "CSS", "Bootstrap", "Docker", "Swagger"]
        data["project_one"] = project_one
        project_two = ["Python", "Django", "DRF", "API", "SQLite", "HTML", "Bootstrap", "Docker"]
        data["project_two"] = project_two
        project_three = ["Python", "Aiogram", "API", "SQLite", "Docker"]
        data["project_three"] = project_three

        return Response(data)
