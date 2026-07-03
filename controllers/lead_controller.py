from services.lead_finder import search_businesses


class LeadController:

    @staticmethod
    def find(keyword, country):
        print(f"Searching for: {keyword} in {country}")

        data = search_businesses(keyword, country)

        print("Returned Data:", data)

        return data