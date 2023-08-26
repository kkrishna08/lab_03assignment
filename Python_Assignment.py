class FlightTable:
    def _init_(self):
        self.data = [
            {"Location": "Mumbai", "Team 01": "India", "Team 02": "Sri Lanka", "Timing": "DAY"},
            {"Location": "Delhi", "Team 01": "England", "Team 02": "Australia", "Timing": "DAY-NIGHT"},
            {"Location": "Chennai", "Team 01": "India", "Team 02": "South Africa", "Timing": "DAY"},
            {"Location": "Indore", "Team 01": "England", "Team 02": "Sri Lanka", "Timing": "DAY-NIGHT"},
            {"Location": "Mohali", "Team 01": "Australia", "Team 02": "South Africa", "Timing": "DAY-NIGHT"},
            {"Location": "Delhi", "Team 01": "India", "Team 02": "Australia", "Timing": "DAY"}
        ]

    def search_by_team(self, team_name):
        matches = [match for match in self.data if match["Team 01"] == team_name or match["Team 02"] == team_name]
        if matches:
            return matches
        else:
            return "No matches found for the given team."

    def search_by_location(self, location_name):
        matches = [match for match in self.data if match["Location"] == location_name]
        if matches:
            return matches
        else:
            return "No matches found at the given location."

    def search_by_timing(self, timing):
        matches = [match for match in self.data if match["Timing"] == timing]
        if matches:
            return matches
        else:
            return "No matches found at the given timing."

    def display_matches(self, matches):
        if isinstance(matches, list):
            if len(matches) > 0:
                for match in matches:
                    print(f"Location: {match['Location']}, Team 01: {match['Team 01']}, Team 02: {match['Team 02']}, Timing: {match['Timing']}")
            else:
                print("No matches found.")
        else:
            print(matches)


def main():
    flight_table = FlightTable()

    while True:
        print("\nChoose a search parameter:")
        print("1. List of all the matches of a Team")
        print("2. List of Matches on a Location")
        print("3. List of Matches based on timing")
        print("4. Quit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            team_name = input("Enter the team name: ")
            matches = flight_table.search_by_team(team_name)
            flight_table.display_matches(matches)
        elif choice == "2":
            location_name = input("Enter the location name: ")
            matches = flight_table.search_by_location(location_name)
            flight_table.display_matches(matches)
        elif choice == "3":
            timing = input("Enter the timing: ")
            matches = flight_table.search_by_timing(timing)
            flight_table.display_matches(matches)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if _name_ == "_main_":
    main()