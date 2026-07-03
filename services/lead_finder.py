from ddgs import DDGS


def search_businesses(keyword, country):
    """
    Search businesses using DDGS.
    Returns a list of tuples:
    (Company Name, Website)
    """

    query = f"{keyword} companies in {country}"

    businesses = []

    try:
        with DDGS() as ddgs:
            results = ddgs.text(query, max_results=10)

            for result in results:
                title = result.get("title", "Unknown Company")
                website = result.get("href") or result.get("url", "No Website")

                businesses.append((title, website))

    except Exception as e:
        print("Lead Finder Error:", e)

    return businesses


if __name__ == "__main__":
    data = search_businesses("supplements", "USA")

    print(f"\nFound {len(data)} businesses\n")

    for company, website in data:
        print(company)
        print(website)
        print("-" * 50)