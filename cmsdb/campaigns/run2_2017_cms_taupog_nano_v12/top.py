# coding: utf-8

"""
Top quark datasets for the 2017 data-taking campaign with datasets at NanoAOD tier in
version 11, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2017_cms_taupog_nano_v12 import campaign_run2_2017_cms_taupog_nano_v12 as cpn


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
    n_files=223,
    n_events=1,  # meaningless number because I don't want to look it up
)

cpn.add_dataset(
    name="tt_dl_powheg",
    id=14188237,
    processes=[procs.tt_dl],
    keys=[
        "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=92,
    n_events=106724000,  # meaningless number because I don't want to look it up
)

cpn.add_dataset(
    name="tt_fh_powheg",
    id=14222447,
    processes=[procs.tt_fh],
    keys=[
        "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=97,
    n_events=235719999,  # meaningless number because I don't want to look it up
)
