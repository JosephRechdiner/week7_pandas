import pandas as pd
from utils import convert_datatypes, clean_html_col, replace_coupon_used_col, add_month_col, add_high_value_order_col_and_sort, add_avg_rating_per_country, filtering_by_total_amount_and_rating, adding_delivery_status_col

# q 0:
df = pd.read_json("orders_simple.json")

df_piped = (df
            .pipe(convert_datatypes)
            .pipe(clean_html_col)
            .pipe(replace_coupon_used_col)
            .pipe(add_month_col)
            .pipe(add_high_value_order_col_and_sort)
            .pipe(add_avg_rating_per_country)
            .pipe(filtering_by_total_amount_and_rating)
            .pipe(adding_delivery_status_col))

# q 9:
df_piped.to_csv("clean_orders_[213507742].csv")
