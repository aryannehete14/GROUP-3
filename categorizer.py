def categorize_expense(text):

    text = text.lower()

    food_keywords = [
        "domino",
        "pizza",
        "burger",
        "zomato",
        "swiggy"
    ]

    travel_keywords = [
        "uber",
        "ola",
        "taxi"
    ]

    for word in food_keywords:
        if word in text:
            return "Food"

    for word in travel_keywords:
        if word in text:
            return "Travel"

    return "Others"