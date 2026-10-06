import os, sys, urllib.request

sys.stdout.reconfigure(encoding='utf-8')

DRIVE_FILES = {
    # Bai 05
    "Bai_05": {
        "05-1.mp3": "1XMSn0vZhYUcQpsm47_C0TyQ8exmbofvW",
        "05-2.mp3": "1D-4Txsl2SlFYg_oYV0K32oem5oq9CAl6",
        "05-3.mp3": "13Lc5xwkqbHQ7AMI5w02EM5nApy0t0dla",
        "05-4.mp3": "1bAXCb7mMkLYFs7APVnxaOH57OppAFfv6",
        "05-5.mp3": "1SQbYV8RbIOrwKFcAusZ22A5pxpnaFete",
    },
    # Bai 06
    "Bai_06": {
        "06-1.mp3": "1IKGUpkMFyAldytMyC_usYBaSOsjI0l-t",
        "06-2.mp3": "1EDx8DCkM3FGomWRmRSPmfud2QBp6BSJB",
        "06-3.mp3": "1N_qRJyKh0A7VgacObiTpq2t29jLb4J0q",
        "06-4.mp3": "1KaPK1vUC_iedZUOB8RskUrchtmUQ45SM",
        "06-5.mp3": "1nvxzDe6VHCuxRhX4ojsY4AxVGrJRs0v0",
    },
    # Bai 07
    "Bai_07": {
        "07-1.mp3": "11lZix-ffdTNG5SfZBnHe0AAVgaJtspp-",
        "07-2.mp3": "1zK5lsqfYnxf60iEmIJoFJYMfSBnl-96g",
        "07-3.mp3": "1HLQdbRA9gKOXtqhKPhQOry0abG0PQmTS",
        "07-4.mp3": "17kNMIdsKQqnKJ_czc95ZFlwRjxwURuLE",
        "07-5.mp3": "1_yxzG8g5WHcwZZ4zSfaoD2Qf1S6Ha8YE",
    },
    # Bai 08
    "Bai_08": {
        "08-1.mp3": "1liX_mqMnMXuCGAGmfHzF7AgNDA2KRlTB",
        "08-2.mp3": "1rgMRuk1sMzZMZDWzIGcRFnyONeZbs6Up",
        "08-3.mp3": "1Jb1VpGSSSuWgUhRUc5FZSCBMuWrThEu7",
        "08-4.mp3": "1mDyVqOVJG4F-TUFS43T_kYXbCjfjWwfH",
        "08-5.mp3": "1MPBJO095Ar_yTPB_IKXzy9TrVnTaGPnu",
    },
    # Bai 09
    "Bai_09": {
        "09-1.mp3": "1chm-1reFzyylSVgLJNk6_c5aYGuzk5NC",
        "09-2.mp3": "1vhK1duSMiitjeb9LZQkK8GJ1IyCKsM5S",
        "09-3.mp3": "1fcs2bXGRDDTK9lWJ96RYCjH78-EH3DwD",
        "09-4.mp3": "1CLQFz5ucXTNaWTlyWPNWIru7ULBOeEpc",
        "09-5.mp3": "1QRGgDIy0Iy-v69_lBPmDplcyVeQmctPC",
    },
    # Bai 10
    "Bai_10": {
        "10-1.mp3": "1EEImsa2WUr5xy8ymij78S6yLLlynf-oG",
        "10-2.mp3": "17agQCzbGwgOl5SPT5tJRQqijBCgyKvIB",
        "10-3.mp3": "1js5WrnuPWSjrzr0Vf-0B1Ad5n1kzwfaU",
        "10-4.mp3": "1dxgbVy4I7443Akr2hpXiWcyUbJ1B9BFp",
    }
}

base_dir = r"e:\HSK3\2_Web_SoanBai_HSK3\audio_textbook"

for folder, files in DRIVE_FILES.items():
    target_folder = os.path.join(base_dir, folder)
    os.makedirs(target_folder, exist_ok=True)
    print(f"\n=== DOWNLOADING FOR {folder} ===")
    for fname, drive_id in files.items():
        dest = os.path.join(target_folder, fname)
        url = f"https://drive.google.com/uc?export=download&id={drive_id}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        try:
            with urllib.request.urlopen(req) as resp:
                data = resp.read()
            with open(dest, 'wb') as f:
                f.write(data)
            print(f"  [OK] {fname}: {len(data):,} bytes -> {dest}")
        except Exception as e:
            print(f"  [FAIL] {fname} (ID: {drive_id}): {e}")

print("\n🎉 All Google Drive audio files for Bài 5 - 10 downloaded and updated!")
