import sqlite3
import pandas as pd
import streamlit as st

st.set_page_config(page_title="NFL 2024 Team Explorer", layout="wide")
st.title("NFL 2024 Team Explorer")


@st.cache_data
def run_query(sql, params=()):
    conn = sqlite3.connect("nfl.db")
    df = pd.read_sql(sql, conn, params=params)
    conn.close()
    return df


teams = run_query("SELECT DISTINCT posteam FROM plays ORDER BY posteam")["posteam"].tolist()
team = st.selectbox("Choose a team", teams, index=teams.index("WAS"))

summary = run_query(
    """
    SELECT COUNT(*) AS plays,
           ROUND(AVG(yards_gained), 2) AS yards_per_play,
           ROUND(AVG(success), 3) AS success_rate,
           ROUND(AVG(epa), 3) AS epa_per_play
    FROM plays
    WHERE posteam = ?
    """,
    (team,),
).iloc[0]

col1, col2, col3, col4 = st.columns(4)
col1.metric("Plays", int(summary["plays"]))
col2.metric("Yards per play", summary["yards_per_play"])
col3.metric("Success rate", summary["success_rate"])
col4.metric("EPA per play", summary["epa_per_play"])

weekly = run_query(
    """
    SELECT week, ROUND(AVG(epa), 3) AS epa_per_play
    FROM plays
    WHERE posteam = ?
    GROUP BY week
    ORDER BY week
    """,
    (team,),
)
weekly["rolling_3"] = weekly["epa_per_play"].rolling(3, min_periods=1).mean().round(3)

st.subheader(f"{team}: EPA per play by week")
st.line_chart(weekly.set_index("week")[["epa_per_play", "rolling_3"]])