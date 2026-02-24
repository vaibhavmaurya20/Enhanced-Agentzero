
"""
Download Link Generator
Generates direct download links for files and packages
"""

import os

from typing import Dict, Optional
from pathlib import Path
from datetime import datetime, timedelta
import hashlib
import secrets

class DownloadLinkGenerator:
    def __init__(self, base_url: str = "/downloads"):
        self.base_url = base_url
        self.token_data: Dict[str, Dict] = {}
        self.downloads_dir = Path("/a0/usr/workdir/downloads")
        self.downloads_dir.mkdir(parents=True, exist_ok=True)

    def generate_token(self, file_path: str, expires_in_hours: int = 24) -> str:
        token = secrets.token_urlsafe(32)
        expires_at = datetime.now() + timedelta(hours=expires_in_hours)
        self.token_data[token] = {
            "file_path": file_path,
            "expires_at": expires_at.isoformat(),
            "downloads": 0,
            "max_downloads": 10
        }
        return token

    def register_file_download(self, file_path: str) -> Dict[str, str]:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        file_name = os.path.basename(file_path)
        download_path = self.downloads_dir / file_name

        if str(download_path) != file_path:
            import shutil
            shutil.copy2(file_path, download_path)

        token = self.generate_token(str(download_path))
        download_url = f"{self.base_url}/{token}"

        with open(download_path, "rb") as f:
            file_hash = hashlib.sha256(f.read()).hexdigest()

        return {
            "token": token,
            "url": download_url,
            "file_name": file_name,
            "file_size": os.path.getsize(download_path),
            "sha256": file_hash
        }

_download_generator = None

def get_download_generator() -> DownloadLinkGenerator:
    global _download_generator
    if _download_generator is None:
        _download_generator = DownloadLinkGenerator()
    return _download_generator
