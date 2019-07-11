## export_kinda.py -> export_csv.py / export_box_figure.py

# Perform data collection for PIL_PATH system

import kinda
from kinda import options
options.peppercorn_params.update({'max_reaction_count' :20000})
options.peppercorn_params.update({'max_complex_count' :10000})
options.peppercorn_params.update({'max_complex_size' :20})

# Change the MODE flag to 'demo' for quick-and-dirty results or 'publication' for more detailed results.
MODE = 'demo'

PIL_PATH = 'system.pil'
DATA_PATH = 'system_raw.kinda'

#### Read domains, strands, and complexes from old-style PIL file
sstats = kinda.from_pil('system.pil')


#### Analyze reaction rates.

## Collect all reactions to simulate.

rxns = sstats.get_reactions()

print "Reaction analysis order:"
for i,r in enumerate(rxns):
  print i,r

## Set up parameters dict.
if MODE == 'demo':
  params = {
    'relative_error':  0.5,
    'init_batch_size': 50,
    'max_batch_size':  5000,
    'max_sims':        5000,
    'sims_per_update': 1
  }
elif MODE == 'publication':
  params = {
    'relative_error':  0.01,
    'init_batch_size': 500,
    'max_batch_size':  15000,
    'max_sims':        100000,
    'sims_per_update': 50
  }

## Simulate each emuerated reaction
for i, r in enumerate(rxns):
  print "\nAnalyzing reaction {}: {}".format(i,r)

  # Get stats object
  rxn_stats = sstats.get_stats(r)

  # Query k1 and k2 reaction rates to requested precision
  rxn_stats.get_k1(verbose=1, **params)
  rxn_stats.get_k2(verbose=1, **params)
  print "k1: {} +/- {}".format(rxn_stats.get_k1(max_sims=0), rxn_stats.get_k1_error(max_sims=0))
  print "k2: {} +/- {}".format(rxn_stats.get_k2(max_sims=0), rxn_stats.get_k2_error(max_sims=0))

## Export all collected data
kinda.export_data(sstats, DATA_PATH)


#### Analyze resting sets.

## Collect all resting sets to analyze.
restingsets = sstats.get_restingsets()

print "Resting set analysis order:"
for i,rs in enumerate(restingsets):
  print i,rs
print

## Set up parameters dict.
if MODE == 'demo':
  params = {
    'relative_error':  0.1,
    'init_batch_size': 50,
    'max_batch_size':  1000,
    'max_sims':        5000
  }
elif MODE == 'publication':
  params = {
    'relative_error':  0.005,
    'init_batch_size': 500,
    'max_batch_size':  10000,
    'max_sims':        500000
  }

## Analyze each resting set
for i,rs in enumerate(restingsets):
  print "\nAnalyzing resting set {}: {}".format(i,rs)

  # Get stats object
  rs_stats = sstats.get_stats(rs)

  # Query probabilities for all conformations (including the spurious conformation, denoted as None)
  rs_stats.get_conformation_probs(verbose=1, **params)
  for c in rs.complexes:
    print c.name, rs_stats.get_conformation_prob(c.name,max_sims=0), '+/-', rs_stats.get_conformation_prob_error(c.name,max_sims=0)

## Export all collected data
kinda.export_data(sstats, DATA_PATH)
