# FlowMake

EGR CashFLow From Prompt to Diagram

## File Structure

flowmake/
├── .git/
├── .venv/
├── src/
│ └── flowmake/
│ ├── **init**.py
│ ├── cli.py # Entry point / CLI
│ ├── prompt.py # Prompt templates (EGR cashflow prompt)
│ ├── llm.py # LLM layer (API calls, JSON parsing)
│ ├── models.py # Data models (CashFlow, Period, Amount)
│ ├── chart.py # Chart generation from parsed JSON
│ └── vision.py # Future: image-to-text-to-prompt pipeline
├── tests/
│ ├── test_llm.py
│ ├── test_chart.py
│ └── test_models.py
├── pyproject.toml
├── README.md
└── .gitignore
