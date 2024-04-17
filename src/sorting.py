import sys 

def extract_pmid(entry):
    return entry.split()[0]

def main():
    input_file = sys.argv[1]
    with open(input_file, 'r') as file:
        entries = file.readlines()
    sorted_entries = sorted(entries, key=extract_pmid)
    with open(input_file, 'w') as file:
        for entry in sorted_entries:
            file.write(entry)

if __name__ == "__main__":
    main()