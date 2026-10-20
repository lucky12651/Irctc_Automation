from __future__ import annotations

import os
from dataclasses import dataclass


IRCTC_URL = "https://www.irctc.co.in/nget/train-search"


@dataclass(frozen=True)
class Settings:
    username: str
    password: str
    from_station: str
    to_station: str
    journey_date: str
    quota: str
    train_index: int
    passenger_name: str
    age: str
    gender: str
    wait_seconds: int = 20


def load_settings() -> Settings:
    username = os.getenv("IRCTC_USERNAME", "").strip()
    password = os.getenv("IRCTC_PASSWORD", "").strip()
    if not username or not password:
        raise ValueError(
            "Set IRCTC_USERNAME and IRCTC_PASSWORD in the environment or a .env file."
        )

    return Settings(
        username=username,
        password=password,
        from_station=os.getenv("IRCTC_FROM_STATION", "GHAZIABAD - GZB"),
        to_station=os.getenv("IRCTC_TO_STATION", "LUCKNOW NR - LKO"),
        journey_date=os.getenv("IRCTC_JOURNEY_DATE", "04/05/2026"),
        quota=os.getenv("IRCTC_QUOTA", "GENERAL"),
        train_index=int(os.getenv("IRCTC_TRAIN_INDEX", "15")),
        passenger_name=os.getenv("IRCTC_PASSENGER_NAME", "Nisha Srivastava"),
        age=os.getenv("IRCTC_PASSENGER_AGE", "43"),
        gender=os.getenv("IRCTC_PASSENGER_GENDER", "F"),
        wait_seconds=int(os.getenv("IRCTC_WAIT_SECONDS", "20")),
    )
