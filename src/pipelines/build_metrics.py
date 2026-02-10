from __future__ import annotations

import pandas as pd


def build_team_outcomes(events: pd.DataFrame) -> pd.DataFrame:
    """
    Deterministic team-season outcomes.
    Excludes rows with missing scores (no imputation).
    """
    df = events.dropna(subset=["score_home", "score_away"]).copy()

    df["home_win"] = (df["score_home"] > df["score_away"]).astype(int)
    df["away_win"] = (df["score_away"] > df["score_home"]).astype(int)
    df["tie"] = (df["score_home"] == df["score_away"]).astype(int)

    home = pd.DataFrame(
        {
            "team": df["team_home"],
            "season": df["schedule_season"],
            "games_played": 1,
            "wins": df["home_win"],
            "losses": df["away_win"],
            "ties": df["tie"],
            "points_for": df["score_home"].astype(int),
            "points_against": df["score_away"].astype(int),
        }
    )

    away = pd.DataFrame(
        {
            "team": df["team_away"],
            "season": df["schedule_season"],
            "games_played": 1,
            "wins": df["away_win"],
            "losses": df["home_win"],
            "ties": df["tie"],
            "points_for": df["score_away"].astype(int),
            "points_against": df["score_home"].astype(int),
        }
    )

    out = pd.concat([home, away], ignore_index=True)
    out = (
        out.groupby(["team", "season"], as_index=False)[
            ["games_played", "wins", "losses", "ties", "points_for", "points_against"]
        ]
        .sum()
        .sort_values(["season", "team"])
        .reset_index(drop=True)
    )
    return out


def build_season_summaries(events: pd.DataFrame) -> pd.DataFrame:
    out = (
        events.groupby("schedule_season", as_index=False)
        .agg(
            games_total=("schedule_season", "size"),
            playoff_games=("schedule_playoff", "sum"),
        )
        .rename(columns={"schedule_season": "season"})
        .sort_values("season")
        .reset_index(drop=True)
    )
    out["regular_games"] = out["games_total"] - out["playoff_games"]
    return out


def build_venue_neutral_counts(events: pd.DataFrame) -> pd.DataFrame:
    out = (
        events.groupby("schedule_season", as_index=False)
        .agg(neutral_games=("stadium_neutral", "sum"))
        .rename(columns={"schedule_season": "season"})
        .sort_values("season")
        .reset_index(drop=True)
    )
    return out
