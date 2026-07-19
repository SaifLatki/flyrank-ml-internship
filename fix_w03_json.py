import json
from pathlib import Path
path = Path('work/notebooks/w03_data_contract.ipynb')
nb = json.loads(path.read_text())
source = [
    'import pandas as pd\n',
    'from pathlib import Path\n',
    '\n',
    'repo_root = Path.cwd()\n',
    'for _ in range(6):\n',
    '    candidate = repo_root / "data" / "raw" / "content_refresh_anonymized.csv"\n',
    '    if candidate.exists():\n',
    '        break\n',
    '    repo_root = repo_root.parent\n',
    'csv_path = candidate\n',
    'assert csv_path.exists(), f"data/raw/content_refresh_anonymized.csv not found from cwd={Path.cwd()}"\n',
    '\n',
    'df = pd.read_csv(csv_path)\n',
    'window_cols = [c for c in df.columns if any(w in c for w in ("_90d", "_last_30d", "_prev_30d"))]\n',
    'print("rows", len(df))\n',
    'print("unique content_id", df["content_id"].nunique())\n',
    'print("duplicate content_id", df["content_id"].duplicated().sum())\n',
    'print("unique client_id", df["client_id"].nunique())\n',
    'print("date-like columns", [c for c in df.columns if "date" in c.lower()])\n',
    'print("window columns count", len(window_cols))\n',
    'print("window columns sample", sorted(window_cols)[:20])\n',
    'print("trend field missing values", df[["trend_direction", "trend_pct"]].isna().sum().to_dict())\n',
]
nb['cells'][2]['source'] = source
path.write_text(json.dumps(nb, indent=1, ensure_ascii=False) + '\n')
print('notebook repaired')
