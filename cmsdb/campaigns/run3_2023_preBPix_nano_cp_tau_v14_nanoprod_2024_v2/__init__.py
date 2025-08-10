# coding: utf-8

from order import Campaign


# ----------- #
#   Campaign  #
# ----------- #
campaign_run3_2023_preBPix_nano_cp_tau_v14_nanoprod_2024_v2 = Campaign(
    name='run3_2023_preBPix_nano_cp_tau_v14_nanoprod_2024_v2',
    id=231401,
    ecm=13.6,
    bx=25,
    aux={
        "tier": "NanoAOD", 
        "year": 2023,
        "run": 3,
        "postfix": "preBPix",
        "version": 14,
        "custom": {
            "name": "run3_2023_preBPix_nano_cp_tau_v14_nanoprod_2024_v2",
            "creator": "IPHC",
            "location": "/store/user/ksavva/data/HLepRare/skim_2024_v2/Run3_2023",
        },
    },
)


# trailing imports to load datasets
import cmsdb.campaigns.run3_2023_preBPix_nano_cp_tau_v14_nanoprod_2024_v2.data
import cmsdb.campaigns.run3_2023_preBPix_nano_cp_tau_v14_nanoprod_2024_v2.dy
import cmsdb.campaigns.run3_2023_preBPix_nano_cp_tau_v14_nanoprod_2024_v2.signal
import cmsdb.campaigns.run3_2023_preBPix_nano_cp_tau_v14_nanoprod_2024_v2.st
import cmsdb.campaigns.run3_2023_preBPix_nano_cp_tau_v14_nanoprod_2024_v2.tt
import cmsdb.campaigns.run3_2023_preBPix_nano_cp_tau_v14_nanoprod_2024_v2.vv
import cmsdb.campaigns.run3_2023_preBPix_nano_cp_tau_v14_nanoprod_2024_v2.wj
import cmsdb.campaigns.run3_2023_preBPix_nano_cp_tau_v14_nanoprod_2024_v2.qcd
