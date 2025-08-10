# data.py
# Link: /store/user/ksavva/data/HLepRare/skim_2024_v2/Run3_2022

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_cp_tau_v14_nanoprod_2024_v2 import campaign_run3_2022_preEE_nano_cp_tau_v14_nanoprod_2024_v2 as cpn




cpn.add_dataset(
    name='data_tau_C',
    id=2214010,
    is_data=True,
    processes=[procs.data_tau],
    keys=['/Tau_Run2022C'],
    n_files=22,
    n_events=25903135.0, # this n_events is the gensumwt
    aux={'era': 'CD', 'n_events': 25903135} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='data_tau_D',
    id=2214011,
    is_data=True,
    processes=[procs.data_tau],
    keys=['/Tau_Run2022D'],
    n_files=13,
    n_events=16686692.0, # this n_events is the gensumwt
    aux={'era': 'CD', 'n_events': 16686692} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='data_single_mu_C',
    id=2214012,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/SingleMuon_Run2022C'],
    n_files=8,
    n_events=20162441.0, # this n_events is the gensumwt
    aux={'era': 'CD', 'n_events': 20162441} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='data_mu_C',
    id=2214013,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/Muon_Run2022C'],
    n_files=60,
    n_events=138329693.0, # this n_events is the gensumwt
    aux={'era': 'CD', 'n_events': 138329693} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='data_mu_D',
    id=2214014,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/Muon_Run2022D'],
    n_files=34,
    n_events=75440027.0, # this n_events is the gensumwt
    aux={'era': 'CD', 'n_events': 75440027} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='data_double_mu_C',
    id=2214015,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/DoubleMuon_Run2022C'],
    n_files=3,
    n_events=4646904.0, # this n_events is the gensumwt
    aux={'era': 'CD', 'n_events': 4646904} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='data_muon_eg_C',
    id=2214016,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/MuonEG_Run2022C'],
    n_files=13,
    n_events=15768439.0, # this n_events is the gensumwt
    aux={'era': 'CD', 'n_events': 15768439} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='data_muon_eg_D',
    id=2214017,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/MuonEG_Run2022D'],
    n_files=7,
    n_events=8007031.0, # this n_events is the gensumwt
    aux={'era': 'CD', 'n_events': 8007031} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='data_e_C',
    id=2214018,
    is_data=True,
    processes=[procs.data_e],
    keys=['/EGamma_Run2022C'],
    n_files=119,
    n_events=263549470.0, # this n_events is the gensumwt
    aux={'era': 'CD', 'n_events': 263549470} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='data_e_D',
    id=2214019,
    is_data=True,
    processes=[procs.data_e],
    keys=['/EGamma_Run2022D'],
    n_files=46,
    n_events=89134996.0, # this n_events is the gensumwt
    aux={'era': 'CD', 'n_events': 89134996} # n_events in aux is the nEvents produced
)