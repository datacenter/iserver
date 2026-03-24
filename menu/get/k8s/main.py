import click

from menu.get.k8s.am import get_k8s_am_command
from menu.get.k8s.amcfg import get_k8s_amcfg_command
from menu.get.k8s.auth import get_k8s_auth_command
from menu.get.k8s.bmh import get_k8s_bmh_command
from menu.get.k8s.catsrc import get_k8s_catsrc_command
from menu.get.k8s.cconf import get_k8s_cconf_command
from menu.get.k8s.cluster import get_k8s_cluster
from menu.get.k8s.cm import get_k8s_cm_command
from menu.get.k8s.cni import get_k8s_cni_command
from menu.get.k8s.co import get_k8s_co_command
from menu.get.k8s.cquota import get_k8s_cquota_command
from menu.get.k8s.crb import get_k8s_crb_command
from menu.get.k8s.crd import get_k8s_crd_command
from menu.get.k8s.csv import get_k8s_csv_command
from menu.get.k8s.cv import get_k8s_cv_command
from menu.get.k8s.dc import get_k8s_dc_command
from menu.get.k8s.dep import get_k8s_dep_command
from menu.get.k8s.dns import get_k8s_dns_command
from menu.get.k8s.ds import get_k8s_ds_command
from menu.get.k8s.dsc import get_k8s_dsc_command
from menu.get.k8s.dsci import get_k8s_dsci_command
from menu.get.k8s.dv import get_k8s_dv_command
from menu.get.k8s.eip import get_k8s_eip_command
from menu.get.k8s.ep import get_k8s_ep_command
from menu.get.k8s.erouter import get_k8s_erouter_command
from menu.get.k8s.ev import get_k8s_ev_command
from menu.get.k8s.gd import get_k8s_gd_command
from menu.get.k8s.gi import get_k8s_gi_command
from menu.get.k8s.group import get_k8s_group_command
from menu.get.k8s.ing import get_k8s_ing_command
from menu.get.k8s.infra import get_k8s_infra_command
from menu.get.k8s.image_stream import get_k8s_is_command
from menu.get.k8s.kc import get_k8s_kc_command
from menu.get.k8s.kv import get_k8s_kv_command
from menu.get.k8s.limit import get_k8s_limit_command
from menu.get.k8s.locv import get_k8s_locv_command
from menu.get.k8s.locvd import get_k8s_locvd_command
from menu.get.k8s.locvdr import get_k8s_locvdr_command
from menu.get.k8s.locvs import get_k8s_locvs_command
from menu.get.k8s.lv import get_k8s_lv_command
from menu.get.k8s.lvmc import get_k8s_lvmc_command
from menu.get.k8s.mc import get_k8s_mc_command
from menu.get.k8s.mcp import get_k8s_mcp_command
from menu.get.k8s.mp import get_k8s_mp_command
from menu.get.k8s.ms import get_k8s_ms_command
from menu.get.k8s.nad import get_k8s_nad_command
from menu.get.k8s.net import get_k8s_net_command
from menu.get.k8s.nmap import get_k8s_nmap_command
from menu.get.k8s.nnce import get_k8s_nnce_command
from menu.get.k8s.nncp import get_k8s_nncp_command
from menu.get.k8s.nns import get_k8s_nns_command
from menu.get.k8s.node import get_k8s_node_command
from menu.get.k8s.ns import get_k8s_ns_command
from menu.get.k8s.og import get_k8s_og_command
from menu.get.k8s.package import get_k8s_package_command
from menu.get.k8s.pc import get_k8s_pc_command
from menu.get.k8s.pmon import get_k8s_pmon_command
from menu.get.k8s.pod import get_k8s_pod_command
from menu.get.k8s.pp import get_k8s_pp_command
from menu.get.k8s.prb import get_k8s_prb_command
from menu.get.k8s.profile import get_k8s_profile_command
from menu.get.k8s.prom import get_k8s_prom_command
from menu.get.k8s.promrule import get_k8s_promrule_command
from menu.get.k8s.promtarget import get_k8s_promtarget_command
from menu.get.k8s.pv import get_k8s_pv_command
from menu.get.k8s.pvc import get_k8s_pvc_command
from menu.get.k8s.quota import get_k8s_quota_command
from menu.get.k8s.rb import get_k8s_rb_command
from menu.get.k8s.rc import get_k8s_rc_command
from menu.get.k8s.route import get_k8s_route_command
from menu.get.k8s.rs import get_k8s_rs_command
from menu.get.k8s.ruler import get_k8s_ruler_command
from menu.get.k8s.sa import get_k8s_sa_command
from menu.get.k8s.sc import get_k8s_sc_command
from menu.get.k8s.scc import get_k8s_scc_command
from menu.get.k8s.sec import get_k8s_sec_command
from menu.get.k8s.smap import get_k8s_smap_command
from menu.get.k8s.smon import get_k8s_smon_command
from menu.get.k8s.srn import get_k8s_srn_command
from menu.get.k8s.srnnp import get_k8s_srnnp_command
from menu.get.k8s.srnns import get_k8s_srnns_command
from menu.get.k8s.standalone import get_k8s_standalone_command
from menu.get.k8s.sts import get_k8s_sts_command
from menu.get.k8s.sub import get_k8s_sub_command
from menu.get.k8s.svc import get_k8s_svc_command
from menu.get.k8s.tgar import get_k8s_tgar_command
from menu.get.k8s.tgnp import get_k8s_tgnp_command
from menu.get.k8s.tgnpn import get_k8s_tgnpn_command
from menu.get.k8s.tgpi import get_k8s_tgpi_command
from menu.get.k8s.tgsp import get_k8s_tgsp_command
from menu.get.k8s.tgspn import get_k8s_tgspn_command
from menu.get.k8s.tgtp import get_k8s_tgtp_command
from menu.get.k8s.tgtpn import get_k8s_tgtpn_command
from menu.get.k8s.tuned import get_k8s_tuned_command
from menu.get.k8s.udn import get_k8s_udn_command
from menu.get.k8s.user import get_k8s_user_command
from menu.get.k8s.va import get_k8s_va_command
from menu.get.k8s.vastc import get_k8s_vastc_command
from menu.get.k8s.vastd import get_k8s_vastd_command
from menu.get.k8s.vasts import get_k8s_vasts_command
from menu.get.k8s.ver import get_k8s_ver_command
from menu.get.k8s.vm import get_k8s_vm_command
from menu.get.k8s.vmc import get_k8s_vmc_command
from menu.get.k8s.vmcf import get_k8s_vmcf_command
from menu.get.k8s.vmcp import get_k8s_vmcp_command
from menu.get.k8s.vme import get_k8s_vme_command
from menu.get.k8s.vmf import get_k8s_vmf_command
from menu.get.k8s.vmi import get_k8s_vmi_command
from menu.get.k8s.vmim import get_k8s_vmim_command
from menu.get.k8s.vmipr import get_k8s_vmipr_command
from menu.get.k8s.vmirs import get_k8s_vmirs_command
from menu.get.k8s.vmp import get_k8s_vmp_command
from menu.get.k8s.vmr import get_k8s_vmr_command
from menu.get.k8s.vms import get_k8s_vms_command
from menu.get.k8s.vmsc import get_k8s_vmsc_command
from menu.get.k8s.vs import get_k8s_vs_command
from menu.get.k8s.vsc import get_k8s_vsc_command
from menu.get.k8s.vsclass import get_k8s_vsclass_command


class Failure(Exception):
    pass


@click.group("k8s")
@click.pass_obj
def get_k8s_menu(ctx):
    """Get k8s commands (alpha)"""


get_k8s_menu.add_command(get_k8s_am_command)
get_k8s_menu.add_command(get_k8s_amcfg_command)
get_k8s_menu.add_command(get_k8s_auth_command)
get_k8s_menu.add_command(get_k8s_bmh_command)
get_k8s_menu.add_command(get_k8s_catsrc_command)
get_k8s_menu.add_command(get_k8s_cconf_command)
get_k8s_menu.add_command(get_k8s_cluster)
get_k8s_menu.add_command(get_k8s_cm_command)
get_k8s_menu.add_command(get_k8s_cni_command)
get_k8s_menu.add_command(get_k8s_co_command)
get_k8s_menu.add_command(get_k8s_cquota_command)
get_k8s_menu.add_command(get_k8s_crb_command)
get_k8s_menu.add_command(get_k8s_crd_command)
get_k8s_menu.add_command(get_k8s_csv_command)
get_k8s_menu.add_command(get_k8s_cv_command)
get_k8s_menu.add_command(get_k8s_dc_command)
get_k8s_menu.add_command(get_k8s_dep_command)
get_k8s_menu.add_command(get_k8s_dns_command)
get_k8s_menu.add_command(get_k8s_ds_command)
get_k8s_menu.add_command(get_k8s_dsc_command)
get_k8s_menu.add_command(get_k8s_dsci_command)
get_k8s_menu.add_command(get_k8s_dv_command)
get_k8s_menu.add_command(get_k8s_eip_command)
get_k8s_menu.add_command(get_k8s_ep_command)
get_k8s_menu.add_command(get_k8s_erouter_command)
get_k8s_menu.add_command(get_k8s_ev_command)
get_k8s_menu.add_command(get_k8s_gd_command)
get_k8s_menu.add_command(get_k8s_gi_command)
get_k8s_menu.add_command(get_k8s_group_command)
get_k8s_menu.add_command(get_k8s_ing_command)
get_k8s_menu.add_command(get_k8s_infra_command)
get_k8s_menu.add_command(get_k8s_is_command)
get_k8s_menu.add_command(get_k8s_kc_command)
get_k8s_menu.add_command(get_k8s_kv_command)
get_k8s_menu.add_command(get_k8s_limit_command)
get_k8s_menu.add_command(get_k8s_locv_command)
get_k8s_menu.add_command(get_k8s_locvd_command)
get_k8s_menu.add_command(get_k8s_locvdr_command)
get_k8s_menu.add_command(get_k8s_locvs_command)
get_k8s_menu.add_command(get_k8s_lv_command)
get_k8s_menu.add_command(get_k8s_lvmc_command)
get_k8s_menu.add_command(get_k8s_mc_command)
get_k8s_menu.add_command(get_k8s_mp_command)
get_k8s_menu.add_command(get_k8s_ms_command)
get_k8s_menu.add_command(get_k8s_mcp_command)
get_k8s_menu.add_command(get_k8s_nad_command)
get_k8s_menu.add_command(get_k8s_net_command)
get_k8s_menu.add_command(get_k8s_nmap_command)
get_k8s_menu.add_command(get_k8s_nnce_command)
get_k8s_menu.add_command(get_k8s_nncp_command)
get_k8s_menu.add_command(get_k8s_nns_command)
get_k8s_menu.add_command(get_k8s_node_command)
get_k8s_menu.add_command(get_k8s_ns_command)
get_k8s_menu.add_command(get_k8s_og_command)
get_k8s_menu.add_command(get_k8s_package_command)
get_k8s_menu.add_command(get_k8s_pc_command)
get_k8s_menu.add_command(get_k8s_pmon_command)
get_k8s_menu.add_command(get_k8s_pod_command)
get_k8s_menu.add_command(get_k8s_pp_command)
get_k8s_menu.add_command(get_k8s_prb_command)
get_k8s_menu.add_command(get_k8s_profile_command)
get_k8s_menu.add_command(get_k8s_prom_command)
get_k8s_menu.add_command(get_k8s_promrule_command)
get_k8s_menu.add_command(get_k8s_promtarget_command)
get_k8s_menu.add_command(get_k8s_pv_command)
get_k8s_menu.add_command(get_k8s_pvc_command)
get_k8s_menu.add_command(get_k8s_quota_command)
get_k8s_menu.add_command(get_k8s_rb_command)
get_k8s_menu.add_command(get_k8s_rc_command)
get_k8s_menu.add_command(get_k8s_route_command)
get_k8s_menu.add_command(get_k8s_rs_command)
get_k8s_menu.add_command(get_k8s_ruler_command)
get_k8s_menu.add_command(get_k8s_sa_command)
get_k8s_menu.add_command(get_k8s_sc_command)
get_k8s_menu.add_command(get_k8s_scc_command)
get_k8s_menu.add_command(get_k8s_sec_command)
get_k8s_menu.add_command(get_k8s_smap_command)
get_k8s_menu.add_command(get_k8s_smon_command)
get_k8s_menu.add_command(get_k8s_srn_command)
get_k8s_menu.add_command(get_k8s_srnnp_command)
get_k8s_menu.add_command(get_k8s_srnns_command)
get_k8s_menu.add_command(get_k8s_standalone_command)
get_k8s_menu.add_command(get_k8s_sts_command)
get_k8s_menu.add_command(get_k8s_sub_command)
get_k8s_menu.add_command(get_k8s_svc_command)
get_k8s_menu.add_command(get_k8s_tgar_command)
get_k8s_menu.add_command(get_k8s_tgnp_command)
get_k8s_menu.add_command(get_k8s_tgnpn_command)
get_k8s_menu.add_command(get_k8s_tgpi_command)
get_k8s_menu.add_command(get_k8s_tgsp_command)
get_k8s_menu.add_command(get_k8s_tgspn_command)
get_k8s_menu.add_command(get_k8s_tgtp_command)
get_k8s_menu.add_command(get_k8s_tgtpn_command)
get_k8s_menu.add_command(get_k8s_tuned_command)
get_k8s_menu.add_command(get_k8s_udn_command)
get_k8s_menu.add_command(get_k8s_user_command)
get_k8s_menu.add_command(get_k8s_va_command)
get_k8s_menu.add_command(get_k8s_vastc_command)
get_k8s_menu.add_command(get_k8s_vastd_command)
get_k8s_menu.add_command(get_k8s_vasts_command)
get_k8s_menu.add_command(get_k8s_ver_command)
get_k8s_menu.add_command(get_k8s_vm_command)
get_k8s_menu.add_command(get_k8s_vmc_command)
get_k8s_menu.add_command(get_k8s_vmcf_command)
get_k8s_menu.add_command(get_k8s_vmcp_command)
get_k8s_menu.add_command(get_k8s_vme_command)
get_k8s_menu.add_command(get_k8s_vmf_command)
get_k8s_menu.add_command(get_k8s_vmi_command)
get_k8s_menu.add_command(get_k8s_vmim_command)
get_k8s_menu.add_command(get_k8s_vmipr_command)
get_k8s_menu.add_command(get_k8s_vmirs_command)
get_k8s_menu.add_command(get_k8s_vmp_command)
get_k8s_menu.add_command(get_k8s_vmr_command)
get_k8s_menu.add_command(get_k8s_vms_command)
get_k8s_menu.add_command(get_k8s_vmsc_command)
get_k8s_menu.add_command(get_k8s_vs_command)
get_k8s_menu.add_command(get_k8s_vsc_command)
get_k8s_menu.add_command(get_k8s_vsclass_command)
