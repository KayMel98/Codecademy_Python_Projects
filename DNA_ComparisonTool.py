sample = ['GTA','GGG','CAC']

#Function to read DNA from file
def read_dna(dna_file):
  dna_data = ""
  #opens data files to read dna data
  with open(dna_file, "r") as f:
    #append dna data var with data
    for line in f:
      dna_data += line
  return dna_data

#Function to create list of condons from str
def dna_codons(dna):
  codons = []
  for i in range(0, len(dna), 3):
    if (i+3) < len(dna):
      codons.append(dna[i: i+3])
  return codons

#Function that will compare codons to dna sample
def match_dna(dna):
  matches = 0
  #loop to iterate through dna list
  for codon in dna:
    if codon in sample:
      matches += 1
  return matches

#method to analyze matches for criminal
def is_criminal(dna_sample):
  #use methods to analyze dna
  dna_data = read_dna(dna_sample)
  codons = dna_codons(dna_data)
  num_matches = match_dna(codons)
  
  #determine if results lead to criminal
  if num_matches >= 3:
    print "The number of codon matches: %s. DNA matches suspect profile. Continue Investigation.\n" % num_matches
  else: 
    print "The number of codon matches: %s. DNA does not match suspect profile. Suspect can be released. \n" % num_matches

