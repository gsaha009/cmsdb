# wj.py
# Link: /store/user/ksavva/data/HLepRare/skim_2024_v2/Run3_2022

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_cp_tau_v14_nanoprod_2024_v2 import campaign_run3_2022_preEE_nano_cp_tau_v14_nanoprod_2024_v2 as cpn




cpn.add_dataset(
    name='wj_incl_madgraph',
    id=22140134,
    is_data=False,
    processes=[procs.w_lnu],
    keys=['/WtoLNu_madgraphMLM', '/WtoLNu_madgraphMLM_ext1'],
    n_files=95,
    n_events=183585526.0, # this n_events is the gensumwt
    aux={'n_events': 183585526} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_1j_madgraph',
    id=22140135,
    is_data=False,
    processes=[procs.w_lnu_1j],
    keys=['/WtoLNu_1J_madgraphMLM'],
    n_files=8,
    n_events=11896625.0, # this n_events is the gensumwt
    aux={'n_events': 11896625} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_2j_madgraph',
    id=22140136,
    is_data=False,
    processes=[procs.w_lnu_2j],
    keys=['/WtoLNu_2J_madgraphMLM'],
    n_files=8,
    n_events=9283334.0, # this n_events is the gensumwt
    aux={'n_events': 9283334} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_3j_madgraph',
    id=22140137,
    is_data=False,
    processes=[procs.w_lnu_3j],
    keys=['/WtoLNu_3J_madgraphMLM'],
    n_files=9,
    n_events=8221862.0, # this n_events is the gensumwt
    aux={'n_events': 8221862} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_4j_madgraph',
    id=22140138,
    is_data=False,
    processes=[procs.w_lnu_4j],
    keys=['/WtoLNu_4J_madgraphMLM'],
    n_files=3,
    n_events=1463885.0, # this n_events is the gensumwt
    aux={'n_events': 1463885} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_incl_amcatnlo',
    id=22140139,
    is_data=False,
    processes=[procs.w_lnu],
    keys=['/WtoLNu_amcatnloFXFX'],
    n_files=50,
    n_events=55638210.0, # this n_events is the gensumwt
    aux={'n_events': 81878020} # n_events in aux is the nEvents produced
)