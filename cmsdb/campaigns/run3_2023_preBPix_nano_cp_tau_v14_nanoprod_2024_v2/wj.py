# wj.py
# Link: /store/user/ksavva/data/HLepRare/skim_2024_v2/Run3_2023

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_cp_tau_v14_nanoprod_2024_v2 import campaign_run3_2023_preBPix_nano_cp_tau_v14_nanoprod_2024_v2 as cpn




cpn.add_dataset(
    name='wj_incl_madgraph',
    id=23140130,
    is_data=False,
    processes=[procs.w_lnu],
    keys=['/WtoLNu_madgraphMLM'],
    n_files=104,
    n_events=191075090.0, # this n_events is the gensumwt
    aux={'n_events': 191075090} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_1j_madgraph',
    id=23140131,
    is_data=False,
    processes=[procs.w_lnu_1j],
    keys=['/WtoLNu_1J_madgraphMLM'],
    n_files=15,
    n_events=23085414.0, # this n_events is the gensumwt
    aux={'n_events': 23085414} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_2j_madgraph',
    id=23140132,
    is_data=False,
    processes=[procs.w_lnu_2j],
    keys=['/WtoLNu_2J_madgraphMLM'],
    n_files=18,
    n_events=20267771.0, # this n_events is the gensumwt
    aux={'n_events': 20267771} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_3j_madgraph',
    id=23140133,
    is_data=False,
    processes=[procs.w_lnu_3j],
    keys=['/WtoLNu_3J_madgraphMLM'],
    n_files=18,
    n_events=15887453.0, # this n_events is the gensumwt
    aux={'n_events': 15887453} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_4j_madgraph',
    id=23140134,
    is_data=False,
    processes=[procs.w_lnu_4j],
    keys=['/WtoLNu_4J_madgraphMLM'],
    n_files=5,
    n_events=2962673.0, # this n_events is the gensumwt
    aux={'n_events': 2962673} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_incl_amcatnlo',
    id=23140135,
    is_data=False,
    processes=[procs.w_lnu],
    keys=['/WtoLNu_amcatnloFXFX'],
    n_files=121,
    n_events=135956411.0, # this n_events is the gensumwt
    aux={'n_events': 200023087} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_0j_amcatnlo',
    id=23140136,
    is_data=False,
    processes=[procs.w_lnu_0j],
    keys=['/WtoLNu_0J_amcatnloFXFX'],
    n_files=200,
    n_events=319260057.0, # this n_events is the gensumwt
    aux={'n_events': 400733495} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_1j_amcatnlo',
    id=23140137,
    is_data=False,
    processes=[procs.w_lnu_1j],
    keys=['/WtoLNu_1J_amcatnloFXFX'],
    n_files=228,
    n_events=149517038.0, # this n_events is the gensumwt
    aux={'n_events': 308973330} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_2j_amcatnlo',
    id=23140138,
    is_data=False,
    processes=[procs.w_lnu_2j],
    keys=['/WtoLNu_2J_amcatnloFXFX'],
    n_files=201,
    n_events=60255669.0, # this n_events is the gensumwt
    aux={'n_events': 195609805} # n_events in aux is the nEvents produced
)