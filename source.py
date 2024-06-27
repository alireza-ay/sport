import requests
from prettytable import PrettyTable


def get_league_data(league, year):
    api_url = f"https://api.football-data.org/v2/competitions/{league}/standings?season={year}"
    headers = {
        'X-Auth-Token': '4d1d14b548c7479580d6ce482839c129' 
    }
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data from API")
        return None


def display_standings(data):
    table = PrettyTable()
    table.field_names = ["startDate", "endDate", "currentMatchday", "winner name"]
    table.add_row([data['season']['startDate'], data['season']['endDate'], data['season']['currentMatchday'], data['season']['winner']['name'], ])
    print(table)


def main():
    leagues = {
        '1': 'PL',       # Premier League
        '2': 'CL',       # Champions League
        '3': 'BL1',      # Bundesliga
        '4': 'PD'        # La Liga
    }

    print("Select a league:")
    print("1. Premier League")
    print("2. Champions League")
    print("3. Bundesliga")
    print("4. La Liga")
    
    league_choice = input("Enter the number of your choice: ")
    if league_choice not in leagues:
        print("Invalid choice")
        return 0
    
    year = input("Enter the year (e.g., 2023): ")

    league = leagues[league_choice]
    data = get_league_data(league, year)
    if data:
        display_standings(data)

if __name__ == "__main__":
    main()
