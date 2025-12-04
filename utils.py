import re
import pandas as pd

def clean_dollar_sign(price: str) -> str:
    return price[:-1]

def parse_html_items(item: str) -> str:
    return re.sub('<[^<]+?>', ' ', str(item))

# ===============================================================

# q 1:
def convert_datatypes(df):
    df["total_amount"] = df["total_amount"].astype(str)
    df["total_amount"] = df["total_amount"].apply(clean_dollar_sign)
    df["total_amount"] = df["total_amount"].astype(float)

    df["order_date"] = pd.to_datetime(df["order_date"])
    return df
# ===============================================================

# q 2:
def clean_html_col(df):
    df["items_html"] = df["items_html"].astype(str)
    df["items_html"] = df["items_html"].apply(parse_html_items)
    return df

# ===============================================================

# q 3:
def replace_coupon_used_col(df):
    df["coupon_used"] = df["coupon_used"].replace("", "no coupon")
    return df

# ===============================================================

# q 4:
def add_month_col(df):
    df["order_month"] = pd.DatetimeIndex(df['order_date']).month
    return df

# ===============================================================

# q 5:
def add_high_value_order_col_and_sort(df):
    mask = df["total_amount"] > df["total_amount"].mean()
    df["high_value_order"] = mask.values
    df = df.sort_values(by="total_amount", ascending=False)
    return df

# ===============================================================

# q 6:
def add_avg_rating_per_country(df):
    country_avg = df.groupby("country")["rating"].mean()
    country_avg_dict = country_avg.to_dict()

    df["avg_by_country"] = ""
    df["avg_by_country"] = df["country"].apply(lambda x: country_avg_dict.get(x))
    return df

# ===============================================================

# q 7:
def filtering_by_total_amount_and_rating(df):
    df = df[(df["total_amount"] > 1000) & (df["rating"] > 4.5)]
    return df

# ===============================================================

# q 8:
def adding_delivery_status_col(df):
    df['delivery_status'] = ""
    df["delivery_status"] = df["shipping_days"].apply(lambda x: "delayed" if x > 7 else "on time")
    return df

