"""
Script to download official ARC-AGI dataset from GitHub / official repository.
Menyimpan dataset training dan evaluation ke direktori data/arc/.
"""

import os
import sys
import json
import urllib.request
import zipfile
import io

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "arc")
os.makedirs(DATA_DIR, exist_ok=True)

# URL alternatif untuk mengunduh dataset ARC resmi dari GitHub
# Menggunakan repository resmi fchollet/ARC-AGI
GITHUB_ZIP_URL = "https://github.com/fchollet/ARC-AGI/archive/refs/heads/master.zip"


def download_arc_dataset():
    print(f"[*] Mengunduh dataset ARC resmi dari: {GITHUB_ZIP_URL}")
    headers = {'User-Agent': 'Mozilla/5.0'}
    req = urllib.request.Request(GITHUB_ZIP_URL, headers=headers)
    
    try:
        with urllib.request.urlopen(req, timeout=60) as response:
            zip_content = response.read()
            print(f"[+] Download selesai ({len(zip_content) / (1024*1024):.2f} MB). Mengekstrak file...")
            
            with zipfile.ZipFile(io.BytesIO(zip_content)) as z:
                # Filter file training & evaluation
                for file_info in z.infolist():
                    if "/data/training/" in file_info.filename and file_info.filename.endswith(".json"):
                        filename = os.path.basename(file_info.filename)
                        dest_dir = os.path.join(DATA_DIR, "training")
                        os.makedirs(dest_dir, exist_ok=True)
                        dest_path = os.path.join(dest_dir, filename)
                        with open(dest_path, "wb") as f:
                            f.write(z.read(file_info.filename))
                            
                    elif "/data/evaluation/" in file_info.filename and file_info.filename.endswith(".json"):
                        filename = os.path.basename(file_info.filename)
                        dest_dir = os.path.join(DATA_DIR, "evaluation")
                        os.makedirs(dest_dir, exist_ok=True)
                        dest_path = os.path.join(dest_dir, filename)
                        with open(dest_path, "wb") as f:
                            f.write(z.read(file_info.filename))
                            
        train_count = len(os.listdir(os.path.join(DATA_DIR, "training")))
        eval_count = len(os.listdir(os.path.join(DATA_DIR, "evaluation")))
        print(f"[+] Berhasil mengekstrak {train_count} training tasks dan {eval_count} evaluation tasks ke {DATA_DIR}!")
        return True
    except Exception as e:
        print(f"[-] Gagal mengunduh ZIP: {e}")
        print("[*] Mencoba mengunduh sample task langsung...")
        return download_sample_tasks()


def download_sample_tasks():
    """Mengunduh beberapa sample task populer jika ZIP repo gagal."""
    sample_ids = [
        "007bbfb7", "00d62c1b", "017c7c7b", "025d127b", "045e512c",
        "0520fde7", "05269061", "05f2a901", "06df4c85", "08ed6ac7"
    ]
    train_dir = os.path.join(DATA_DIR, "training")
    os.makedirs(train_dir, exist_ok=True)
    
    success_count = 0
    for tid in sample_ids:
        url = f"https://raw.githubusercontent.com/fchollet/ARC-AGI/master/data/training/{tid}.json"
        dest_path = os.path.join(train_dir, f"{tid}.json")
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = resp.read()
                with open(dest_path, "wb") as f:
                    f.write(data)
            success_count += 1
        except Exception as e:
            print(f"[-] Gagal mengunduh {tid}: {e}")
            
    print(f"[+] Mengunduh {success_count} sample training tasks ke {train_dir}!")
    return success_count > 0


if __name__ == "__main__":
    download_arc_dataset()
