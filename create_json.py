import json
import os
def Create():
    category = []
    count = 0
    with open("data/all_categories_dict.json", encoding="utf-8") as file:
        all_category = json.load(file)
    for category_name in all_category.items():
        if category_name[0] != 'Danone':
            name = category_name
        else:
            continue
        category_name = name[0]
        rep = [",", " ", "-", "'"]
        for i in rep:
            if i in category_name:
                category_name = category_name.replace(i, "_")
        category.append(
            {
                "Category_name": category_name,
                "Category_id": count
            }
        )
        count += 1
    with open("data/categories_item.json", "w", encoding="utf-8") as file:
        json.dump(category, file, indent=4, ensure_ascii=False)

    name = []
    with open("data/categories_item.json", encoding='utf-8') as file:
        category = json.load(file)
    for item in category:
        item = item["Category_name"]
        rep = [",", " ", "-", "'"]
        for i in rep:
            if i in item:
                item = item.replace(i, "_")
        name.append(item)

    count = 0
    category_item = []
    if count == 0:
        for item_name in name:
            with open(f"data/{count}_{item_name}.json", encoding="utf-8") as file:
                category_item.append(json.load(file))
            count +=1
    with open("data/all_products.json", "w", encoding="utf-8") as file:
        json.dump(category_item, file, indent=4, ensure_ascii=False)
    def Delete(filename):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), filename)
        os.remove(path)
    for i in category:
        x = i["Category_name"]
        y = i["Category_id"]
        js = f"data/{y}_{x}.json"
        csv = f"data/{y}_{x}.csv"
        html = f"data/{y}_{x}.html"
        Delete(csv)
        Delete(js)
        Delete(html)
    Delete("data/all_categories_dict.json")
    Delete("data/40_Danone.html")
