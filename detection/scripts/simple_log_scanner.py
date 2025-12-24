import re

patterns = [
    r"(?i)or\s+1\s*=\s*1",
    r"(?i)union\s+select",
    r"--",
    r"/\*.*\*/"
]

def scan_log(file_path):
    with open(file_path, "r", errors="ignore") as log:
        for line_no, line in enumerate(log, 1):
            for pattern in patterns:
                if re.search(pattern, line):
                    print(f"[!] Suspicious entry at line {line_no}: {line.strip()}")

if __name__ == "__main__":
    scan_log("access.log")
