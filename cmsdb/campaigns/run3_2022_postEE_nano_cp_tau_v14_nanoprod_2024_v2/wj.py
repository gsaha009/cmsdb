# wj.py
# Link: /store/user/ksavva/data/HLepRare/skim_2024_v2/Run3_2022EE

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_nano_cp_tau_v14_nanoprod_2024_v2 import campaign_run3_2022_postEE_nano_cp_tau_v14_nanoprod_2024_v2 as cpn




cpn.add_dataset(
    name='wj_incl_madgraph',
    id=22140236,
    is_data=False,
    processes=[procs.w_lnu],
    keys=['/WtoLNu_madgraphMLM', '/WtoLNu_madgraphMLM_ext1'],
    n_files=344,
    n_events=683448011.0, # this n_events is the gensumwt
    aux={'n_events': 683448011} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_1j_madgraph',
    id=22140237,
    is_data=False,
    processes=[procs.w_lnu_1j],
    keys=['/WtoLNu_1J_madgraphMLM'],
    n_files=25,
    n_events=42695566.0, # this n_events is the gensumwt
    aux={'n_events': 42695566} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_2j_madgraph',
    id=22140238,
    is_data=False,
    processes=[procs.w_lnu_2j],
    keys=['/WtoLNu_2J_madgraphMLM'],
    n_files=29,
    n_events=36349344.0, # this n_events is the gensumwt
    aux={'n_events': 36349344} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_3j_madgraph',
    id=22140239,
    is_data=False,
    processes=[procs.w_lnu_3j],
    keys=['/WtoLNu_3J_madgraphMLM'],
    n_files=28,
    n_events=27828446.0, # this n_events is the gensumwt
    aux={'n_events': 27828446} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_4j_madgraph',
    id=22140240,
    is_data=False,
    processes=[procs.w_lnu_4j],
    keys=['/WtoLNu_4J_madgraphMLM'],
    n_files=7,
    n_events=4906634.0, # this n_events is the gensumwt
    aux={'n_events': 4906634} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wj_incl_amcatnlo',
    id=22140241,
    is_data=False,
    processes=[procs.w_lnu],
    keys=['/WtoLNu_amcatnloFXFX'],
    n_files=162,
    n_events=195475598.0, # this n_events is the gensumwt
    aux={'n_events': 287618486} # n_events in aux is the nEvents produced
)