# wj.py
# Link: /store/user/ksavva/data/HLepRare/skim_2024_v2/Run3_2023BPix

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_postBPix_nano_cp_tau_v14_nanoprod_2024_v2 import campaign_run3_2023_postBPix_nano_cp_tau_v14_nanoprod_2024_v2 as cpn




cpn.add_dataset(
    name='wj_incl_madgraph',
    id=23140230,
    is_data=False,
    processes=[procs.w_lnu],
    keys=['/WtoLNu_madgraphMLM'],
    n_files=51,
    n_events=94639090.0, # this n_events is the gensumwt
    aux={'n_events': 94639090} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_1j_madgraph',
    id=23140231,
    is_data=False,
    processes=[procs.w_lnu_1j],
    keys=['/WtoLNu_1J_madgraphMLM'],
    n_files=8,
    n_events=11369658.0, # this n_events is the gensumwt
    aux={'n_events': 11369658} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_2j_madgraph',
    id=23140232,
    is_data=False,
    processes=[procs.w_lnu_2j],
    keys=['/WtoLNu_2J_madgraphMLM'],
    n_files=9,
    n_events=9459992.0, # this n_events is the gensumwt
    aux={'n_events': 9459992} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_3j_madgraph',
    id=23140233,
    is_data=False,
    processes=[procs.w_lnu_3j],
    keys=['/WtoLNu_3J_madgraphMLM'],
    n_files=9,
    n_events=7718351.0, # this n_events is the gensumwt
    aux={'n_events': 7718351} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_4j_madgraph',
    id=23140234,
    is_data=False,
    processes=[procs.w_lnu_4j],
    keys=['/WtoLNu_4J_madgraphMLM'],
    n_files=3,
    n_events=1436944.0, # this n_events is the gensumwt
    aux={'n_events': 1436944} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_incl_amcatnlo',
    id=23140235,
    is_data=False,
    processes=[procs.w_lnu],
    keys=['/WtoLNu_amcatnloFXFX'],
    n_files=59,
    n_events=64991689.0, # this n_events is the gensumwt
    aux={'n_events': 95603855} # n_events in aux is the nEvents produced
)