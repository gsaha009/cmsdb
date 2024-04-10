

# coding: utf-8

"""
Common, analysis independent definition of the 2017 data-taking campaign
with datasets at NanoAOD tier in version 11, created with custom content at UHH.
See https://python-order.readthedocs.io/en/latest/quickstart.html#analysis-campaign-and-config.

Dataset ids are identical to those of MiniAOD input datasets in DAS (https://cmsweb.cern.ch/das).

Since this is a custom production, neither can LFNs be obtained through DAS (or dasgloclient), nor
can PFNs be located through the usual, central redirectors.

They are centrally saved at the EOS instance at CERN under
/eos/cms/eos/cms/store/group/phys_higgs/HLepRare/HTT_skim_v1
"""

from order import Campaign


#
# campaign
#

campaign_run2_2017_cms_taupog_nano_v12 = Campaign(
    name="run2_2017_cms_taupog_nano_v12",
    id=220171220,  # 2 2017 12 20(t)
    ecm=13,
    bx=25,
    aux={
        "tier": "NanoAOD",
        "year": 2017,
        "version": 12,
        "custom": {
            "name": "cms_taupog",
            "creator": "cms",
            "wlcg_fs": "wlcg_fs_tau_pog_nanoaod",  # noqa
            "tag": "HTT_skim_v1",
        },
    },
)


# trailing imports to load datasets
# import cmsdb.campaigns.run2_2017_cms_taupog_nano_v12.data  # noqa
import cmsdb.campaigns.run2_2017_cms_taupog_nano_v12.top  # noqa
# import cmsdb.campaigns.run2_2017_cms_taupog_nano_v12.ewk  # noqa
# import cmsdb.campaigns.run2_2017_cms_taupog_nano_v12.qcd  # noqa
# import cmsdb.campaigns.run2_2017_cms_taupog_nano_v12.higgs  # noqa
# import cmsdb.campaigns.run2_2017_cms_taupog_nano_v12.hh2bbtautau  # noqa
