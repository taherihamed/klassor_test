def get_contact():
    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")

    customer = {}
    customer['name'] = name
    customer['phone'] = phone

    return customer


