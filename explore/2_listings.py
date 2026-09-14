# %%
import pandas as pd
from staysage import config

calendar = pd.read_csv(
    config.calendar_path("austin"),
    nrows=300_000,
    parse_dates=["date"],
    compression="gzip",
)

print(calendar.head())
print()
print("Earliest date:", calendar["date"].min())
print("Latest date: ", calendar["date"].max())
# %%
# availability
print(calendar["available"].value_counts())
# %%
# is there a pattern on the weekends?

calendar["day_name"] = calendar["date"].dt.day_name()

days_in_order = ["Monday", "Tuesday", "Wednesday", "Thursday",
                 "Friday", "Saturday", "Sunday"]

for day in days_in_order:
    # keeps rows for THIS wseekday
    this_day = calendar[calendar["day_name"] == day]
    # what fraction are not available

    is_unavailable = this_day["available"] == "f"
    percent_taken = is_unavailable.mean() * 100

    print(day, "-", round(percent_taken, 1), "% unavailable")
# %%
# the demand, month by month

calendar["month"] = calendar["date"].dt.month

for month_number in range(1, 13):
    this_month = calendar[calendar["month"] == month_number]

    if len(this_month) == 0:
        continue

    is_booked = this_month["available"] == "f"
    percent_booked = is_booked.mean() * 100

    print("Month", month_number, "-", round(percent_booked, 1), "% booked")
# %%

