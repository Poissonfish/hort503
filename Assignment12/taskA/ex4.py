import re
import pandas as pd
from io import StringIO

# nameFile = "TAIR10_functional_descriptionss.txt"
# with open (nameFile, 'r' ) as file:
#     text = file.read()

text = '''AT1G01060.1	protein_coding	Homeodomain-like superfamily protein	LHY encodes a myb-related putative transcription factor involved in circadian rhythm along with another myb transcription factor CCA1	LATE ELONGATED HYPOCOTYL (LHY); CONTAINS InterPro DOMAIN/s: SANT, DNA-binding (InterPro:IPR001005), Homeodomain-like (InterPro:IPR009057), Myb, DNA-binding (InterPro:IPR014778), HTH transcriptional regulator, Myb-type, DNA-binding (InterPro:IPR017930), Myb-like DNA-binding domain, SHAQKYF class (InterPro:IPR006447); BEST Arabidopsis thaliana protein match is: circadian clock associated 1 (TAIR:AT2G46830.1); Has 2469 Blast hits to 2022 proteins in 280 species: Archae - 2; Bacteria - 257; Metazoa - 292; Fungi - 162; Plants - 1048; Viruses - 29; Other Eukaryotes - 679 (source: NCBI BLink).
AT1G01060.2	protein_coding	Homeodomain-like superfamily protein	LHY encodes a myb-related putative transcription factor involved in circadian rhythm along with another myb transcription factor CCA1	LATE ELONGATED HYPOCOTYL (LHY); CONTAINS InterPro DOMAIN/s: SANT, DNA-binding (InterPro:IPR001005), Homeodomain-like (InterPro:IPR009057), Myb, DNA-binding (InterPro:IPR014778), HTH transcriptional regulator, Myb-type, DNA-binding (InterPro:IPR017930), Myb-like DNA-binding domain, SHAQKYF class (InterPro:IPR006447); BEST Arabidopsis thaliana protein match is: circadian clock associated 1 (TAIR:AT2G46830.1); Has 2469 Blast hits to 2022 proteins in 280 species: Archae - 2; Bacteria - 257; Metazoa - 292; Fungi - 162; Plants - 1048; Viruses - 29; Other Eukaryotes - 679 (source: NCBI BLink).
AT1G01060.3	protein_coding	Homeodomain-like superfamily protein	LHY encodes a myb-related putative transcription factor involved in circadian rhythm along with another myb transcription factor CCA1	LATE ELONGATED HYPOCOTYL (LHY); CONTAINS InterPro DOMAIN/s: SANT, DNA-binding (InterPro:IPR001005), Homeodomain-like (InterPro:IPR009057), Myb, DNA-binding (InterPro:IPR014778), HTH transcriptional regulator, Myb-type, DNA-binding (InterPro:IPR017930), Myb-like DNA-binding domain, SHAQKYF class (InterPro:IPR006447); BEST Arabidopsis thaliana protein match is: circadian clock associated 1 (TAIR:AT2G46830.1); Has 35333 Blast hits to 34131 proteins in 2444 species: Archae - 798; Bacteria - 22429; Metazoa - 974; Fungi - 991; Plants - 531; Viruses - 0; Other Eukaryotes - 9610 (source: NCBI BLink).
AT1G01060.4	protein_coding	Homeodomain-like superfamily protein	LHY encodes a myb-related putative transcription factor involved in circadian rhythm along with another myb transcription factor CCA1	LATE ELONGATED HYPOCOTYL (LHY); CONTAINS InterPro DOMAIN/s: SANT, DNA-binding (InterPro:IPR001005), Myb, DNA-binding (InterPro:IPR014778), Homeodomain-like (InterPro:IPR009057), Myb-like DNA-binding domain, SHAQKYF class (InterPro:IPR006447), HTH transcriptional regulator, Myb-type, DNA-binding (InterPro:IPR017930); BEST Arabidopsis thaliana protein match is: circadian clock associated 1 (TAIR:AT2G46830.1); Has 2567 Blast hits to 2041 proteins in 275 species: Archae - 2; Bacteria - 252; Metazoa - 294; Fungi - 166; Plants - 1044; Viruses - 30; Other Eukaryotes - 779 (source: NCBI BLink).
AT1G01060.5	protein_coding	Homeodomain-like superfamily protein	LHY encodes a myb-related putative transcription factor involved in circadian rhythm along with another myb transcription factor CCA1	LATE ELONGATED HYPOCOTYL (LHY); FUNCTIONS IN: DNA binding, sequence-specific DNA binding transcription factor activity; INVOLVED IN: in 11 processes; EXPRESSED IN: 22 plant structures; EXPRESSED DURING: 13 growth stages; BEST Arabidopsis thaliana protein match is: circadian clock associated 1 (TAIR:AT2G46830.1).'''

pattern = '.*?(^AT\dG\d+\.\d+|IPR\d+|$).*?'
results = re.sub(pattern, r'\1,', text, 0, flags = re.M)
results_io = StringIO(results)
df = pd.read_csv(results_io, sep=",", header=None)
df.columns = ['Transcript ID','IPR1', 'IPR2', 'IPR3', 'IPR4', 'IPR5', 'IPR6', 'IPR7']
annots = df.melt(id_vars = 'Transcript ID', value_name = 'IPR Term')
annots = annots.drop('variable', axis=1)
annots = annots.dropna()
print(annots)


