import pandas as pd
import datetime

def read_report(report_mt5_file):
    df = pd.read_excel( report_mt5_file, sheet_name="Sheet1", 
    names = ["Time", "Deal", "Symbol", "Type", "Direction", "Volume", "Price", 
            "Order", "Commission", "Swap", "Profit", "Balance", "Comment"])
    index_deals = df[df["Time"] == "Time"].index.values
    df_report = df[ index_deals[0]+2: len(df.index)-1 ].reset_index(drop=True)
    df_report["Time"] = pd.to_datetime(df_report["Time"].astype(str), format="%Y/%m/%d")
    df_report["Time"] = df_report["Time"] - pd.DateOffset(minutes=1) - pd.to_timedelta(df_report["Time"].dt.second, unit='S')
    return df_report

def format_report(df):
    dff = df.groupby("Direction")
    df_in = dff.get_group("in").reset_index()
    df_out = dff.get_group("out").reset_index()
    df_report_format = pd.DataFrame()  
    df_report_format["price_open_report"]  = df_in["Price"]
    df_report_format["date_open_report"]   = df_in["Time"]
    df_report_format["type_report"]        = df_in["Type"]
    df_report_format["date_close_report"]  = df_out["Time"]
    df_report_format["price_close_report"] = df_out["Price"]
    df_report_format["comment_report"]     = df_in["Comment"]
    df_report_format["swap_report"]        = df_out["Swap"]
    df_report_format["total_report"]       = df_out["Profit"]
    df_report_format["diff_report"]        = df_out["Profit"] + df_out["Swap"]  
    return df_report_format

def read_total(ma_total_file):
    return pd.read_csv( ma_total_file, usecols = range(1, 11))
                    

def drop_excess_items(df_large, df_small):
    pass

if __name__ == "__main__":
    

    report_mt5_file = "ReportTester-61123378.xlsx"
    ma_total_file = "3270_3270_totals.csv"

    df_report = format_report(read_report(report_mt5_file))
    df_total = read_total(ma_total_file)

    # df_report.to_csv("asdasda.csv")
    
    print( df_report[906:912])
    print( df_total.head())