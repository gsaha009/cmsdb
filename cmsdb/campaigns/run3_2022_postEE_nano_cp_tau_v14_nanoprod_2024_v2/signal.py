# signal.py
# Link: /store/user/ksavva/data/HLepRare/skim_2024_v2/Run3_2022EE

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_nano_cp_tau_v14_nanoprod_2024_v2 import campaign_run3_2022_postEE_nano_cp_tau_v14_nanoprod_2024_v2 as cpn




cpn.add_dataset(
    name='h_ggf_tautau_uncorrelated_filter',
    id=22140277,
    is_data=False,
    processes=[procs.h_ggf_htt],
    keys=['/GluGluHTo2Tau_UncorrelatedDecay_Filtered'],
    n_files=32,
    n_events=21340204.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 21340864} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='h_ggf_tautau_uncorrelatedDecay_CPodd_Filtered_ProdAndDecay',
    id=22140278,
    is_data=False,
    processes=[procs.h_ggf_htt],
    keys=['/GluGluHTo2Tau_UncorrelatedDecay_CPodd_Filtered_ProdAndDecay'],
    n_files=42,
    n_events=21495773.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 26545013} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='h_ggf_tautau_uncorrelatedDecay_MM_Filtered_ProdAndDecay',
    id=22140279,
    is_data=False,
    processes=[procs.h_ggf_htt],
    keys=['/GluGluHTo2Tau_UncorrelatedDecay_MM_Filtered_ProdAndDecay'],
    n_files=40,
    n_events=20689379.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 25643123} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='h_ggf_tautau_uncorrelatedDecay_SM_Filtered_ProdAndDecay',
    id=22140280,
    is_data=False,
    processes=[procs.h_ggf_htt],
    keys=['/GluGluHTo2Tau_UncorrelatedDecay_SM_Filtered_ProdAndDecay'],
    n_files=38,
    n_events=19599725.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 24356269} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='h_ggf_tautau_M125_amcatnloFXFX',
    id=22140281,
    is_data=False,
    processes=[procs.h_ggf_htt],
    keys=['/GluGluHToTauTau_M125_amcatnloFXFX'],
    n_files=5,
    n_events=1992281.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 3533459} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='zh_tautau_uncorrelatedDecay_Filtered',
    id=22140282,
    is_data=False,
    processes=[procs.zh_htt],
    keys=['/ZHToTauTau_UncorrelatedDecay_Filtered'],
    n_files=4,
    n_events=1863291.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 1863291} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wph_tautau_uncorrelatedDecay_Filtered',
    id=22140283,
    is_data=False,
    processes=[procs.wph_htt],
    keys=['/WplusHToTauTau_UncorrelatedDecay_Filtered'],
    n_files=5,
    n_events=2025321.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 2121547} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wmh_tautau_uncorrelatedDecay_Filtered',
    id=22140284,
    is_data=False,
    processes=[procs.wmh_htt],
    keys=['/WminusHToTauTau_UncorrelatedDecay_Filtered'],
    n_files=4,
    n_events=1480135.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 1550013} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='h_vbf_tautau_uncorrelatedDecay_Filtered',
    id=22140285,
    is_data=False,
    processes=[procs.h_vbf_htt],
    keys=['/VBFHToTauTau_UncorrelatedDecay_Filtered'],
    n_files=26,
    n_events=14552639.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 14569859} # n_events in aux is the nEvents produced
)