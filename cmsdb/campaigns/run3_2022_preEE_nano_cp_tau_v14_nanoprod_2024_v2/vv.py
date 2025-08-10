# vv.py
# Link: /store/user/ksavva/data/HLepRare/skim_2024_v2/Run3_2022

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_cp_tau_v14_nanoprod_2024_v2 import campaign_run3_2022_preEE_nano_cp_tau_v14_nanoprod_2024_v2 as cpn




cpn.add_dataset(
    name='ww',
    id=22140140,
    is_data=False,
    processes=[procs.ww],
    keys=['/WW'],
    n_files=10,
    n_events=15405496.0, # this n_events is the gensumwt
    aux={'n_events': 15405496} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='ww_dl_powheg',
    id=22140141,
    is_data=False,
    processes=[procs.ww_dl],
    keys=['/WWto2L2Nu_powheg', '/WWto2L2Nu_powheg_ext1'],
    n_files=17,
    n_events=12732644.0, # this n_events is the gensumwt
    aux={'n_events': 12735192} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='ww_sl_powheg',
    id=22140142,
    is_data=False,
    processes=[procs.ww_sl],
    keys=['/WWtoLNu2Q_powheg', '/WWtoLNu2Q_powheg_ext1'],
    n_files=58,
    n_events=53661178.0, # this n_events is the gensumwt
    aux={'n_events': 53671760} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='ww_fh_powheg',
    id=22140143,
    is_data=False,
    processes=[procs.ww_fh],
    keys=['/WWto4Q_powheg', '/WWto4Q_powheg_ext1'],
    n_files=58,
    n_events=56360585.0, # this n_events is the gensumwt
    aux={'n_events': 56371745} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='ww_sl_amcatnlo',
    id=22140144,
    is_data=False,
    processes=[procs.ww_sl],
    keys=['/WWtoLNu2Q_amcatnloFXFX'],
    n_files=28,
    n_events=14248541.0, # this n_events is the gensumwt
    aux={'n_events': 23835113} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='ww_fh_amcatnlo',
    id=22140145,
    is_data=False,
    processes=[procs.ww_fh],
    keys=['/WWto4Q_amcatnloFXFX'],
    n_files=9,
    n_events=6813648.0, # this n_events is the gensumwt
    aux={'n_events': 11293022} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wz',
    id=22140146,
    is_data=False,
    processes=[procs.wz],
    keys=['/WZ'],
    n_files=5,
    n_events=7479528.0, # this n_events is the gensumwt
    aux={'n_events': 7479528} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wz_wlnu_zll_powheg',
    id=22140147,
    is_data=False,
    processes=[procs.wz_wlnu_zll],
    keys=['/WZto3LNu_powheg'],
    n_files=4,
    n_events=2791528.0, # this n_events is the gensumwt
    aux={'n_events': 2797132} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wz_wqq_zll_powheg',
    id=22140148,
    is_data=False,
    processes=[procs.wz_wqq_zll],
    keys=['/WZto2L2Q_powheg', '/WZto2L2Q_powheg_ext1'],
    n_files=10,
    n_events=8432772.0, # this n_events is the gensumwt
    aux={'n_events': 8441558} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wz_wlnu_zqq_powheg',
    id=22140149,
    is_data=False,
    processes=[procs.wz_wlnu_zqq],
    keys=['/WZtoLNu2Q_powheg', '/WZtoLNu2Q_powheg_ext1'],
    n_files=19,
    n_events=17619082.0, # this n_events is the gensumwt
    aux={'n_events': 17626624} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wz_wlnu_zll_amcatnlo',
    id=22140150,
    is_data=False,
    processes=[procs.wz_wlnu_zll],
    keys=['/WZto3LNu_amcatnloFXFX'],
    n_files=4,
    n_events=1906322.0, # this n_events is the gensumwt
    aux={'n_events': 3006412} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wz_wlnu_zqq_amcatnlo',
    id=22140151,
    is_data=False,
    processes=[procs.wz_wlnu_zqq],
    keys=['/WZtoLNu2Q_amcatnloFXFX'],
    n_files=4,
    n_events=1404272.0, # this n_events is the gensumwt
    aux={'n_events': 2453964} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='zz',
    id=22140152,
    is_data=False,
    processes=[procs.zz],
    keys=['/ZZ'],
    n_files=1,
    n_events=1181750.0, # this n_events is the gensumwt
    aux={'n_events': 1181750} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='zz_zqq_zll_powheg',
    id=22140153,
    is_data=False,
    processes=[procs.zz_zqq_zll],
    keys=['/ZZto2L2Q_powheg', '/ZZto2L2Q_powheg_ext1'],
    n_files=33,
    n_events=29478956.0, # this n_events is the gensumwt
    aux={'n_events': 29662670} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='zz_zqq_zll_amcatnlo',
    id=22140154,
    is_data=False,
    processes=[procs.zz_zqq_zll],
    keys=['/ZZto2L2Q_amcatnloFXFX'],
    n_files=4,
    n_events=1310582.0, # this n_events is the gensumwt
    aux={'n_events': 2150664} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='zz_zll_znunu_powheg',
    id=22140155,
    is_data=False,
    processes=[procs.zz_zll_znunu],
    keys=['/ZZto2L2Nu_powheg', '/ZZto2L2Nu_powheg_ext1'],
    n_files=29,
    n_events=29249225.0, # this n_events is the gensumwt
    aux={'n_events': 29313363} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='zz_zll_zll_powheg',
    id=22140156,
    is_data=False,
    processes=[procs.zz_zll_zll],
    keys=['/ZZto4L_powheg', '/ZZto4L_powheg_ext1'],
    n_files=35,
    n_events=28778338.0, # this n_events is the gensumwt
    aux={'n_events': 29079492} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='zz_znunu_zqq_powheg',
    id=22140157,
    is_data=False,
    processes=[procs.zz_znunu_zqq],
    keys=['/ZZto2Nu2Q_powheg', '/ZZto2Nu2Q_powheg_ext1'],
    n_files=4,
    n_events=5881587.0, # this n_events is the gensumwt
    aux={'n_events': 5890817} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='www',
    id=22140158,
    is_data=False,
    processes=[procs.www],
    keys=['/WWW_4F'],
    n_files=1,
    n_events=408136.0, # this n_events is the gensumwt
    aux={'n_events': 450000} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wwz',
    id=22140159,
    is_data=False,
    processes=[procs.wwz],
    keys=['/WWZ_4F'],
    n_files=4,
    n_events=1774030.0, # this n_events is the gensumwt
    aux={'n_events': 1950044} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='wzz',
    id=22140160,
    is_data=False,
    processes=[procs.wzz],
    keys=['/WZZ'],
    n_files=4,
    n_events=1806418.0, # this n_events is the gensumwt
    aux={'n_events': 1987058} # n_events in aux is the nEvents produced
)

cpn.add_dataset(
    name='zzz',
    id=22140161,
    is_data=False,
    processes=[procs.zzz],
    keys=['/ZZZ'],
    n_files=3,
    n_events=1751582.0, # this n_events is the gensumwt
    aux={'n_events': 1970234} # n_events in aux is the nEvents produced
)