class CountryInfo:
    def __init__(self):
        self.visa_data = {
            "USA": {
                "visa_required": True,
                "details": "Visa required for most travelers. Check the U.S. Department of State website for specific requirements."
            },
            "Canada": {
                "visa_required": False,
                "details": "No visa required for short stays. Check the Government of Canada website for more information."
            },
            "UK": {
                "visa_required": True,
                "details": "Visa required for most non-UK residents. Visit the UK Government website for details."
            },
            # Add more countries and their visa information as needed
        }

    def get_visa_info(self, country_name):
        return self.visa_data.get(country_name, "Visa information not available for this country.")