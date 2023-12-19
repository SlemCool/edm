from datetime import date


def year(request):
    """Добавляет переменную с текущим годом."""
    get_date = date.today()
    return {
        'year': get_date.year,
    }
