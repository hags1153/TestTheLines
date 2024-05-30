import requests
from bs4 import BeautifulSoup

def get_live_mlb_scores():
    url = 'https://www.espn.com/mlb/scoreboard'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    scores = []
    
    games = soup.find_all('div', class_='ScoreCell__Scoreboard')
    for game in games:
        teams = game.find_all('span', class_='sb-team-short')
        team1 = teams[0].text if teams else 'N/A'
        team2 = teams[1].text if teams else 'N/A'
        
        score1 = game.find('span', class_='ScoreCell__Score--scoreboard sb-score sb-score-0').text if game.find('span', class_='ScoreCell__Score--scoreboard sb-score sb-score-0') else 'N/A'
        score2 = game.find('span', class_='ScoreCell__Score--scoreboard sb-score sb-score-1').text if game.find('span', class_='ScoreCell__Score--scoreboard sb-score sb-score-1') else 'N/A'
        
        scores.append(f"{team1} {score1} - {team2} {score2}")
    
    return scores

if __name__ == "__main__":
    live_scores = get_live_mlb_scores()
    for score in live_scores:
        print(score)
