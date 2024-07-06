# 2890 Reshape Data: Melt

import pandas as pd


def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return report.melt(
        id_vars=["product"],
        var_name="quarter",
        value_vars=["quarter_1", "quarter_2", "quarter_3", "quarter_4"],
        value_name="sales",
    )
