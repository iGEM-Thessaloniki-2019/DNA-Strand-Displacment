## export_kinda.py -> export_csv.py / export_box_figure.py

# Perform data analysis on system_raw.kinda (created from system.pil)-- 1st experiment

import datetime
import kinda


DATA_PATH = 'first_reaction.json'

OUTPUT_PATH = 'fast_false.csv'

out = open(OUTPUT_PATH, 'w')

out.write("# Data analyzed from {} on {}\n,\n".format(DATA_PATH, datetime.datetime.now().strftime("%x at %X")))

## Import collected data.
sstats = kinda.import_data(DATA_PATH)
print('**************')
print(sstats)

## For each reaction, print k_1 and k_2 data.
rxns = sstats.get_reactions()
out.write('# REACTION RATE DATA\n')
out.write('reaction,k_1,k_1 err,k_2,k_2 err\n')
for r in rxns:
  stats = sstats.get_stats(r)

  k_1 = stats.get_k1(max_sims=0)
  k_1_err = stats.get_k1_error(max_sims=0)
  k_2 = stats.get_k2(max_sims=0)
  k_2_err = stats.get_k2_error(max_sims=0)
  out.write('{},{},{},{},{}\n'.format(r, k_1, k_1_err, k_2, k_2_err))
out.write(',\n')

## For each resting set, print probability of expected conformations (1-p_spurious) and temporary depletion.
restingsets = sstats.get_restingsets()  ##it was (spurious = False)-- mayb it will be an error
out.write('# RESTING SET DATA\n')
out.write('resting set,p(nonspurious),p(nonspurious) err,temporary depletion\n')
for rs in restingsets:
  stats = sstats.get_stats(rs)

  p_nonspurious = 1 - stats.get_conformation_prob(None, max_sims=0)
  p_nonspurious_err = stats.get_conformation_prob_error(None, max_sims=0)
  temp_dep = stats.get_temporary_depletion(max_sims=0)
  out.write('{},{},{},{}\n'.format(rs, p_nonspurious, p_nonspurious_err, temp_dep))
out.write(',\n')

out.close()
