import os
from datetime import date

input_file = "./us_billboard.psv"
output_file_titles = "./files/billboard-titles-{}.txt".format(date.today().strftime("%Y-%m-%d"))
output_file_artists = "./files/billboard-artists-{}.txt".format(date.today().strftime("%Y-%m-%d"))

with open(input_file, 'r') as f:
    lines = f.readlines()

# Extract titles
titles = [line.split('|')[4] for line in lines]

with open(output_file_titles, 'w') as f:
    f.write('\n'.join(titles))

# Extract artists and replace "featuring" with new lines
artists = [line.split('|')[5].replace(' featuring ', '\n') for line in lines]

with open(output_file_artists, 'w') as f:
    f.write('\n'.join(artists))
