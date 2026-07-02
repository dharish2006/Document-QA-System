from pathlib import Path
import shutil


def clean_uploaded_documents():
    backend_root = Path(__file__).resolve().parents[2]

    upload_folder = backend_root / "uploaded_docs"

    if upload_folder.exists():
        shutil.rmtree(upload_folder)

    upload_folder.mkdir(parents=True, exist_ok=True)