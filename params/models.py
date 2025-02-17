from django.db import models
from django.utils.timezone import now
from datetime import time, datetime


class ListParams(models.Model):
    CATEGORY_CHOICE = [
        ("BEGINNER", "BEGINNER"),
        ("INTERMEDIARY", "INTERMEDIARY"),
        ("ADVANCED", "ADVANCED"),
        ("WARNING", "WARNING"),
        ("WEEKEND", "WEEKEND"),
    ]

    UNIT_CHOICES = [
        ("IPANEMA", "IPANEMA"),
        ("BARRA", "BARRA"),
    ]

    CLASS_TIME_CHOICES = [
        (time(6, 0), "06:00"),
        (time(7, 0), "07:00"),
        (time(8, 0), "08:00"),
        (time(9, 0), "09:00"),
        (time(17, 0), "17:00"),
        (time(18, 0), "18:00"),
        (time(6, 15), "06:15"),
        (time(7, 15), "07:15"),
        (time(8, 15), "08:15"),
    ]

    CATEGORY_TIMES_BY_UNIT = {
        "BEGINNER": {
            "IPANEMA": {
                0: [time(8, 0), time(18, 0)],
                1: [time(6, 0), time(8, 0), time(18, 0)],
                2: [time(8, 0), time(18, 0)],
                3: [time(6, 0), time(8, 0), time(18, 0)],
                4: [time(8, 0)],
            },
            "BARRA": {
                0: [time(7, 15), time(8, 15)],
                1: [time(7, 15), time(8, 15)],
                2: [time(7, 15), time(8, 15)],
                3: [time(7, 15), time(8, 15)],
                4: [time(7, 15), time(8, 15)],
            },
        },
        "INTERMEDIARY": {
            "IPANEMA": {
                0: [time(6, 0), time(17, 0)],
                1: [time(7, 0), time(17, 0)],
                2: [time(6, 0), time(17, 0)],
                3: [time(7, 0), time(17, 0)],
                4: [time(6, 0)],
            },
            "BARRA": {
                0: [time(6, 15)],
                2: [time(6, 15)],
                4: [time(6, 15)],
            },
        },
        "ADVANCED": {
            "IPANEMA": {
                0: [time(7, 0)],
                1: [time(9, 0)],
                2: [time(7, 0)],
                3: [time(9, 0)],
                4: [time(7, 0)],
            },
            "BARRA": {
                1: [time(6, 15)],
                3: [time(6, 15)],
            },
        },
    }

    class_date = models.DateField()
    class_time = models.TimeField(choices=CLASS_TIME_CHOICES)
    status = models.BooleanField(default=True)
    expires_at = models.DateTimeField()
    description = models.TextField()
    category = models.CharField(max_length=12, choices=CATEGORY_CHOICE)
    unit = models.CharField(max_length=7, choices=UNIT_CHOICES)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.class_time:
            if self.category in self.CATEGORY_TIMES_BY_UNIT:
                if self.unit in self.CATEGORY_TIMES_BY_UNIT[self.category]:
                    weekday = self.class_date.weekday()
                    valid_times = self.CATEGORY_TIMES_BY_UNIT[self.category][
                        self.unit
                    ].get(weekday, [])

                if self.class_time not in valid_times:
                    raise ValueError(
                        f"The class time {self.class_time.strftime("%H:%M")} is not allowed for  category {self.category} at {self.unit} on {self.class_date.strftime("%Y-%m-%d")}"
                    )
                else:
                    raise ValueError(
                        f"Invalid unit {self.unit} for category {self.category}"
                    )
            else:
                raise ValueError(f"Invalid category {self.category}")

    def save(self, *args, **kwargs):
        self.clean()
        if self.expires_at not in [self.get_option_1(), self.get_option_2()]:
            raise ValueError(
                "The `expires_at` field must be either 9:00 PM on the day of creation or 3:30 PM on the day of the class."
            )
        super().save(*args, **kwargs)

    def get_option_1(self):
        return datetime.combine(self.created_at.date(), time(21, 0))

    def get_option_2(self):
        return datetime.combine(self.class_date, time(15, 30))

    def __str__(self):
        return f"{self.class_date} - {self.category} - {self.unit} - {self.class_time.strftime("%H:%M")} - {"Active' if self.status else 'Inactive"}"
