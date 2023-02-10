from app_jobs.models import City, Language


list_cities = [(city.name, city.name)for city in City.objects.all()]
list_languages = [(language.name, language.name) for language in Language.objects.all()]