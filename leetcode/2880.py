# 2880 Select Data

import pandas as pd


def selectData(students: pd.DataFrame) -> pd.DataFrame:
    selected_id = 101
    res = students.query(f"student_id == {selected_id}")
    return res.drop(columns=["student_id"])
