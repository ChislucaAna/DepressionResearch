import requests
from pathlib import Path
from urllib.parse import urlparse
import pandas as pd

#https://wwwn.cdc.gov/nchs/nhanes/
#source for the nhanes datasets

# Example dataset families you want to look for
dataset_codes = ["DPQ"]

# Candidate year folders and filename styles
# Add more if you need them
year_configs = [
    {"year": "2021", "filename_template": "{code}_L.xpt"},
    {"year": "2017", "filename_template": "P_{code}.xpt"},
    {"year": "2015", "filename_template": "{code}_I.xpt"},
    {"year": "2013", "filename_template": "{code}_H.xpt"},
    {"year": "2011", "filename_template": "{code}_G.xpt"},
    {"year": "2009", "filename_template": "{code}_F.xpt"},
]

base_template = "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/{year}/DataFiles/{filename}"

download_dir = Path("nhanes_downloads")
csv_dir = Path("nhanes_csv")
download_dir.mkdir(exist_ok=True)
csv_dir.mkdir(exist_ok=True)

session = requests.Session()

found_files = []
missing_files = []

for code in dataset_codes:
    for cfg in year_configs:
        year = cfg["year"]
        filename = cfg["filename_template"].format(code=code)
        url = base_template.format(year=year, filename=filename)

        try:
            r = session.get(url, timeout=20)
            if r.status_code == 200:
                xpt_path = download_dir / f"nhanes_{year}_{Path(filename).stem}.xpt"

                with open(xpt_path, "wb") as f:
                    f.write(r.content)

                try:
                    df = pd.read_sas(xpt_path, format="xport")
                    csv_path = csv_dir / f"{xpt_path.stem}.csv"
                    df.to_csv(csv_path, index=False)

                    found_files.append(
                        {"year": year, "url": url, "xpt": str(xpt_path), "csv": str(csv_path)}
                    )
                    print(f"FOUND: {url}")
                except Exception as e:
                    found_files.append(
                        {"year": year, "url": url, "xpt": str(xpt_path), "csv": None}
                    )
                    print(f"DOWNLOADED BUT COULD NOT CONVERT: {url} | {e}")
            else:
                missing_files.append(url)
                print(f"NOT FOUND: {url}")

        except requests.RequestException as e:
            missing_files.append(url)
            print(f"ERROR: {url} | {e}")

print("\nSummary")
print(f"Found: {len(found_files)}")
print(f"Missing/Error: {len(missing_files)}")