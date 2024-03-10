import requests #importnuli request modeli
import re

class Database:
    def __init__(self):  #constructor. init ispolzavan dla initizaciyi
        self.sites_db = []

    def add_site(self, url, keywords):
        site = {"url": url, "keywords": keywords, "count": 0}
        self.sites_db.append(site)

    def clear_db(self):
        self.sites_db = []

class SiteParser:
    def __init__(self, search_terms):
        self.search_terms = search_terms

    def parse_site(self, url):
        response = requests.get(url)
        text = response.text.lower()

        results = {term: len(re.findall(term, text)) for term in self.search_terms}
        return results

class UserInterface:
    def get_user_input(self, prompt):
        return input(prompt)

    def display_results(self, results):
        for site in results:
            print(f"URL: {site['url']}, Count: {site['count']}")
            print("Keywords:", ", ".join(site['keywords']))
            print("")

    def display_menu(self):
        print("1. Добавте Сайт")
        print("2. Удалить дату")
        print("3. Поиск")
        print("4. Выход")

def run():
    db = Database()
    parser = SiteParser(["keyword1", "keyword2"])  # Замените на свои ключевые слова
    ui = UserInterface()

    while True:
        ui.display_menu()
        choice = int(ui.get_user_input("Введите свой выбор: "))

        if choice == 1:
            url = ui.get_user_input("Введите URL сайта: ")
            keywords = ui.get_user_input("Enter keywords (разделенные запятой): ").split(',')
            db.add_site(url, keywords)
        elif choice == 2:
            db.clear_db()
        elif choice == 3:
            for site in db.sites_db:
                results = parser.parse_site(site["url"])
                site["count"] = sum(results.values())
            sorted_sites = sorted(db.sites_db, key=lambda x: x["count"], reverse=True)
            ui.display_results(sorted_sites)
        elif choice == 4:
            break

if __name__ == "__main__": #uslobviya v skripte proverayet esli eto v main script a ne imported esli pravelno to on zapustit kod
    run()
