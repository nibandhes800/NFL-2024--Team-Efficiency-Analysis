# NFL 2024 Team Efficiency Analysis

An exploratory analysis of NFL 2024 play by play data that compares team offenses by yards per play, success rate and EPA (expected points added) per play, with a SQLite database and a Streamlit app for exploring each team.
**Live app:** https://nfl2024teamefficiency.streamlit.app/

## Question
Does yards per play tell the whole story about how good an offense is?

## Data
- Source: [nflverse](https://github.com/nflverse/nflverse-data/releases/tag/pbp) play by play data for the 2024 season (`play_by_play_2024.csv`), including the playoffs.
- 49,492 plays loaded, 35,050 run and pass plays kept (the other 29.2% were kickoffs, punts, field goals and similar), 32 teams.
- The raw CSV is not in this repo because it is almost 100 MB. Download `play_by_play_2024.csv` and put it in a folder named `dataset/`.

## Key findings
- Yards per play and EPA per play are strongly related across the 32 teams: the correlation is 0.888, so about 79% of the team to team variation in EPA per play moves with yards per play.
- Yards still do not tell the whole story. WAS gained 5.73 yards per play and ATL gained 5.88, yet WAS added 0.132 expected points per play against 0.034 for ATL (EPA rank 4th vs 12th, yards per play rank 11th vs 8th).
- League averages: 5.51 yards per play and 0.01 EPA per play, with 56% of plays having negative EPA. BAL was the best offense by EPA (0.219) and CLE the worst.

## What is in this repo
- `Proj1-NFLData.ipynb`: the full analysis, covering loading and cleaning, team metrics with pandas and NumPy, charts, a written summary, and the SQL queries on the database.
- `app.py`: a Streamlit app where you pick a team and see its plays, yards per play, success rate, EPA per play and a weekly EPA chart with a 3 week rolling average.
- `nfl.db`: SQLite database with a `plays` table (run and pass plays) and a `games` table (teams and scores).
- `charts/`: EPA per play by team (`epa_per_team.png`) and yards per play vs EPA per play (`ypp_vs_epa.png`, plus an interactive `ypp_vs_epa.html`).

## How to run
1. Install the libraries: `pip install pandas numpy matplotlib seaborn plotly streamlit jupyter`
2. Start the app: `streamlit run app.py`

To rerun the analysis, download the dataset into `dataset/` (see above) and open `Proj1-NFLData.ipynb`.

## Limitations
- One season only (2024), so the results may not hold in other years.
- The correlation is based on 32 teams, which is a small sample.
- The analysis is descriptive. It shows how the measures relate, not what makes a team good.
- The data includes playoff games, where only a few teams play.

## Skills practiced
pandas, NumPy, SQL joins and window functions, Matplotlib, Seaborn, Plotly, Streamlit, git
