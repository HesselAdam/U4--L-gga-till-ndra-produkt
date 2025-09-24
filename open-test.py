import csv
import os
import locale
import pick

def format_currency(value):
    return locale.currency(value,grouping=True)


def load_data(filename): 
    products = []
    with open(filename, 'r') as file:       #öppnar en fil med read-rättighet
        reader = csv.DictReader(file)
        for row in reader:
            id = int(row['id'])
            name = row['name']
            desc = row['desc']
            price = float(row['price'])
            quantity = int(row['quantity'])
            
            products.append(
                {                   
                    "id": id,       
                    "name": name,
                    "desc": desc,
                    "price": price,
                    "quantity": quantity
                }
            )
    return products

# SPARAR DATAN SÅ JAG KAN RADERA BORT EN PRODUKT.
def save_data(filename, products):
    with open(filename, 'w', newline='') as file:
        fieldnames = ['id', 'name', 'desc', 'price', 'quantity']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for product in products:
            writer.writerow(product)

def numererad_lista(products):
    for i, product in enumerate(products, 1):
        print(f"{product['id']}) -- {i}. {product['name']} - {format_currency(product['price'])} - {product['quantity']} st")


def get_product_by_id(products, products_id):
    for product in products:
        if product["id"] == products_id:
            return print(f"Produkt: {product['name']} Beskrivning: {product['desc']} Pris: {product['price']} Antal i lager: {product['quantity']} st")


def remove_product_by_id(products, products_id):
    for product in products:
        if product["id"] == products_id:
            products.remove(product)
            return print(f"Produkten med id {products_id} har tagits bort.")
    return None

#TODO: Lägg till en funktion för att lägga till en produkt
def add_product(products):
    print("Lägga till produkt:")
    print()
    
    new_id = max(product["id"] for product in products) + 1 if products else 1
    name = input("Ange produktens namn: ")
    desc = input("Ange produktens beskrivning: ")
    price = float(input("Ange produktens pris: "))
    quantity = int(input("Ange produktens kvantitet: "))

    new_product = {
        "id":new_id,
        "name": name,
        "desc": desc,
        "price": price,
        "quantity": quantity
    }
    products.append(new_product)
    return print(f"Produkten {name} har lagts till med id {new_id}.")

def change_product(products):
    product_id = int(input("Vilken produkt vill du ändra data för? (ange id): "))
    for product in products:
        
        print(f"Nuvarande namn för produkten är: {product['name']}")
        new_name = input("Ange det nya namnet för produkten: ")
        product['name'] = new_name if new_name else product['name']
        
        print(f"Nuvarande beskrivning för produkten är: {product['desc']}")
        new_desc = input("Ange den nya beskrivningen för produkten: ")
        product['desc'] = new_desc if new_desc else product['desc']
        
        print(f"Nuvarande pris för produkten är: {product['price']}")
        new_price = input("Ange det nya priset för produkten: ")
        product['price'] = float(new_price) if new_price else product['price']
        
        print(f"Nuvarande kvantitet för produkten är: {product['quantity']}")
        new_quantity = input("Ange den nya kvantiteten för produkten: ")
        product['quantity'] = int(new_quantity) if new_quantity else product['quantity']
        
        return print(f"Produkten med id {product_id} har uppdaterats.")

def option_menu():
    options = ["Totalt antal", "Medelvärde"]
    option = option, index = pick.pick(options, "Vilken statistik vill du veta?", indicator = ">", default_index =0)
    return option

def statistics(products, option):
    if option == "Totalt antal":
        for product in products:
            print(f"Totalt antal produkter i lager är på: {product['name']} ----> {product['quantity']} Styck ")
    
    if option == "Medelvärde":
        print()
        print("Medelvärde för produkterna i lager är:")
        total = 0
        for product in products:
            total += product['price']
        average = total / len(products)
        print(f"Medelpris: {average:.2f} Kr")

os.system('cls')
locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')  

products = load_data('db_products.csv')
    
numererad_lista(products)

val = option_menu()

statistics(products, val)

get_product_by_id(products, int(input("Ange produktens id: ")))

remove_product_by_id(products, int(input("Ange produktens id som ska tas bort: ")))

add_product(products)

change_product(products)

save_data('db_products.csv', products)