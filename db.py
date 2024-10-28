<<<<<<< HEAD
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
=======

from tinydb import TinyDB, Query
from typing import Union

# TinyDB ma'lumotlar bazasi fayllari
db = TinyDB('db.json', indent=4, encoding='utf-8')
cart = TinyDB('cart.json', indent=4)
item = cart.table('item')
q = Query()


# Ovqat brendlarini olish
def get_categories():
    return db.tables()

# Kategoriya bo'yicha ovqatlarni olish
# Kategoriya bo'yicha ovqatlarni olish
def get_foods_by_category(category: str) -> list:
    """Berilgan kategoriya bo'yicha ovqatlarni olish."""
    if category in db.tables():
        collection = db.table(category)
        try:
            foods = collection.all()  # Kategoriya bo'yicha ovqatlarni olish
        except Exception as e:
            print(f"Xatolik yuz berdi: {e}")
            return []

        # Har bir ovqat ob'ekti uchun 'id' ni kiritish
        for index, food in enumerate(foods):
            if isinstance(food, dict):  # Oziq-ovqat ob'ekti dict bo'lishi kerak
                food['id'] = str(index + 1)  # Oziq-ovqat ob'ektiga id qo'shamiz
            else:
                print(f"Xato: Oziq-ovqat ob'ekti noto'g'ri formatda: {food}")

        return foods
    else:
        print(f"Kategoriya topilmadi: {category}")
    return []


def get_food_by_id(category: str, food_id: Union[int, str], language: str) -> dict:
    # Kategoriya mavjudligini tekshirish
    if category in db.tables():
        collection = db.table(category)
        food = collection.get(doc_id=food_id)

        if food:
            # 'description' kaliti mavjudligini tekshiramiz va tilga mos tavsifni olishga harakat qilamiz
            description = food.get('description', {})
            if isinstance(description, dict):  # 'description' lug'at ekanligini tekshiramiz
                description = description.get(language, description.get("🌟 O'zbekcha", "Tavsif mavjud emas."))
            else:
                description = "Tavsif mavjud emas."

            # 'name' kaliti mavjudligini tekshiramiz va tilga mos nomni olishga harakat qilamiz
            name = food.get('name', {})
            if isinstance(name, dict):  # 'name' lug'at ekanligini tekshiramiz
                name = name.get(language, name.get("🌟 O'zbekcha", "Nom mavjud emas."))
            else:
                name = "Nom mavjud emas."

            # Boshqa ma'lumotlarni qaytarish
            return {
                "name": name,
                "category": food.get('category', "Kategoriya mavjud emas."),
                "description": description,
                "ingredients": food.get('ingredients', "Ingredientlar mavjud emas."),
                "price": food.get('price', 0),
                "img_url": food.get('img_url', "")
            }
    # Agar kategoriya yoki ovqat topilmasa, bo'sh natija qaytariladi
    return {}


def add_item(user_id: Union[int, str], category: str, food_id: Union[int, str], quantity: int = 1,
             language: str = '🌟 O\'zbekcha'):
    # Ovqat ma'lumotlarini olish
    food = get_food_by_id(category, food_id, language)  # Til parametrini uzatmoqdasiz
    if not food:  # Agar ovqat topilmasa
        print(f"Xato: Ovqat topilmadi. Kategoriya: {category}, Ovqat ID: {food_id}")
        return

    # Ovqat nomini olish
    name = food.get('name', "Nom mavjud emas.")  # To'g'ridan-to'g'ri ovqat nomini olamiz

    # Savatga qo'shadigan ma'lumotlar
    existing_item = item.get(lambda doc: doc["user_id"] == user_id and doc["food_id"] == food_id)

    if existing_item:
        # Agar item allaqachon mavjud bo'lsa, miqdorini yangilaymiz
        new_quantity = existing_item["quantity"] + quantity
        item.update({"quantity": new_quantity}, doc_ids=[existing_item.doc_id])
        print(f"{name} savatdagi miqdori yangilandi: {new_quantity} ta.")
    else:
        # Yangi item qo'shamiz
        item.insert({
            "user_id": user_id,
            "food_id": food_id,
            "category": category,
            "name": name,  # Tilga mos nomni qo'shish
            "price": food.get('price', 0),
            "quantity": quantity
        })
        print(f"{quantity} ta {name} savatga qo'shildi!")



def remove_item_from_cart_by_name(user_id, product_name):
    # Mahsulot nomiga asoslangan o'chirish logikasi
    item.remove((q.user_id == user_id) & (q.name == product_name))




# Foydalanuvchi savatini olish
def get_items(user_id: Union[int, str]):
    items = item.search(q.user_id == user_id)
    return items

# Foydalanuvchi savatini tozalash
def clear_items(user_id: Union[int, str]):
    item.remove(q.user_id == user_id)


def send_cart_summary(user_id: Union[int, str], cart_items: list, language: str = "🌟 O'zbekcha") -> str:
    total_price = 0

    translations = {
        "🌟 O'zbekcha": {
            'delete': "*«❌ Mahsulot nomi»* - savatdan o'chirish",
            'clear': "*«🔄 Tozalash»* - savatni butunlay bo'shatish",
            'cart': "\nSavatcha:",
            'total': "\nJami: {total_price} so'm",
            'currency': "so'm"
        },
        '🇬🇧 English': {
            'delete': "*«❌ Product name»* - remove from cart",
            'clear': "*«🔄 Clear»* - empty the cart",
            'cart': "\nCart:",
            'total': "\nTotal: {total_price} UZS",
            'currency': "UZS"
        },
        "🌐 Русский": {
            'delete': "*«❌ Название товара»* - удалить из корзины",
            'clear': "*«🔄 Очистить»* - очистить корзину",
            'cart': "\nКорзина:",
            'total': "\nИтого: {total_price} сум",
            'currency': "сум"
        }
    }

    translation = translations.get(language, translations["🌟 O'zbekcha"])

    summary_lines = [
        translation['delete'],
        translation['clear'],
        translation['cart']
    ]

    for item in cart_items:
        item_total = item['quantity'] * item['price']
        total_price += item_total

        # Ovqat nomini olish
        name = item['name'] if isinstance(item['name'], str) else "Noma'lum mahsulot"

        summary_lines.append(
            f"{name} \n{item['quantity']} x {item['price']} = {item_total} {translation['currency']}"
        )

    summary_lines.append(translation['total'].format(total_price=total_price))

    return "\n".join(summary_lines)

>>>>>>> cabb932 ( umid zor)
