# librecalc_read_parquet

LibreOffice Calc Python macro for opening a Parquet file with Polars and loading it into Calc.

The macro is in [read_parquet.py](/home/neri/Documents/GitHub/librecalc_read_parquet/read_parquet.py).

Test input included in the repo root:
sequences_rdrp_motif_results.parquet

Before running it, edit `external_env_path` in [read_parquet.py](/home/neri/Documents/GitHub/librecalc_read_parquet/read_parquet.py) so it points to the `site-packages` directory of a Python installation that has `polars` installed.

Install and run:

1. clone into something like `/home/neri/.config/libreoffice/4/user/Scripts/python/read_parquet.py`
2. enable macros (`Settings`, search for `security`, and adjust if needed)
3. press `Tools` -> `Macros` -> `Python`
4. select it and press `Run`

A dialog should pop up. 