import os
from Bio import Entrez, SeqIO

Entrez.email = "jmarsland2@gmail.com"

def fasta_maker(ids):
    
    os.makedirs("data", exist_ok=True)
    
    success_count = 0
    failed_count = 0
    
    for i, id in enumerate(ids, start = 1):
        print(f"Processing sequence {i} of {len(ids)}: {id}")
        try:
            handle = Entrez.efetch(db="nucleotide", id = id, rettype='fasta', retmode = 'text')
            record = SeqIO.read(handle, "fasta")
        except Exception as e:
            print(f"Error fetching sequence for ID: {id} - {e}")
            failed_count += 1
            continue
        
        fasta_path = f"data/{id}.fasta"
        with open(fasta_path, 'w') as file:
            SeqIO.write(record, file, "fasta")

        print(f"Successfully saved: {fasta_path}")
        print(f"ID: {record.id}")
        print(f"Description: {record.description}")
        print(f"Sequence: {record.seq[:100]}...")
        success_count += 1
    
    print("Operation complete!")
    print("Summary:")
    print(f"{success_count} sequences were successfully saved.")
    print(f"{failed_count} sequences failed to save")

def main():
    nums = [id.strip() for id in list(input("Enter your comma-separated accession numbers: ").split(','))]
    fasta_maker(nums)
    
if __name__ == "__main__":
    main()
