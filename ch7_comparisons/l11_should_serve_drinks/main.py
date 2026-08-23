def should_serve_customer(customer_age, on_break, time):
    if customer_age >= 21:
        if not on_break: 
            if time >= 5 and time <= 10:
                return True
    return False

