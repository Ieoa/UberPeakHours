from dotenv import load_dotenv
import os

load_dotenv()

BQ_PROJECT = os.getenv("BQ_PROJECT", "default_project")

DEFAULT_START = "2023-01-01"
DEFAULT_END = "2023-12-31"
