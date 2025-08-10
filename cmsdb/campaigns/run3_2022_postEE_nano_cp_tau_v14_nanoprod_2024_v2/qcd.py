# qcd.py
# Link: /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v2/Run3_2023BPix

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_nano_cp_tau_v14_nanoprod_2024_v2 import campaign_run3_2022_postEE_nano_cp_tau_v14_nanoprod_2024_v2 as cpn


cpn.add_dataset(
    name='qcd',
    id=22140999,
    is_data=False,
    processes=[procs.qcd],
    keys=[],
    n_files=1,
    n_events=94639090.0, # this n_events is the gensumwt
    aux={'n_events': 94639090} # n_events in aux is the nEvents produced
)
