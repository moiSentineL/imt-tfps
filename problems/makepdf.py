
import os
import glob

bruh = sorted([i for i in glob.glob('*md')])
for i in range(len(bruh)):
    print(f"creating proof {i+1}")
    os.system(f"pandoc {bruh[i]} -o '../pdfs/proof-{i +
              1}.pdf' --pdf-engine pdflatex")
