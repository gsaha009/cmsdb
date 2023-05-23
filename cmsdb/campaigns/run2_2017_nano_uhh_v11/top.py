# coding: utf-8

"""
Top quark datasets for the 2017 data-taking campaign with datasets at NanoAOD tier in
version 11, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2017_nano_uhh_v11 import campaign_run2_2017_nano_uhh_v11 as cpn


#
# ttbar
#

cpn.add_dataset(
    name="tt_sl_powheg",
    id=14186280,
    processes=[procs.tt_sl],
    keys=[
        "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=436,
    n_events=355332000,
)
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#         "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=436,
#     n_events=355332000,
# ),
#         tune_up=DatasetInfo(
#             keys=[
#                 "/TTToSemiLeptonic_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#             ],
#             n_files=142,
#             n_events=137062000,
#         ),
#         tune_down=DatasetInfo(
#             keys=[
#                 "/TTToSemiLeptonic_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#             ],
#             n_files=122,
#             n_events=134394000,
#         ),
#         hdamp_up=DatasetInfo(
#             keys=[
#                 "/TTToSemiLeptonic_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#             ],
#             n_files=119,
#             n_events=132184000,
#         ),
#         hdamp_down=DatasetInfo(
#             keys=[
#                 "/TTToSemiLeptonic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#             ],
#             n_files=119,
#             n_events=133515999,
#         ),
#         mtop_up=DatasetInfo(
#             keys=[
#                 "/TTToSemiLeptonic_mtop173p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#             ],
#             n_files=142,
#             n_events=137904000,
#         ),
#         mtop_down=DatasetInfo(
#             keys=[
#                 "/TTToSemiLeptonic_mtop171p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#             ],
#             n_files=111,
#             n_events=132484000,
#         ),
#     ),
# )




cpn.add_dataset(
    name="tt_dl_powheg",
    id=14188237,
    processes=[procs.tt_dl],
    keys=[
        "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=123,
    n_events=106724000,
)

#     info=dict(
#         nominal=DatasetInfo(
#     keys=[
#         "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=123,
#     n_events=106724000,
# ),
#         tune_up=DatasetInfo(
#             keys=[
#                 "/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#             ],
#             n_files=56,
#             n_events=42388000,
#         ),
#         tune_down=DatasetInfo(
#             keys=[
#                 "/TTTo2L2Nu_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#             ],
#             n_files=39,
#             n_events=39285000,
#         ),
#         hdamp_up=DatasetInfo(
#             keys=[
#                 "/TTTo2L2Nu_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#             ],
#             n_files=53,
#             n_events=39884000,
#         ),
#         hdamp_down=DatasetInfo(
#             keys=[
#                 "/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#             ],
#             n_files=60,
#             n_events=39380000,
#         ),
#         mtop_up=DatasetInfo(
#             keys=[
#                 "/TTTo2L2Nu_mtop173p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#             ],
#             n_files=40,
#             n_events=42742000,
#         ),
#         mtop_down=DatasetInfo(
#             keys=[
#                 "/TTTo2L2Nu_mtop171p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#             ],
#             n_files=55,
#             n_events=40782000,
#         ),
#     ),
# )


cpn.add_dataset(
    name="tt_fh_powheg",
    id=14222447,
    processes=[procs.tt_fh],
    keys=[
        "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=296,
    n_events=235719999,
)

#     info=dict(
#         nominal=DatasetInfo(
# keys=[
#     "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
# ],
# n_files=296,
# n_events=235719999,
# ),
#         tune_up=DatasetInfo(
#             keys=[
#                 "",  # noqa
#             ],
#             n_files=,
#             n_events=,
#         ),
#         tune_down=DatasetInfo(
#             keys=[
#                 "",  # noqa
#             ],
#             n_files=,
#             n_events=39285000,
#         ),
#         hdamp_up=DatasetInfo(
#             keys=[
#                 "",  # noqa
#             ],
#             n_files=,
#             n_events=,
#         ),
#         hdamp_down=DatasetInfo(
#             keys=[
#                 "",  # noqa
#             ],
#             n_files=,
#             n_events=,
#         ),
#         mtop_up=DatasetInfo(
#             keys=[
#                 "",  # noqa
#             ],
#             n_files=,
#             n_events=,
#         ),
#         mtop_down=DatasetInfo(
#             keys=[
#                 "",  # noqa
#             ],
#             n_files=,
#             n_events=,
#         ),
#     ),
# )



#
# ttbar + 1 vector boson
#

cpn.add_dataset(
    name="ttz_llnunu_m10_amcatnlo",
    id=14196941,
    processes=[procs.ttz_llnunu_m10],
    keys=[
        "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=21,
    n_events=14196000,
)

#     info=dict(
#         nominal=DatasetInfo(
    # keys=[
    #     "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    # ],
    # n_files=21,
    # n_events=14196000,
# ),
#         tune_up=DatasetInfo(
#             keys=[
#                 "",  # noqa
#             ],
#             n_files=,
#             n_events=,
#         ),
#         tune_down=DatasetInfo(
#             keys=[
#                 "",  # noqa
#             ],
#             n_files=,
#             n_events=,
#         ),
#     ),
# )


cpn.add_dataset(
    name="ttw_nlu_amcatnlo",
    id=14197077,
    processes=[procs.ttw_lnu],
    keys=[
        "/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=7460671,
)


#     info=dict(
#         nominal=DatasetInfo(
    # keys=[
    #     "/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    # ],
    # n_files=11,
    # n_events=7460671,
# ),
#         tune_up=DatasetInfo(
#             keys=[
#                 "",  # noqa
#             ],
#             n_files=,
#             n_events=,
#         ),
#         tune_down=DatasetInfo(
#             keys=[
#                 "",  # noqa
#             ],
#             n_files=,
#             n_events=,
#         ),
#     ),
# )


cpn.add_dataset(
    name="ttw_qq_amcatnlo",
    id=14208089,
    processes=[procs.ttw_qq],
    keys=[
        "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=655018,
)


#
# ttbar + 2 vector bosons
#

cpn.add_dataset(
    name="ttzz_madgraph",
    id=14212185,
    processes=[procs.ttzz],
    keys=[
        "/TTZZ_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=327000,
)

cpn.add_dataset(
    name="ttwz_madgraph",
    id=14213107,
    processes=[procs.ttwz],
    keys=[
        "/TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=350000,
)

cpn.add_dataset(
    name="ttww_madgraph",
    id=14226543,
    processes=[procs.ttww],
    keys=[
        "/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=698000,
)


#
# single top
#

cpn.add_dataset(
    name="st_tchannel_t_powheg",
    id=14294738,
    processes=[procs.st_tchannel_t],
    keys=[
        "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=124,
    n_events=129903000,
)
#     info=dict(
#         nominal=DatasetInfo(
    # keys=[
    #     "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    # ],
    # n_files=124,
    # n_events=129903000,
# ),
#         tune_up=DatasetInfo(
#             keys=[
#                 "",  # noqa
#             ],
#             n_files=,
#             n_events=,
#         ),
#         tune_down=DatasetInfo(
#             keys=[
#                 "",  # noqa
#             ],
#             n_files=,
#             n_events=39285000,
#         ),
#         mtop_up=DatasetInfo(
#             keys=[
#                 "",  # noqa
#             ],
#             n_files=,
#             n_events=,
#         ),
#         mtop_down=DatasetInfo(
#             keys=[
#                 "",  # noqa
#             ],
#             n_files=,
#             n_events=,
#         ),
#     ),
# )



cpn.add_dataset(
    name="st_tchannel_tbar_powheg",
    id=14296512,
    processes=[procs.st_tchannel_tbar],
    keys=[
        "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=70,
    n_events=69921000,
)


#     info=dict(
#         nominal=DatasetInfo(
    # keys=[
    #     "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    # ],
    # n_files=70,
    # n_events=69921000,
# ),
#         tune_up=DatasetInfo(
#             keys=[
#                 "",  # noqa
#             ],
#             n_files=,
#             n_events=,
#         ),
#         tune_down=DatasetInfo(
#             keys=[
#                 "",  # noqa
#             ],
#             n_files=,
#             n_events=39285000,
#         ),
#         mtop_up=DatasetInfo(
#             keys=[
#                 "",  # noqa
#             ],
#             n_files=,
#             n_events=,
#         ),
#         mtop_down=DatasetInfo(
#             keys=[
#                 "",  # noqa
#             ],
#             n_files=,
#             n_events=,
#         ),
#     ),
# )



cpn.add_dataset(
    name="st_twchannel_t_powheg",
    id=14246006,
    processes=[procs.st_twchannel_t],
    keys=[
        "/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=5649000,
)

cpn.add_dataset(
    name="st_twchannel_tbar_powheg",
    id=14251337,
    processes=[procs.st_twchannel_tbar],
    keys=[
        "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=5674000,
)
