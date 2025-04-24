from datetime import timedelta

from flatsat_lib import Config
from flatsat_lib.config import DataStoreConfig,PusConfig
from flatsat_lib.context import Context

from endurance_db_icd.com_obc import tm as com_tm
from endurance_db_icd.com_obc import tc as com_tc

from endurance_db_icd.pf_obc import tm as pf_tm
from endurance_db_icd.pf_obc import tc as pf_tc


from gripper_test.parsing_toml import parse_toml_file

config_file = parse_toml_file('config.toml')

config = Config(
    endpoint=config_file['Config']['endpoint'],
    instance=config_file['Config']['instance'],
    pus= PusConfig(default_tc_ack_timeout=timedelta(seconds=2)),
    datastore= DataStoreConfig(links=[])
)

context = Context(config=config)
context.wait(duration=timedelta(seconds=2))

def GPM_01_IST_A1_01():
    """
    Initialize the PLSW (PLatform Software) context.
    """
    return None

def GPM_01_IST_A1_02(
        ctx:Context,
        tc_129_1 = pf_tc.TC_129_1_TODO() ):
    """
    Send TC[129,1] to switch on the gripper.
    """
    return None

def GPM_01_IST_A1_03():
    """
    Log Can for 5 seconds.
    """
    return None

def GPM_01_IST_A1_04(        
        ctx:Context,
        tc_20_1 = pf_tc.TC_20_1_ReportParameterValues(ParameterId=TODO) ):
    """
    Send TC[20,1] to request parameter values: 
        - Operation Mode
        - internal state
    """
    return None

def GPM_01_IST_A1_05(        
        ctx:Context,
        tc_129_2 = pf_tc.TC_129_2_ActiveModeTransReq() ):
    """
    Send TC[129,2] to switch off the gripper.
    """
    return None

def GPM_01_IST_A1_06(
        ctx:Context,
        tc_20_1 = pf_tc.TC_20_1_ReportParameterValues(ParameterId=TODO)
    ):
    """
    Send TC[20,1] to request parameter values:
        - Operation Mode
        - internal state
    """
    return None

def GPM_01_IST_A1_07():
    """
    Check for received TM[5,1], TM[5,2], TM[5,3] and TM[5,4].
    """
    return None