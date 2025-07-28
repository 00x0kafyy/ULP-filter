import os

def banner():
    print("="*50)
    print(" 🔍 Smart Multi-Keyword Filter by @gibranrakamulyadi - Astraaaa")
    print("="*50)

def filter_lines(file_path, keywords, output_path="filtered.txt"):
    if not os.path.isfile(file_path):
        print(f"[!] File '{file_path}' not found.")
        return

    # Ubah semua keyword jadi lowercase
    keywords = [k.strip().lower() for k in keywords]

    count = 0
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file, \
         open(output_path, 'w') as output:
        for line in file:
            line_lower = line.lower()
            if any(k in line_lower for k in keywords):
                output.write(line)
                count += 1

    print(f"[✓] Done. {count} matching lines saved to '{output_path}'.")

if __name__ == "__main__":
    banner()
    path = input("📄 Enter input filename (e.g. list.txt): ").strip()
    raw_keywords = input("🔑 Enter keyword(s) to filter (e.g. go.id,/login,/admin): ")
    keyword_list = raw_keywords.split(',')

    filter_lines(path, keyword_list)
