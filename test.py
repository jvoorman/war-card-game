import game
import json
import pytest
import re
from unittest.mock import MagicMock
import requests
import dev_space

mock_deck = json.loads(
"""
{
    "success": true,
    "deck_id": "9hw727op8fe7",
    "cards": [
        {
            "code": "0C",
            "image": "https://deckofcardsapi.com/static/img/0C.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/0C.svg",
                "png": "https://deckofcardsapi.com/static/img/0C.png"
            },
            "value": "10",
            "suit": "CLUBS"
        },
        {
            "code": "2H",
            "image": "https://deckofcardsapi.com/static/img/2H.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/2H.svg",
                "png": "https://deckofcardsapi.com/static/img/2H.png"
            },
            "value": "2",
            "suit": "HEARTS"
        },
        {
            "code": "KH",
            "image": "https://deckofcardsapi.com/static/img/KH.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/KH.svg",
                "png": "https://deckofcardsapi.com/static/img/KH.png"
            },
            "value": "KING",
            "suit": "HEARTS"
        },
        {
            "code": "KS",
            "image": "https://deckofcardsapi.com/static/img/KS.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/KS.svg",
                "png": "https://deckofcardsapi.com/static/img/KS.png"
            },
            "value": "KING",
            "suit": "SPADES"
        },
        {
            "code": "9D",
            "image": "https://deckofcardsapi.com/static/img/9D.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/9D.svg",
                "png": "https://deckofcardsapi.com/static/img/9D.png"
            },
            "value": "9",
            "suit": "DIAMONDS"
        },
        {
            "code": "JD",
            "image": "https://deckofcardsapi.com/static/img/JD.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/JD.svg",
                "png": "https://deckofcardsapi.com/static/img/JD.png"
            },
            "value": "JACK",
            "suit": "DIAMONDS"
        },
        {
            "code": "5H",
            "image": "https://deckofcardsapi.com/static/img/5H.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/5H.svg",
                "png": "https://deckofcardsapi.com/static/img/5H.png"
            },
            "value": "5",
            "suit": "HEARTS"
        },
        {
            "code": "AH",
            "image": "https://deckofcardsapi.com/static/img/AH.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/AH.svg",
                "png": "https://deckofcardsapi.com/static/img/AH.png"
            },
            "value": "ACE",
            "suit": "HEARTS"
        },
        {
            "code": "0S",
            "image": "https://deckofcardsapi.com/static/img/0S.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/0S.svg",
                "png": "https://deckofcardsapi.com/static/img/0S.png"
            },
            "value": "10",
            "suit": "SPADES"
        },
        {
            "code": "KD",
            "image": "https://deckofcardsapi.com/static/img/KD.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/KD.svg",
                "png": "https://deckofcardsapi.com/static/img/KD.png"
            },
            "value": "KING",
            "suit": "DIAMONDS"
        },
        {
            "code": "9S",
            "image": "https://deckofcardsapi.com/static/img/9S.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/9S.svg",
                "png": "https://deckofcardsapi.com/static/img/9S.png"
            },
            "value": "9",
            "suit": "SPADES"
        },
        {
            "code": "9H",
            "image": "https://deckofcardsapi.com/static/img/9H.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/9H.svg",
                "png": "https://deckofcardsapi.com/static/img/9H.png"
            },
            "value": "9",
            "suit": "HEARTS"
        },
        {
            "code": "KC",
            "image": "https://deckofcardsapi.com/static/img/KC.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/KC.svg",
                "png": "https://deckofcardsapi.com/static/img/KC.png"
            },
            "value": "KING",
            "suit": "CLUBS"
        },
        {
            "code": "4H",
            "image": "https://deckofcardsapi.com/static/img/4H.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/4H.svg",
                "png": "https://deckofcardsapi.com/static/img/4H.png"
            },
            "value": "4",
            "suit": "HEARTS"
        },
        {
            "code": "5S",
            "image": "https://deckofcardsapi.com/static/img/5S.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/5S.svg",
                "png": "https://deckofcardsapi.com/static/img/5S.png"
            },
            "value": "5",
            "suit": "SPADES"
        },
        {
            "code": "2D",
            "image": "https://deckofcardsapi.com/static/img/2D.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/2D.svg",
                "png": "https://deckofcardsapi.com/static/img/2D.png"
            },
            "value": "2",
            "suit": "DIAMONDS"
        },
        {
            "code": "0H",
            "image": "https://deckofcardsapi.com/static/img/0H.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/0H.svg",
                "png": "https://deckofcardsapi.com/static/img/0H.png"
            },
            "value": "10",
            "suit": "HEARTS"
        },
        {
            "code": "9C",
            "image": "https://deckofcardsapi.com/static/img/9C.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/9C.svg",
                "png": "https://deckofcardsapi.com/static/img/9C.png"
            },
            "value": "9",
            "suit": "CLUBS"
        },
        {
            "code": "4C",
            "image": "https://deckofcardsapi.com/static/img/4C.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/4C.svg",
                "png": "https://deckofcardsapi.com/static/img/4C.png"
            },
            "value": "4",
            "suit": "CLUBS"
        },
        {
            "code": "7H",
            "image": "https://deckofcardsapi.com/static/img/7H.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/7H.svg",
                "png": "https://deckofcardsapi.com/static/img/7H.png"
            },
            "value": "7",
            "suit": "HEARTS"
        },
        {
            "code": "QH",
            "image": "https://deckofcardsapi.com/static/img/QH.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/QH.svg",
                "png": "https://deckofcardsapi.com/static/img/QH.png"
            },
            "value": "QUEEN",
            "suit": "HEARTS"
        },
        {
            "code": "8C",
            "image": "https://deckofcardsapi.com/static/img/8C.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/8C.svg",
                "png": "https://deckofcardsapi.com/static/img/8C.png"
            },
            "value": "8",
            "suit": "CLUBS"
        },
        {
            "code": "QD",
            "image": "https://deckofcardsapi.com/static/img/QD.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/QD.svg",
                "png": "https://deckofcardsapi.com/static/img/QD.png"
            },
            "value": "QUEEN",
            "suit": "DIAMONDS"
        },
        {
            "code": "0D",
            "image": "https://deckofcardsapi.com/static/img/0D.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/0D.svg",
                "png": "https://deckofcardsapi.com/static/img/0D.png"
            },
            "value": "10",
            "suit": "DIAMONDS"
        },
        {
            "code": "6H",
            "image": "https://deckofcardsapi.com/static/img/6H.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/6H.svg",
                "png": "https://deckofcardsapi.com/static/img/6H.png"
            },
            "value": "6",
            "suit": "HEARTS"
        },
        {
            "code": "JS",
            "image": "https://deckofcardsapi.com/static/img/JS.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/JS.svg",
                "png": "https://deckofcardsapi.com/static/img/JS.png"
            },
            "value": "JACK",
            "suit": "SPADES"
        },
        {
            "code": "7C",
            "image": "https://deckofcardsapi.com/static/img/7C.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/7C.svg",
                "png": "https://deckofcardsapi.com/static/img/7C.png"
            },
            "value": "7",
            "suit": "CLUBS"
        },
        {
            "code": "3C",
            "image": "https://deckofcardsapi.com/static/img/3C.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/3C.svg",
                "png": "https://deckofcardsapi.com/static/img/3C.png"
            },
            "value": "3",
            "suit": "CLUBS"
        },
        {
            "code": "6D",
            "image": "https://deckofcardsapi.com/static/img/6D.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/6D.svg",
                "png": "https://deckofcardsapi.com/static/img/6D.png"
            },
            "value": "6",
            "suit": "DIAMONDS"
        },
        {
            "code": "QC",
            "image": "https://deckofcardsapi.com/static/img/QC.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/QC.svg",
                "png": "https://deckofcardsapi.com/static/img/QC.png"
            },
            "value": "QUEEN",
            "suit": "CLUBS"
        },
        {
            "code": "3H",
            "image": "https://deckofcardsapi.com/static/img/3H.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/3H.svg",
                "png": "https://deckofcardsapi.com/static/img/3H.png"
            },
            "value": "3",
            "suit": "HEARTS"
        },
        {
            "code": "3D",
            "image": "https://deckofcardsapi.com/static/img/3D.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/3D.svg",
                "png": "https://deckofcardsapi.com/static/img/3D.png"
            },
            "value": "3",
            "suit": "DIAMONDS"
        },
        {
            "code": "JC",
            "image": "https://deckofcardsapi.com/static/img/JC.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/JC.svg",
                "png": "https://deckofcardsapi.com/static/img/JC.png"
            },
            "value": "JACK",
            "suit": "CLUBS"
        },
        {
            "code": "6C",
            "image": "https://deckofcardsapi.com/static/img/6C.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/6C.svg",
                "png": "https://deckofcardsapi.com/static/img/6C.png"
            },
            "value": "6",
            "suit": "CLUBS"
        },
        {
            "code": "AC",
            "image": "https://deckofcardsapi.com/static/img/AC.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/AC.svg",
                "png": "https://deckofcardsapi.com/static/img/AC.png"
            },
            "value": "ACE",
            "suit": "CLUBS"
        },
        {
            "code": "QS",
            "image": "https://deckofcardsapi.com/static/img/QS.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/QS.svg",
                "png": "https://deckofcardsapi.com/static/img/QS.png"
            },
            "value": "QUEEN",
            "suit": "SPADES"
        },
        {
            "code": "7D",
            "image": "https://deckofcardsapi.com/static/img/7D.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/7D.svg",
                "png": "https://deckofcardsapi.com/static/img/7D.png"
            },
            "value": "7",
            "suit": "DIAMONDS"
        },
        {
            "code": "8D",
            "image": "https://deckofcardsapi.com/static/img/8D.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/8D.svg",
                "png": "https://deckofcardsapi.com/static/img/8D.png"
            },
            "value": "8",
            "suit": "DIAMONDS"
        },
        {
            "code": "2S",
            "image": "https://deckofcardsapi.com/static/img/2S.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/2S.svg",
                "png": "https://deckofcardsapi.com/static/img/2S.png"
            },
            "value": "2",
            "suit": "SPADES"
        },
        {
            "code": "AD",
            "image": "https://deckofcardsapi.com/static/img/aceDiamonds.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/aceDiamonds.svg",
                "png": "https://deckofcardsapi.com/static/img/aceDiamonds.png"
            },
            "value": "ACE",
            "suit": "DIAMONDS"
        },
        {
            "code": "2C",
            "image": "https://deckofcardsapi.com/static/img/2C.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/2C.svg",
                "png": "https://deckofcardsapi.com/static/img/2C.png"
            },
            "value": "2",
            "suit": "CLUBS"
        },
        {
            "code": "5C",
            "image": "https://deckofcardsapi.com/static/img/5C.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/5C.svg",
                "png": "https://deckofcardsapi.com/static/img/5C.png"
            },
            "value": "5",
            "suit": "CLUBS"
        },
        {
            "code": "4D",
            "image": "https://deckofcardsapi.com/static/img/4D.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/4D.svg",
                "png": "https://deckofcardsapi.com/static/img/4D.png"
            },
            "value": "4",
            "suit": "DIAMONDS"
        },
        {
            "code": "4S",
            "image": "https://deckofcardsapi.com/static/img/4S.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/4S.svg",
                "png": "https://deckofcardsapi.com/static/img/4S.png"
            },
            "value": "4",
            "suit": "SPADES"
        },
        {
            "code": "JH",
            "image": "https://deckofcardsapi.com/static/img/JH.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/JH.svg",
                "png": "https://deckofcardsapi.com/static/img/JH.png"
            },
            "value": "JACK",
            "suit": "HEARTS"
        },
        {
            "code": "AS",
            "image": "https://deckofcardsapi.com/static/img/AS.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/AS.svg",
                "png": "https://deckofcardsapi.com/static/img/AS.png"
            },
            "value": "ACE",
            "suit": "SPADES"
        },
        {
            "code": "7S",
            "image": "https://deckofcardsapi.com/static/img/7S.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/7S.svg",
                "png": "https://deckofcardsapi.com/static/img/7S.png"
            },
            "value": "7",
            "suit": "SPADES"
        },
        {
            "code": "6S",
            "image": "https://deckofcardsapi.com/static/img/6S.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/6S.svg",
                "png": "https://deckofcardsapi.com/static/img/6S.png"
            },
            "value": "6",
            "suit": "SPADES"
        },
        {
            "code": "8S",
            "image": "https://deckofcardsapi.com/static/img/8S.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/8S.svg",
                "png": "https://deckofcardsapi.com/static/img/8S.png"
            },
            "value": "8",
            "suit": "SPADES"
        },
        {
            "code": "8H",
            "image": "https://deckofcardsapi.com/static/img/8H.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/8H.svg",
                "png": "https://deckofcardsapi.com/static/img/8H.png"
            },
            "value": "8",
            "suit": "HEARTS"
        },
        {
            "code": "5D",
            "image": "https://deckofcardsapi.com/static/img/5D.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/5D.svg",
                "png": "https://deckofcardsapi.com/static/img/5D.png"
            },
            "value": "5",
            "suit": "DIAMONDS"
        },
        {
            "code": "3S",
            "image": "https://deckofcardsapi.com/static/img/3S.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/3S.svg",
                "png": "https://deckofcardsapi.com/static/img/3S.png"
            },
            "value": "3",
            "suit": "SPADES"
        }
    ],
    "remaining": 0,
    "shuffled": true
}
"""
)

players = ["player1", "player2", "player3"]

player1_pile = json.loads(
"""
{
    "success": true,
    "deck_id": "9hw727op8fe7",
    "remaining": 0,
    "piles": {
        "player1": {
            "remaining": 18,
            "cards": [
                {
                    "code": "0C",
                    "image": "https://deckofcardsapi.com/static/img/0C.png",
                    "images": {
                        "svg": "https://deckofcardsapi.com/static/img/0C.svg",
                        "png": "https://deckofcardsapi.com/static/img/0C.png"
                    },
                    "value": "10",
                    "suit": "CLUBS"
                },
                {
                    "code": "KS",
                    "image": "https://deckofcardsapi.com/static/img/KS.png",
                    "images": {
                        "svg": "https://deckofcardsapi.com/static/img/KS.svg",
                        "png": "https://deckofcardsapi.com/static/img/KS.png"
                    },
                    "value": "KING",
                    "suit": "SPADES"
                },
                {
                    "code": "5H",
                    "image": "https://deckofcardsapi.com/static/img/5H.png",
                    "images": {
                        "svg": "https://deckofcardsapi.com/static/img/5H.svg",
                        "png": "https://deckofcardsapi.com/static/img/5H.png"
                    },
                    "value": "5",
                    "suit": "HEARTS"
                },
                {
                    "code": "KD",
                    "image": "https://deckofcardsapi.com/static/img/KD.png",
                    "images": {
                        "svg": "https://deckofcardsapi.com/static/img/KD.svg",
                        "png": "https://deckofcardsapi.com/static/img/KD.png"
                    },
                    "value": "KING",
                    "suit": "DIAMONDS"
                },
                {
                    "code": "KC",
                    "image": "https://deckofcardsapi.com/static/img/KC.png",
                    "images": {
                        "svg": "https://deckofcardsapi.com/static/img/KC.svg",
                        "png": "https://deckofcardsapi.com/static/img/KC.png"
                    },
                    "value": "KING",
                    "suit": "CLUBS"
                },
                {
                    "code": "2D",
                    "image": "https://deckofcardsapi.com/static/img/2D.png",
                    "images": {
                        "svg": "https://deckofcardsapi.com/static/img/2D.svg",
                        "png": "https://deckofcardsapi.com/static/img/2D.png"
                    },
                    "value": "2",
                    "suit": "DIAMONDS"
                },
                {
                    "code": "4C",
                    "image": "https://deckofcardsapi.com/static/img/4C.png",
                    "images": {
                        "svg": "https://deckofcardsapi.com/static/img/4C.svg",
                        "png": "https://deckofcardsapi.com/static/img/4C.png"
                    },
                    "value": "4",
                    "suit": "CLUBS"
                },
                {
                    "code": "8C",
                    "image": "https://deckofcardsapi.com/static/img/8C.png",
                    "images": {
                        "svg": "https://deckofcardsapi.com/static/img/8C.svg",
                        "png": "https://deckofcardsapi.com/static/img/8C.png"
                    },
                    "value": "8",
                    "suit": "CLUBS"
                },
                {
                    "code": "6H",
                    "image": "https://deckofcardsapi.com/static/img/6H.png",
                    "images": {
                        "svg": "https://deckofcardsapi.com/static/img/6H.svg",
                        "png": "https://deckofcardsapi.com/static/img/6H.png"
                    },
                    "value": "6",
                    "suit": "HEARTS"
                },
                {
                    "code": "3C",
                    "image": "https://deckofcardsapi.com/static/img/3C.png",
                    "images": {
                        "svg": "https://deckofcardsapi.com/static/img/3C.svg",
                        "png": "https://deckofcardsapi.com/static/img/3C.png"
                    },
                    "value": "3",
                    "suit": "CLUBS"
                },
                {
                    "code": "3H",
                    "image": "https://deckofcardsapi.com/static/img/3H.png",
                    "images": {
                        "svg": "https://deckofcardsapi.com/static/img/3H.svg",
                        "png": "https://deckofcardsapi.com/static/img/3H.png"
                    },
                    "value": "3",
                    "suit": "HEARTS"
                },
                {
                    "code": "6C",
                    "image": "https://deckofcardsapi.com/static/img/6C.png",
                    "images": {
                        "svg": "https://deckofcardsapi.com/static/img/6C.svg",
                        "png": "https://deckofcardsapi.com/static/img/6C.png"
                    },
                    "value": "6",
                    "suit": "CLUBS"
                },
                {
                    "code": "7D",
                    "image": "https://deckofcardsapi.com/static/img/7D.png",
                    "images": {
                        "svg": "https://deckofcardsapi.com/static/img/7D.svg",
                        "png": "https://deckofcardsapi.com/static/img/7D.png"
                    },
                    "value": "7",
                    "suit": "DIAMONDS"
                },
                {
                    "code": "AD",
                    "image": "https://deckofcardsapi.com/static/img/aceDiamonds.png",
                    "images": {
                        "svg": "https://deckofcardsapi.com/static/img/aceDiamonds.svg",
                        "png": "https://deckofcardsapi.com/static/img/aceDiamonds.png"
                    },
                    "value": "ACE",
                    "suit": "DIAMONDS"
                },
                {
                    "code": "4D",
                    "image": "https://deckofcardsapi.com/static/img/4D.png",
                    "images": {
                        "svg": "https://deckofcardsapi.com/static/img/4D.svg",
                        "png": "https://deckofcardsapi.com/static/img/4D.png"
                    },
                    "value": "4",
                    "suit": "DIAMONDS"
                },
                {
                    "code": "8S",
                    "image": "https://deckofcardsapi.com/static/img/8S.png",
                    "images": {
                        "svg": "https://deckofcardsapi.com/static/img/8S.svg",
                        "png": "https://deckofcardsapi.com/static/img/8S.png"
                    },
                    "value": "8",
                    "suit": "SPADES"
                },
                {
                    "code": "3S",
                    "image": "https://deckofcardsapi.com/static/img/3S.png",
                    "images": {
                        "svg": "https://deckofcardsapi.com/static/img/3S.svg",
                        "png": "https://deckofcardsapi.com/static/img/3S.png"
                    },
                    "value": "3",
                    "suit": "SPADES"
                },
                {
                    "code": "AS",
                    "image": "https://deckofcardsapi.com/static/img/AS.png",
                    "images": {
                        "svg": "https://deckofcardsapi.com/static/img/AS.svg",
                        "png": "https://deckofcardsapi.com/static/img/AS.png"
                    },
                    "value": "ACE",
                    "suit": "SPADES"
                }
            ]
        },
        "player2": {
            "remaining": 17
        },
        "player3": {
            "remaining": 17
        }
    }
}
"""
)

player2_pile = json.loads(
"""
{
    "success": true,
    "deck_id": "9hw727op8fe7",
    "cards": [
        {
            "code": "0C",
            "image": "https://deckofcardsapi.com/static/img/0C.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/0C.svg",
                "png": "https://deckofcardsapi.com/static/img/0C.png"
            },
            "value": "10",
            "suit": "CLUBS"
        },
        {
            "code": "2H",
            "image": "https://deckofcardsapi.com/static/img/2H.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/2H.svg",
                "png": "https://deckofcardsapi.com/static/img/2H.png"
            },
            "value": "2",
            "suit": "HEARTS"
        },
        {
            "code": "KH",
            "image": "https://deckofcardsapi.com/static/img/KH.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/KH.svg",
                "png": "https://deckofcardsapi.com/static/img/KH.png"
            },
            "value": "KING",
            "suit": "HEARTS"
        },
        {
            "code": "KS",
            "image": "https://deckofcardsapi.com/static/img/KS.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/KS.svg",
                "png": "https://deckofcardsapi.com/static/img/KS.png"
            },
            "value": "KING",
            "suit": "SPADES"
        },
        {
            "code": "9D",
            "image": "https://deckofcardsapi.com/static/img/9D.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/9D.svg",
                "png": "https://deckofcardsapi.com/static/img/9D.png"
            },
            "value": "9",
            "suit": "DIAMONDS"
        },
        {
            "code": "JD",
            "image": "https://deckofcardsapi.com/static/img/JD.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/JD.svg",
                "png": "https://deckofcardsapi.com/static/img/JD.png"
            },
            "value": "JACK",
            "suit": "DIAMONDS"
        },
        {
            "code": "5H",
            "image": "https://deckofcardsapi.com/static/img/5H.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/5H.svg",
                "png": "https://deckofcardsapi.com/static/img/5H.png"
            },
            "value": "5",
            "suit": "HEARTS"
        },
        {
            "code": "AH",
            "image": "https://deckofcardsapi.com/static/img/AH.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/AH.svg",
                "png": "https://deckofcardsapi.com/static/img/AH.png"
            },
            "value": "ACE",
            "suit": "HEARTS"
        },
        {
            "code": "0S",
            "image": "https://deckofcardsapi.com/static/img/0S.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/0S.svg",
                "png": "https://deckofcardsapi.com/static/img/0S.png"
            },
            "value": "10",
            "suit": "SPADES"
        },
        {
            "code": "KD",
            "image": "https://deckofcardsapi.com/static/img/KD.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/KD.svg",
                "png": "https://deckofcardsapi.com/static/img/KD.png"
            },
            "value": "KING",
            "suit": "DIAMONDS"
        },
        {
            "code": "9S",
            "image": "https://deckofcardsapi.com/static/img/9S.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/9S.svg",
                "png": "https://deckofcardsapi.com/static/img/9S.png"
            },
            "value": "9",
            "suit": "SPADES"
        },
        {
            "code": "9H",
            "image": "https://deckofcardsapi.com/static/img/9H.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/9H.svg",
                "png": "https://deckofcardsapi.com/static/img/9H.png"
            },
            "value": "9",
            "suit": "HEARTS"
        },
        {
            "code": "KC",
            "image": "https://deckofcardsapi.com/static/img/KC.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/KC.svg",
                "png": "https://deckofcardsapi.com/static/img/KC.png"
            },
            "value": "KING",
            "suit": "CLUBS"
        },
        {
            "code": "4H",
            "image": "https://deckofcardsapi.com/static/img/4H.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/4H.svg",
                "png": "https://deckofcardsapi.com/static/img/4H.png"
            },
            "value": "4",
            "suit": "HEARTS"
        },
        {
            "code": "5S",
            "image": "https://deckofcardsapi.com/static/img/5S.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/5S.svg",
                "png": "https://deckofcardsapi.com/static/img/5S.png"
            },
            "value": "5",
            "suit": "SPADES"
        },
        {
            "code": "2D",
            "image": "https://deckofcardsapi.com/static/img/2D.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/2D.svg",
                "png": "https://deckofcardsapi.com/static/img/2D.png"
            },
            "value": "2",
            "suit": "DIAMONDS"
        },
        {
            "code": "0H",
            "image": "https://deckofcardsapi.com/static/img/0H.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/0H.svg",
                "png": "https://deckofcardsapi.com/static/img/0H.png"
            },
            "value": "10",
            "suit": "HEARTS"
        },
        {
            "code": "9C",
            "image": "https://deckofcardsapi.com/static/img/9C.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/9C.svg",
                "png": "https://deckofcardsapi.com/static/img/9C.png"
            },
            "value": "9",
            "suit": "CLUBS"
        },
        {
            "code": "4C",
            "image": "https://deckofcardsapi.com/static/img/4C.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/4C.svg",
                "png": "https://deckofcardsapi.com/static/img/4C.png"
            },
            "value": "4",
            "suit": "CLUBS"
        },
        {
            "code": "7H",
            "image": "https://deckofcardsapi.com/static/img/7H.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/7H.svg",
                "png": "https://deckofcardsapi.com/static/img/7H.png"
            },
            "value": "7",
            "suit": "HEARTS"
        },
        {
            "code": "QH",
            "image": "https://deckofcardsapi.com/static/img/QH.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/QH.svg",
                "png": "https://deckofcardsapi.com/static/img/QH.png"
            },
            "value": "QUEEN",
            "suit": "HEARTS"
        },
        {
            "code": "8C",
            "image": "https://deckofcardsapi.com/static/img/8C.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/8C.svg",
                "png": "https://deckofcardsapi.com/static/img/8C.png"
            },
            "value": "8",
            "suit": "CLUBS"
        },
        {
            "code": "QD",
            "image": "https://deckofcardsapi.com/static/img/QD.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/QD.svg",
                "png": "https://deckofcardsapi.com/static/img/QD.png"
            },
            "value": "QUEEN",
            "suit": "DIAMONDS"
        },
        {
            "code": "0D",
            "image": "https://deckofcardsapi.com/static/img/0D.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/0D.svg",
                "png": "https://deckofcardsapi.com/static/img/0D.png"
            },
            "value": "10",
            "suit": "DIAMONDS"
        },
        {
            "code": "6H",
            "image": "https://deckofcardsapi.com/static/img/6H.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/6H.svg",
                "png": "https://deckofcardsapi.com/static/img/6H.png"
            },
            "value": "6",
            "suit": "HEARTS"
        },
        {
            "code": "JS",
            "image": "https://deckofcardsapi.com/static/img/JS.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/JS.svg",
                "png": "https://deckofcardsapi.com/static/img/JS.png"
            },
            "value": "JACK",
            "suit": "SPADES"
        },
        {
            "code": "7C",
            "image": "https://deckofcardsapi.com/static/img/7C.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/7C.svg",
                "png": "https://deckofcardsapi.com/static/img/7C.png"
            },
            "value": "7",
            "suit": "CLUBS"
        },
        {
            "code": "3C",
            "image": "https://deckofcardsapi.com/static/img/3C.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/3C.svg",
                "png": "https://deckofcardsapi.com/static/img/3C.png"
            },
            "value": "3",
            "suit": "CLUBS"
        },
        {
            "code": "6D",
            "image": "https://deckofcardsapi.com/static/img/6D.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/6D.svg",
                "png": "https://deckofcardsapi.com/static/img/6D.png"
            },
            "value": "6",
            "suit": "DIAMONDS"
        },
        {
            "code": "QC",
            "image": "https://deckofcardsapi.com/static/img/QC.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/QC.svg",
                "png": "https://deckofcardsapi.com/static/img/QC.png"
            },
            "value": "QUEEN",
            "suit": "CLUBS"
        },
        {
            "code": "3H",
            "image": "https://deckofcardsapi.com/static/img/3H.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/3H.svg",
                "png": "https://deckofcardsapi.com/static/img/3H.png"
            },
            "value": "3",
            "suit": "HEARTS"
        },
        {
            "code": "3D",
            "image": "https://deckofcardsapi.com/static/img/3D.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/3D.svg",
                "png": "https://deckofcardsapi.com/static/img/3D.png"
            },
            "value": "3",
            "suit": "DIAMONDS"
        },
        {
            "code": "JC",
            "image": "https://deckofcardsapi.com/static/img/JC.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/JC.svg",
                "png": "https://deckofcardsapi.com/static/img/JC.png"
            },
            "value": "JACK",
            "suit": "CLUBS"
        },
        {
            "code": "6C",
            "image": "https://deckofcardsapi.com/static/img/6C.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/6C.svg",
                "png": "https://deckofcardsapi.com/static/img/6C.png"
            },
            "value": "6",
            "suit": "CLUBS"
        },
        {
            "code": "AC",
            "image": "https://deckofcardsapi.com/static/img/AC.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/AC.svg",
                "png": "https://deckofcardsapi.com/static/img/AC.png"
            },
            "value": "ACE",
            "suit": "CLUBS"
        },
        {
            "code": "QS",
            "image": "https://deckofcardsapi.com/static/img/QS.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/QS.svg",
                "png": "https://deckofcardsapi.com/static/img/QS.png"
            },
            "value": "QUEEN",
            "suit": "SPADES"
        },
        {
            "code": "7D",
            "image": "https://deckofcardsapi.com/static/img/7D.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/7D.svg",
                "png": "https://deckofcardsapi.com/static/img/7D.png"
            },
            "value": "7",
            "suit": "DIAMONDS"
        },
        {
            "code": "8D",
            "image": "https://deckofcardsapi.com/static/img/8D.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/8D.svg",
                "png": "https://deckofcardsapi.com/static/img/8D.png"
            },
            "value": "8",
            "suit": "DIAMONDS"
        },
        {
            "code": "2S",
            "image": "https://deckofcardsapi.com/static/img/2S.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/2S.svg",
                "png": "https://deckofcardsapi.com/static/img/2S.png"
            },
            "value": "2",
            "suit": "SPADES"
        },
        {
            "code": "AD",
            "image": "https://deckofcardsapi.com/static/img/aceDiamonds.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/aceDiamonds.svg",
                "png": "https://deckofcardsapi.com/static/img/aceDiamonds.png"
            },
            "value": "ACE",
            "suit": "DIAMONDS"
        },
        {
            "code": "2C",
            "image": "https://deckofcardsapi.com/static/img/2C.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/2C.svg",
                "png": "https://deckofcardsapi.com/static/img/2C.png"
            },
            "value": "2",
            "suit": "CLUBS"
        },
        {
            "code": "5C",
            "image": "https://deckofcardsapi.com/static/img/5C.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/5C.svg",
                "png": "https://deckofcardsapi.com/static/img/5C.png"
            },
            "value": "5",
            "suit": "CLUBS"
        },
        {
            "code": "4D",
            "image": "https://deckofcardsapi.com/static/img/4D.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/4D.svg",
                "png": "https://deckofcardsapi.com/static/img/4D.png"
            },
            "value": "4",
            "suit": "DIAMONDS"
        },
        {
            "code": "4S",
            "image": "https://deckofcardsapi.com/static/img/4S.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/4S.svg",
                "png": "https://deckofcardsapi.com/static/img/4S.png"
            },
            "value": "4",
            "suit": "SPADES"
        },
        {
            "code": "JH",
            "image": "https://deckofcardsapi.com/static/img/JH.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/JH.svg",
                "png": "https://deckofcardsapi.com/static/img/JH.png"
            },
            "value": "JACK",
            "suit": "HEARTS"
        },
        {
            "code": "AS",
            "image": "https://deckofcardsapi.com/static/img/AS.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/AS.svg",
                "png": "https://deckofcardsapi.com/static/img/AS.png"
            },
            "value": "ACE",
            "suit": "SPADES"
        },
        {
            "code": "7S",
            "image": "https://deckofcardsapi.com/static/img/7S.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/7S.svg",
                "png": "https://deckofcardsapi.com/static/img/7S.png"
            },
            "value": "7",
            "suit": "SPADES"
        },
        {
            "code": "6S",
            "image": "https://deckofcardsapi.com/static/img/6S.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/6S.svg",
                "png": "https://deckofcardsapi.com/static/img/6S.png"
            },
            "value": "6",
            "suit": "SPADES"
        },
        {
            "code": "8S",
            "image": "https://deckofcardsapi.com/static/img/8S.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/8S.svg",
                "png": "https://deckofcardsapi.com/static/img/8S.png"
            },
            "value": "8",
            "suit": "SPADES"
        },
        {
            "code": "8H",
            "image": "https://deckofcardsapi.com/static/img/8H.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/8H.svg",
                "png": "https://deckofcardsapi.com/static/img/8H.png"
            },
            "value": "8",
            "suit": "HEARTS"
        },
        {
            "code": "5D",
            "image": "https://deckofcardsapi.com/static/img/5D.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/5D.svg",
                "png": "https://deckofcardsapi.com/static/img/5D.png"
            },
            "value": "5",
            "suit": "DIAMONDS"
        },
        {
            "code": "3S",
            "image": "https://deckofcardsapi.com/static/img/3S.png",
            "images": {
                "svg": "https://deckofcardsapi.com/static/img/3S.svg",
                "png": "https://deckofcardsapi.com/static/img/3S.png"
            },
            "value": "3",
            "suit": "SPADES"
        }
    ],
    "remaining": 0
}
"""
)

player3_pile = json.loads(
"""
{
    "success": true,
    "deck_id": "9hw727op8fe7",
    "remaining": 0,
    "piles": {
        "player1": {
            "remaining": 18
        },
        "player2": {
            "remaining": 17
        },
        "player3": {
            "remaining": 17,
            "cards": [
                {
                    "code": "KH",
                    "image": "https://deckofcardsapi.com/static/img/KH.png",
                    "images": {
                        "svg": "https://deckofcardsapi.com/static/img/KH.svg",
                        "png": "https://deckofcardsapi.com/static/img/KH.png"
                    },
                    "value": "KING",
                    "suit": "HEARTS"
                },
                {
                    "code": "JD",
                    "image": "https://deckofcardsapi.com/static/img/JD.png",
                    "images": {
                        "svg": "https://deckofcardsapi.com/static/img/JD.svg",
                        "png": "https://deckofcardsapi.com/static/img/JD.png"
                    },
                    "value": "JACK",
                    "suit": "DIAMONDS"
                },
                {
                    "code": "0S",
                    "image": "https://deckofcardsapi.com/static/img/0S.png",
                    "images": {
                        "svg": "https://deckofcardsapi.com/static/img/0S.svg",
                        "png": "https://deckofcardsapi.com/static/img/0S.png"
                    },
                    "value": "10",
                    "suit": "SPADES"
                },
                {
                    "code": "9H",
                    "image": "https://deckofcardsapi.com/static/img/9H.png",
                    "images": {
                        "svg": "https://deckofcardsapi.com/static/img/9H.svg",
                        "png": "https://deckofcardsapi.com/static/img/9H.png"
                    },
                    "value": "9",
                    "suit": "HEARTS"
                },
                {
                    "code": "5S",
                    "image": "https://deckofcardsapi.com/static/img/5S.png",
                    "images": {
                        "svg": "https://deckofcardsapi.com/static/img/5S.svg",
                        "png": "https://deckofcardsapi.com/static/img/5S.png"
                    },
                    "value": "5",
                    "suit": "SPADES"
                },
                {
                    "code": "9C",
                    "image": "https://deckofcardsapi.com/static/img/9C.png",
                    "images": {
                        "svg": "https://deckofcardsapi.com/static/img/9C.svg",
                        "png": "https://deckofcardsapi.com/static/img/9C.png"
                    },
                    "value": "9",
                    "suit": "CLUBS"
                },
                {
                    "code": "QH",
                    "image": "https://deckofcardsapi.com/static/img/QH.png",
                    "images": {
                        "svg": "https://deckofcardsapi.com/static/img/QH.svg",
                        "png": "https://deckofcardsapi.com/static/img/QH.png"
                    },
                    "value": "QUEEN",
                    "suit": "HEARTS"
                },
                {
                    "code": "0D",
                    "image": "https://deckofcardsapi.com/static/img/0D.png",
                    "images": {
                        "svg": "https://deckofcardsapi.com/static/img/0D.svg",
                        "png": "https://deckofcardsapi.com/static/img/0D.png"
                    },
                    "value": "10",
                    "suit": "DIAMONDS"
                },
                {
                    "code": "7C",
                    "image": "https://deckofcardsapi.com/static/img/7C.png",
                    "images": {
                        "svg": "https://deckofcardsapi.com/static/img/7C.svg",
                        "png": "https://deckofcardsapi.com/static/img/7C.png"
                    },
                    "value": "7",
                    "suit": "CLUBS"
                },
                {
                    "code": "QC",
                    "image": "https://deckofcardsapi.com/static/img/QC.png",
                    "images": {
                        "svg": "https://deckofcardsapi.com/static/img/QC.svg",
                        "png": "https://deckofcardsapi.com/static/img/QC.png"
                    },
                    "value": "QUEEN",
                    "suit": "CLUBS"
                },
                {
                    "code": "JC",
                    "image": "https://deckofcardsapi.com/static/img/JC.png",
                    "images": {
                        "svg": "https://deckofcardsapi.com/static/img/JC.svg",
                        "png": "https://deckofcardsapi.com/static/img/JC.png"
                    },
                    "value": "JACK",
                    "suit": "CLUBS"
                },
                {
                    "code": "QS",
                    "image": "https://deckofcardsapi.com/static/img/QS.png",
                    "images": {
                        "svg": "https://deckofcardsapi.com/static/img/QS.svg",
                        "png": "https://deckofcardsapi.com/static/img/QS.png"
                    },
                    "value": "QUEEN",
                    "suit": "SPADES"
                },
                {
                    "code": "2S",
                    "image": "https://deckofcardsapi.com/static/img/2S.png",
                    "images": {
                        "svg": "https://deckofcardsapi.com/static/img/2S.svg",
                        "png": "https://deckofcardsapi.com/static/img/2S.png"
                    },
                    "value": "2",
                    "suit": "SPADES"
                },
                {
                    "code": "5C",
                    "image": "https://deckofcardsapi.com/static/img/5C.png",
                    "images": {
                        "svg": "https://deckofcardsapi.com/static/img/5C.svg",
                        "png": "https://deckofcardsapi.com/static/img/5C.png"
                    },
                    "value": "5",
                    "suit": "CLUBS"
                },
                {
                    "code": "JH",
                    "image": "https://deckofcardsapi.com/static/img/JH.png",
                    "images": {
                        "svg": "https://deckofcardsapi.com/static/img/JH.svg",
                        "png": "https://deckofcardsapi.com/static/img/JH.png"
                    },
                    "value": "JACK",
                    "suit": "HEARTS"
                },
                {
                    "code": "6S",
                    "image": "https://deckofcardsapi.com/static/img/6S.png",
                    "images": {
                        "svg": "https://deckofcardsapi.com/static/img/6S.svg",
                        "png": "https://deckofcardsapi.com/static/img/6S.png"
                    },
                    "value": "6",
                    "suit": "SPADES"
                },
                {
                    "code": "5D",
                    "image": "https://deckofcardsapi.com/static/img/5D.png",
                    "images": {
                        "svg": "https://deckofcardsapi.com/static/img/5D.svg",
                        "png": "https://deckofcardsapi.com/static/img/5D.png"
                    },
                    "value": "5",
                    "suit": "DIAMONDS"
                }
            ]
        }
    }
}
"""
)

def test_Deck_class():
    deck = game.Deck()

    assert all(key in ('deck_id', 'success', 'remaining', 'shuffled') for key in deck.deck.keys())
    assert deck.deck_id.isalnum() and len(deck.deck_id) == 12
    assert deck.shuffled == True
    assert deck.remaining == 52

    
def test_Deck_draw_from_deck_func():
    deck = game.Deck()
    num_cards = 50
    drawn_cards = deck.draw_from_deck(num_cards)

    assert re.search(r"\s", drawn_cards) == None
    assert len(re.findall(r",", drawn_cards)) == num_cards - 1
    assert len(re.findall(r"[AKQJ0-9][HSCD]+", drawn_cards)) == num_cards
    assert deck.remaining == 52 - num_cards

def test_CardPile_class():
    deck = game.Deck()
    cards = deck.draw_from_deck(5)
    pile = game.CardPile(deck.deck_id, 'my_pile', cards)

    assert all(key in ('deck_id', 'success', 'remaining', 'piles') for key in pile.pile.keys())
    assert pile.deck_id == deck.deck_id
    assert pile.name == 'my_pile'
    assert pile.remaining == 5
    assert ",".join(pile.get_card_codes_list()) == cards

def test_CardPile_add_to_pile_func():
    deck = game.Deck()
    cards = deck.draw_from_deck(5)
    pile = game.CardPile(deck.deck_id, 'my_pile', cards)
    cards_to_add = deck.draw_from_deck(2)
    pile.add_to_pile(cards_to_add)

    assert pile.remaining == 5 + 2
    assert len(pile.get_card_codes_list()) == 5 + 2
    assert ",".join(pile.get_card_codes_list()) == cards + ',' + cards_to_add
    assert deck.remaining == 52 - 7


def test_CardPile_get_card_codes_func():
    deck = game.Deck()
    pile = game.CardPile(deck.deck_id, 'my_pile', deck.draw_from_deck(5))
    card_codes = pile.get_card_codes_list()

    for card in card_codes:
        assert re.match(r"[AKQJ0-9][HSCD]", card)
    assert len(card_codes) == 5

def test_CardPile_draw_cards_from_top_of_pile():
    deck = game.Deck()
    cards = deck.draw_from_deck(5)
    pile = game.CardPile(deck.deck_id, 'my_pile', cards)
    drawn_cards = pile.draw_cards_from_top_of_pile(2)

    assert cards[-5:] == drawn_cards

def test_PilePile_class():
    deck = game.Deck()
    player_list = ['jenna', 'eddie', 'cp1', 'cp2', 'cp3']
    pile_pile = game.PilePile(deck.deck_id)
    for player in player_list:
        pile_pile.add_pile(game.CardPile(deck.deck_id, f'{player}_draw', deck.draw_from_deck(4)))
    
    for player in player_list:
        assert pile_pile.get_pile(f'{player}_draw').name == f'{player}_draw'
        
    assert len(pile_pile.get_draw_piles()) == len(player_list)



"""
def test_init_game_func():
    deck = game.Deck()
    player_list = ['jenna', 'eddie', 'cp1', 'cp2', 'cp3', 'cp4']
    pile_dict = game.init_game(deck, player_list)
    total_card_num = 0
    assert deck.remaining == 0
    for player in player_list:
        pile_name = ('{player}_draw').format(player = player)
        player_pile = pile_dict[pile_name]
        assert player_pile.name == pile_name
        assert player_pile.remaining in (8, 9)
        total_card_num += player_pile.remaining
    assert total_card_num == 52
"""


# finish building tests for PilePile

# Cleanup things to do:
    # Change all .format to f-strings
    # Use type hinting
    # document all functions
    # packing and unpacking lists
    # use list comprehensions
    # research how to use for-loops properly



"""
def test_shuffle_deck_mock():
    game.Deck.get_shuffled_deck = MagicMock(return_value=mock_deck)

    deck = game.Deck.get_shuffled_deck()

    assert len(deck["cards"]) == 52, "Deck contains 52 cards"

def test_draw_from_deck_mock():
    

    game.Deck.get_shuffled_deck = MagicMock(return_value=mock_deck)
    deckClass = game.Deck()

    # deckClass.get_shuffled_deck()

    # cards = deckClass.draw_from_deck(3)
    cards = deckClass.deck["cards"][:3]
    card_codes = [card['code'] for card in cards]
    assert ",".join(card_codes) == '0C,2H,KH'
"""


## Code to generate mocks

# for i, card in enumerate(mock_deck["cards"]):
#     url = "https://deckofcardsapi.com/api/deck/{deck_id}/pile/{pile}/add/?cards={player_card_codes}".format(
#             deck_id = mock_deck["deck_id"],
#             pile = players[i % len(players)],
#             player_card_codes = card["code"]
#         )

#     # print(url)
#     r = requests.get(url)

# for player in players:
#     r = requests.get(
#         "https://deckofcardsapi.com/api/deck/{deck_id}/pile/{pile}/list/".format(
#             deck_id = mock_deck["deck_id"],
#             pile = player
#         )
#     )
#     print(player)
#     print(r.json())
