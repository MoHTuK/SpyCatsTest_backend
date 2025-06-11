# validators.py
import requests
from rest_framework import serializers

CAT_BREEDS_API = "https://api.thecatapi.com/v1/breeds"


class ValidBreedValidator:
    def __call__(self, value):
        try:
            response = requests.get(CAT_BREEDS_API, timeout=5)
            response.raise_for_status()
        except requests.RequestException:
            raise serializers.ValidationError("Failed to verify breed (API unavailable)")

        breeds = response.json()
        breed_names = {breed["name"].lower() for breed in breeds}

        if value.lower() not in breed_names:
            raise serializers.ValidationError(f"Breed ‘{value}’ is not found among the allowed breeds")
