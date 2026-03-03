import os, shutil, subprocess, sys

DRY_RUN = "--dry-run" in sys.argv

def log(msg):
    print(("[DRY RUN] " if DRY_RUN else "") + msg)

def move(src, dst):
    if os.path.exists(src):
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        log(f"MOVE: {src} -> {dst}")
        if not DRY_RUN:
            shutil.move(src, dst)

def remove(path):
    if os.path.exists(path):
        log(f"REMOVE: {path}")
        if not DRY_RUN:
            shutil.rmtree(path) if os.path.isdir(path) else os.remove(path)

LESSON_MAP = {
    "Graphs and Functions": "1-graphs-functions",
    "Pythagoras and Trig/Pythagoras": "2-pythagoras-trig",
    "Pythagoras and Trig/Trigonometry": "2-pythagoras-trig",
    "Number": "3-number",
    "Algebra": "4-algebra",
    "Geometry & Measures": "5-geometry-measures",
    "Probability": "6-probability",
    "Statistics": "7-statistics",
}

print("=== STEP 1: Moving lessons ===")
for old, new in LESSON_MAP.items():
    p = f"lessons/verse-al-maths-restructure/{old}"
    if os.path.exists(p):
        for f in os.listdir(p):
            src = f"{p}/{f}"
            if os.path.isfile(src):
                move(src, f"lessons/{new}/{f.strip()}")
remove("lessons/verse-al-maths-restructure")

print("=== STEP 2: Flattening metadata ===")
nm = "metadata/metadata"
if os.path.exists(nm):
    for topic in os.listdir(nm):
        tp = f"{nm}/{topic}"
        if os.path.isdir(tp):
            for f in os.listdir(tp):
                src = f"{tp}/{f}"
                dst = f"metadata/{topic}/{f.strip()}"
                if os.path.isfile(src):
                    if not os.path.exists(dst):
                        move(src, dst)
                    else:
                        log(f"DUPLICATE removed: {src}")
                        if not DRY_RUN:
                            os.remove(src)
    remove(nm)

print("=== STEP 3: Creating web/ and scripts/ ===")
for d in ["web", "scripts"]:
    os.makedirs(d, exist_ok=True)
    log(f"MKDIR: {d}")

if not DRY_RUN:
    subprocess.run(["git", "add", "-A"])
    subprocess.run(["git", "commit", "-m", "refactor: clean repo structure"])
    r = subprocess.run(["git", "push"], capture_output=True, text=True)
    print("Pushed!" if r.returncode == 0 else f"Push failed: {r.stderr}")
else:
    print("\n--- DRY RUN COMPLETE ---")
    print("Run without --dry-run to apply changes:")
    print("  python3 cleanup_repo.py")
