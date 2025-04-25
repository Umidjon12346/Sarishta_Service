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

from tinydb import TinyDB, Query
import json

# TinyDB ma'lumotlar bazasini yaratish
db = TinyDB('db.json', indent=4, encoding='utf-8')
services_table = db.table('services')

# JSON ma'lumotlarini bazaga yuklash (agar oldin yuklanmagan bo'lsa)
if not services_table.all():
    with open('db.json', 'r', encoding='utf-8') as f:
        services_data = json.load(f)
    
    for service_name, service_info in services_data.items():
        services_table.insert({
            'service_name': service_name,
            'title': service_info['title'],
            'description': service_info['description'],
            'price': service_info['price']
        })

def get_service_titles(language: str):
    """Tanlangan tilga mos xizmat sarlavhalarini qaytaradi"""
    # Til kodlarini emoji belgilariga moslashtirish
    language_map = {
        'uz': "🌟 O'zbekcha",
        'ru': "🌐 Русский",
        'en': "🇬🇧 English"
    }
    selected_language = language_map.get(language, "🌟 O'zbekcha")
    
    # Barcha xizmatlarni olish
    services = services_table.all()
    
    titles = []
    for service in services:
        title = service['title'].get(selected_language, "Title not found")
        titles.append(title)
    
    return titles