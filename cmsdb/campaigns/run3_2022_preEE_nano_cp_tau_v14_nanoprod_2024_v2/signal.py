# signal.py
# Link: /store/user/ksavva/data/HLepRare/skim_2024_v2/Run3_2022

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_cp_tau_v14_nanoprod_2024_v2 import campaign_run3_2022_preEE_nano_cp_tau_v14_nanoprod_2024_v2 as cpn




cpn.add_dataset(
    name='h_ggf_tautau_uncorrelated_filter',
    id=22140175,
    is_data=False,
    processes=[procs.h_ggf_htt],
    keys=['/GluGluHTo2Tau_UncorrelatedDecay_Filtered'],
    n_files=12,
    n_events=8056751.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 8056963} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='h_ggf_tautau_uncorrelatedDecay_CPodd_Filtered_ProdAndDecay',
    id=22140176,
    is_data=False,
    processes=[procs.h_ggf_htt],
    keys=['/GluGluHTo2Tau_UncorrelatedDecay_CPodd_Filtered_ProdAndDecay'],
    n_files=14,
    n_events=7185840.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 8872610} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='h_ggf_tautau_uncorrelatedDecay_MM_Filtered_ProdAndDecay',
    id=22140177,
    is_data=False,
    processes=[procs.h_ggf_htt],
    keys=['/GluGluHTo2Tau_UncorrelatedDecay_MM_Filtered_ProdAndDecay'],
    n_files=13,
    n_events=6424278.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 7964846} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='h_ggf_tautau_uncorrelatedDecay_SM_Filtered_ProdAndDecay',
    id=22140178,
    is_data=False,
    processes=[procs.h_ggf_htt],
    keys=['/GluGluHTo2Tau_UncorrelatedDecay_SM_Filtered_ProdAndDecay'],
    n_files=14,
    n_events=6703604.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 8329190} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='h_ggf_tautau_M125_amcatnloFXFX',
    id=22140179,
    is_data=False,
    processes=[procs.h_ggf_htt],
    keys=['/GluGluHToTauTau_M125_amcatnloFXFX'],
    n_files=2,
    n_events=585054.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 1038456} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='h_ggf_tautau_prod_cp_even_sm',
    id=22140180,
    is_data=False,
    processes=[procs.h_ggf_htt],
    keys=['/GluGluHToTauTau_M125'],
    n_files=1,
    n_events=295692.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 295722} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='zh_tautau_uncorrelatedDecay_Filtered',
    id=22140181,
    is_data=False,
    processes=[procs.zh_htt],
    keys=['/ZHToTauTau_UncorrelatedDecay_Filtered'],
    n_files=2,
    n_events=613598.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 613598} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wph_tautau_uncorrelatedDecay_Filtered',
    id=22140182,
    is_data=False,
    processes=[procs.wh_htt],
    keys=['/WplusHToTauTau_UncorrelatedDecay_Filtered'],
    n_files=2,
    n_events=716466.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 750698} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wmh_tautau_uncorrelatedDecay_Filtered',
    id=22140183,
    is_data=False,
    processes=[procs.wh_htt],
    keys=['/WminusHToTauTau_UncorrelatedDecay_Filtered'],
    n_files=1,
    n_events=431839.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 452083} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='h_vbf_tautau_uncorrelatedDecay_Filtered',
    id=22140184,
    is_data=False,
    processes=[procs.h_vbf_htt],
    keys=['/VBFHToTauTau_UncorrelatedDecay_Filtered'],
    n_files=10,
    n_events=5082505.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 5088809} # n_events in aux is the nEvents produced
)