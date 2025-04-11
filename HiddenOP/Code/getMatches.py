import requests, os, json
import Polars as pl

def getPuuid(name: str, tagline: str):
    """
    This function retrieves the puuid of a player using their in game name and tagline.
    """
    