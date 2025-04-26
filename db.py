# from tinydb import TinyDB, Query

# # TinyDB ma'lumotlar bazasi fayllari
# db = TinyDB('db.json', indent=4, encoding='utf-8')  # DBni 'utf-8' kodlash bilan ochish
# cart = TinyDB('cart.json', indent=4, encoding='utf-8')  # cart.json faylini ham 'utf-8' kodlash bilan ochish
# item = cart.table('item')  # Cart jadvali
# q = Query()

# # Ovqat brendlarini olish
# # def get_service_titles(language: str):
# #     service_table = db.table('services')  # 'services' jadvalini olish

# #     Service = Query()

# #     # Faqat tilga mos xizmatlarni olish
# #     categories = service_table.search(Service.language == language)

# #     titles = []
# #     for category in categories:
# #         titles.append(category['title'])  # 'title' maydonini olish

# #     return titles

# def get_service_titles(language: str):
#     # 'services' jadvalini olish
#     service_table = db.table("db")
#     print(service_table)

#     Service = Query()

#     # Faqat tilga mos xizmatlarni olish
#     categories = service_table.all()

#     titles = []
#     for category in categories:
#         # 'title' maydonidan tilga mos qiymatni olish
#         title = category['title'].get(language, "Title not found for this language")
#         print(title)
#         titles.append(title)

#     return titles

# Ovqat brendlarini olish
# def get_service_titles(language):
#     from tinydb import TinyDB, Query

#     db = TinyDB('db.json')  # DBni ochish
#     service_table = db.table('services')  # 'services' jadvalini olish

#     Service = Query()

#     # Faqat tilga mos xizmatlarni olish
#     categories = service_table.search(Service.language == language)
    
#     titles = []
#     for category in categories:
#         titles.append(category['title'])  # 'title' maydonini olish

#     return titles

from tinydb import TinyDB
import json

# TinyDB ma'lumotlar bazasini yaratish
db = TinyDB('db.json', indent=4, encoding='utf-8')
services_table = db.table('services')

# JSON ma'lumotlarini bazaga yuklash (agar oldin yuklanmagan bo'lsa)
if not services_table.all():
    with open('db.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        services = data.get('services', {})
    
    for service_id, service_data in services.items():
        services_table.insert({
            'service_id': service_id,
            'service_name': service_data['service_name'],
            'title': service_data['title'],
            'description': service_data['description'],
            'price': service_data['price']
        })

def get_service_titles(language: str):
    """Tanlangan tilga mos xizmat sarlavhalarini qaytaradi"""
    
    
    titles = []
    for service in services_table.all():
        title = service['title'].get(language, "Title not found")
        titles.append(title)
    
    return titles
    

def get_service_descriptions(language: str):
    """Tanlangan tilga mos xizmat tavsiflarini qaytaradi"""
    # language_map = {
    #     'uz': "🌟 O'zbekcha",
    #     'ru': "🌐 Русский",
    #     'en': "🇬🇧 English"
    # }
    # selected_language = language_map.get(language, "🌟 O'zbekcha")
    
    with open('db.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        services = data.get('services', {})
    
    descriptions = []
    for service_id, service_data in services.items():
        description = service_data['description'].get(language, "Description not found")
        descriptions.append(description)
    
    return descriptions