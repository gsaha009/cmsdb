# tt.py
# Link: /store/user/ksavva/data/HLepRare/skim_2024_v2/Run3_2022

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_cp_tau_v14_nanoprod_2024_v2 import campaign_run3_2022_preEE_nano_cp_tau_v14_nanoprod_2024_v2 as cpn




cpn.add_dataset(
    name='tt_sl',
    id=22140162,
    is_data=False,
    processes=[procs.tt_sl],
    keys=['/TTtoLNu2Q', '/TTtoLNu2Q_ext1'],
    n_files=334,
    n_events=155346152.0, # this n_events is the gensumwt
    aux={'n_events': 156612890} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='tt_dl',
    id=22140163,
    is_data=False,
    processes=[procs.tt_dl],
    keys=['/TTto2L2Nu', '/TTto2L2Nu_ext1'],
    n_files=106,
    n_events=47500385.0, # this n_events is the gensumwt
    aux={'n_events': 47887413} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='tt_fh',
    id=22140164,
    is_data=False,
    processes=[procs.tt_fh],
    keys=['/TTto4Q', '/TTto4Q_ext1'],
    n_files=142,
    n_events=105030029.0, # this n_events is the gensumwt
    aux={'n_events': 105888577} # n_events in aux is the nEvents produced
)