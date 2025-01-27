from datetime import timedelta

from django.utils.timezone import now

from .models import List


def can_add_to_list(student):

    today = now()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = today + timedelta(days=4)

    frequency_count = List.objects.filter(
        student=student,
        created_at__date__gte=start_of_week.date(),
        created_at__date__lte=end_of_week.date(),
    ).count()

    frequency_mapping = {
        "1X": 1,
        "2X": 2,
        "3X": 3,
        "4X": 4,
        "5X": 5,
    }

    max_frequency = frequency_mapping.get(student.frequency_of_classes, 0)

    return frequency_count < max_frequency
