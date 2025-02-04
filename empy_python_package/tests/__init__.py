import kaggle

print(kaggle.__version__)

from kaggle.api.kaggle_api_extended import KaggleApi

# אתחול ה-API
api = KaggleApi()
api.authenticate()

# הורדת הנתונים מתוך קאגל (החלף ב-id של המערכת)
api.dataset_download_files("brsdincer/alzheimer-features", path="your_path_here", unzip=True)
import pandas as pd

# נניח שהנתונים הם בקובץ CSV בשם "alzheimer_data.csv"
df = pd.read_csv("your_path_here/alzheimer_data.csv")


def split_age_groups(df):
    # יצירת תנאים לחלוקה לפי קבוצות גיל
    conditions = [
        (df["Age"] >= 60) & (df["Age"] <= 69),  # קבוצת גיל 60-69
        (df["Age"] >= 70) & (df["Age"] <= 79),  # קבוצת גיל 70-79
        (df["Age"] >= 80) & (df["Age"] <= 90),  # קבוצת גיל 80-90
    ]

    # יצירת רשימות עם שמות הקבוצות
    age_groups = ["60-69", "70-79", "80-90"]

    # הוספת עמודה חדשה עם קבוצת הגיל
    df["Age Group"] = pd.cut(df["Age"], bins=[60, 70, 80, 90], labels=age_groups, right=False)

    return df


# קריאה לפונקציה
df = split_age_groups(df)

# הצגת הנתונים
print(df.head())