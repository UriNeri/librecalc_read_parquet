import sys
import tempfile

# Point this at the site-packages directory of a Python installation that has polars.
external_env_path = r"/home/neri/Documents/GitHub/rps/rolypoly/.pixi/envs/dev/lib/python3.13/site-packages"

if external_env_path not in sys.path:
    sys.path.append(external_env_path)

import polars as pl
import uno
from com.sun.star.awt.MessageBoxButtons import BUTTONS_OK
from com.sun.star.awt.MessageBoxType import ERRORBOX
from com.sun.star.ui.dialogs.TemplateDescription import FILEOPEN_SIMPLE


def _show_error(desktop, title, message):
    parent = desktop.getCurrentFrame().getContainerWindow()
    toolkit = parent.getToolkit()
    box = toolkit.createMessageBox(parent, ERRORBOX, BUTTONS_OK, title, message)
    box.execute()


def open_parquet_with_polars(*args):
    ctx = uno.getComponentContext()
    smgr = ctx.ServiceManager
    desktop = smgr.createInstanceWithContext("com.sun.star.frame.Desktop", ctx)

    file_picker = smgr.createInstanceWithContext("com.sun.star.ui.dialogs.FilePicker", ctx)
    file_picker.initialize((FILEOPEN_SIMPLE,))
    file_picker.appendFilter("Parquet Files (*.parquet)", "*.parquet")
    file_picker.setTitle("Select Parquet File to Open in Calc")

    if file_picker.execute() != 1:
        return

    selected_urls = file_picker.getFiles()
    if not selected_urls:
        return

    parquet_path = uno.fileUrlToSystemPath(selected_urls[0])

    try:
        df = pl.read_parquet(parquet_path)

        with tempfile.NamedTemporaryFile(suffix=".csv", delete=False) as tmp:
            temp_csv_path = tmp.name

        df.write_csv(temp_csv_path)
        csv_url = uno.systemPathToFileUrl(temp_csv_path)
        desktop.loadComponentFromURL(csv_url, "_blank", 0, ())
    except Exception as exc:
        _show_error(desktop, "Error Opening Parquet", str(exc))


g_exportedScripts = (open_parquet_with_polars,)
