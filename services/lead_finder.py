def search_businesses(keyword, country):
    sample_data = {
        "Supplements": [
            ("Optimum Nutrition", "https://www.optimumnutrition.com"),
            ("MyProtein", "https://www.myprotein.com"),
            ("Transparent Labs", "https://www.transparentlabs.com")
        ],
        "Skincare": [
            ("CeraVe", "https://www.cerave.com"),
            ("The Ordinary", "https://theordinary.com"),
            ("Paula's Choice", "https://www.paulaschoice.com")
        ]
    }

    return sample_data.get(keyword, [])