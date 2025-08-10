# signal.py
# Link: /store/user/ksavva/data/HLepRare/skim_2024_v2/Run3_2023

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_cp_tau_v14_nanoprod_2024_v2 import campaign_run3_2023_preBPix_nano_cp_tau_v14_nanoprod_2024_v2 as cpn




cpn.add_dataset(
    name='h_ggf_tautau_uncorrelated_filter',
    id=23140175,
    is_data=False,
    processes=[procs.h_ggf_htt],
    keys=['/GluGluHTo2Tau_UncorrelatedDecay_Filtered'],
    n_files=31,
    n_events=20011211.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 20011797} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='h_ggf_tautau_uncorrelatedDecay_SM_Filtered_ProdAndDecay',
    id=23140176,
    is_data=False,
    processes=[procs.h_ggf_htt],
    keys=['/GluGluHTo2Tau_UncorrelatedDecay_SM_Filtered_ProdAndDecay'],
    n_files=35,
    n_events=17266134.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 21456982} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='h_ggf_tautau_uncorrelatedDecay_CPodd_Filtered_ProdAndDecay',
    id=23140177,
    is_data=False,
    processes=[procs.h_ggf_htt],
    keys=['/GluGluHTo2Tau_UncorrelatedDecay_CPodd_Filtered_ProdAndDecay'],
    n_files=33,
    n_events=16406657.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 20252897} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='h_ggf_tautau_uncorrelatedDecay_MM_Filtered_ProdAndDecay',
    id=23140178,
    is_data=False,
    processes=[procs.h_ggf_htt],
    keys=['/GluGluHTo2Tau_UncorrelatedDecay_MM_Filtered_ProdAndDecay'],
    n_files=37,
    n_events=18105720.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 22449164} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='h_ggf_tautau_M125_amcatnloFXFX',
    id=23140179,
    is_data=False,
    processes=[procs.h_ggf_htt],
    keys=['/GluGluHToTauTau_M125_amcatnloFXFX'],
    n_files=3,
    n_events=1113441.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 1975609} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='zh_tautau_uncorrelatedDecay_Filtered',
    id=23140180,
    is_data=False,
    processes=[procs.zh_htt],
    keys=['/ZHToTauTau_UncorrelatedDecay_Filtered'],
    n_files=5,
    n_events=1803008.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 1803008} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wph_tautau_uncorrelatedDecay_Filtered',
    id=23140181,
    is_data=False,
    processes=[procs.wh_htt],
    keys=['/WplusHToTauTau_UncorrelatedDecay_Filtered'],
    n_files=4,
    n_events=1802553.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 1887577} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wmh_tautau_uncorrelatedDecay_Filtered',
    id=23140182,
    is_data=False,
    processes=[procs.wh_htt],
    keys=['/WminusHToTauTau_UncorrelatedDecay_Filtered'],
    n_files=3,
    n_events=1248957.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 1307603} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='h_vbf_tautau_M125',
    id=23140183,
    is_data=False,
    processes=[procs.h_vbf_htt],
    keys=['/VBFHToTauTau_M125'],
    n_files=6,
    n_events=3838404.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 3843000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='h_vbf_tautau_uncorrelatedDecay_Filtered',
    id=23140184,
    is_data=False,
    processes=[procs.h_vbf_htt],
    keys=['/VBFHToTauTau_UncorrelatedDecay_Filtered'],
    n_files=24,
    n_events=12453012.0, # this n_events is the gensumwt
    aux={'is_signal': True, 'n_events': 12467954} # n_events in aux is the nEvents produced
)