from lawyer.models import Reminder


def add_reminder(data):
    if data:
        reminder = Reminder.objects.create(**data)
        return reminder
    else:
        return ('Something wrong happened!')


def update_reminder(reminder_id, data):
    if data:
        reminder_item = Reminder.objects.filter(id=reminder_id)
        reminder_item.update(**data)
        return reminder_item[0]
    else:
        return ('Something wrong happened!')
