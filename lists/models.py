from django.db import models


class List(models.Model):
    CATEGORY_CHOICE = [
        ("BEGINNER", "BEGINNER"),
        ("INTERMEDIARY", "INTERMEDIARY"),
        ("ADVANCED", "ADVANCED"),
    ]
    date_day = models.DateField(auto_now_add=True)
    student_id = models.ForeignKey(
        "students.student", on_delete=models.CASCADE, related_name="list"
    )
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICE)
