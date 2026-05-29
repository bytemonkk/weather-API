from setuptools import setup

setup(
    name="weather-api-app",
    version="1.0.0",
    author="Manoj Kumar Sunkara",
    description="Real-Time Weather Application using OpenWeatherMap API",
    install_requires=[
        "streamlit",
        "requests",
        "python-dotenv"
    ],
    python_requires=">=3.10",
)