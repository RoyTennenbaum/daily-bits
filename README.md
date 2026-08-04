# Daily Bits

> Learn something new every day!

**Daily Bits** delivers daily knowledge snippets powered by Wikipedia and Gemini AI.

---

## Prerequisites

- **Python**: `>= 3.13`
- **Package Manager**: [`uv`](https://github.com/astral-sh/uv) (recommended) or standard `pip`

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/daily-bits.git
cd daily-bits
```

### 2. Set up environment variables

Create a `.env` file in the project root to store your API keys and configuration:

```env
GEMINI_API_KEY=your_gemini_api_key_here
WIKI_USER_AGENT=DailyBits/0.1.0 (your-email@example.com)
```

### 3. Install dependencies

Using `uv`:

```bash
uv sync
```

Or using standard `pip`:

```bash
pip install -e .
```

### 4. Run the application

```bash
uv run daily-bits
```

---

## Tech Stack & Dependencies

- **[google-genai](https://pypi.org/project/google-genai/)**: Integration with Google Gemini API models.
- **[wikipedia-api](https://pypi.org/project/Wikipedia-API/)**: Python wrapper for Wikipedia data extraction.
- **[python-dotenv](https://pypi.org/project/python-dotenv/)**: Loads environment variables from `.env` files.
- **[uv](https://astral.sh/uv)**: Fast Python package installer and environment manager.

---

## License

MIT
