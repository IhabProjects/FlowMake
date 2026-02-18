from pydantic import BaseModel, PositiveInt
from typing import float, Literal


class CashFlow(BaseModel):
    amount: Float  # The amount of the cash flow if it's negative it's an outflow, if it's positive it's an infllow
    cashflow_type: Literal[
        "P", "A", "F", ""
    ]  # The type will be either "A" for annual, "P" for present, "F" for future, "G" for gradient, "R" for Random
    start_year: PositiveInt
    end_year: PositiveInt  # could not exist for Future cashflows and for Present cashflows, it will be the same as start_year, for Random cashflows too


mock_cashflow = {"amount": 1000.0, "cashflow_type": "A", "start_year": 1, "end_year": 5}

cashwflowTest = CashFlow(**mock_cashflow)
print(cashwflowTest.amount)
print(cashwflowTest.model_dump())
