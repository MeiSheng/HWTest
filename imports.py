# GPQE_RTM_GoldenEagle_10.13.0_version:10.13.0.6005

Change from master

import os
import sys
import time
sys.path.append(os.getcwd())
curr = os.getcwd()
sys.stdout.write(curr.replace("/","_"))
sys.path.append("/platypus/scriptengine/Modules")
sys.path.append("/platypus/scriptengine/Solution/MFG/Hybrid/")
sys.path.append("/platypus/scriptengine/Solution/")
try:
    all_subdirs = [d for d in os.listdir('/platypus/scriptengine/Solution/MFG/Hybrid/')]
    for folder in all_subdirs:
        sys.stdout.write(folder)
        sys.path.append("/platypus/scriptengine/Solution/MFG/Hybrid/"+folder+"/")
except:
    pass
try:
    all_subdirs = [d for d in os.listdir(os.path.dirname(curr)+"\..\..\..\..\Testware\\"+'Solution\MFG\Hybrid\\')]
    for folder in all_subdirs:
        sys.stdout.write(folder)
        sys.path.append(os.path.dirname(curr)+"\..\..\..\..\Testware\\"+'Solution\MFG\Hybrid\\'+folder+"\\")
except:
    pass
#sys.path.append("/platypus/scriptengine/Solution/MFG/Hybrid/SnowdevilESS/")
sys.path.append(os.path.dirname(curr)+"\..\..\..\Testware")
sys.path.append(os.path.dirname(curr)+"\..\..\..\..\Testware")
sys.path.append(os.path.dirname(curr)+"\..\..\..\..\..\Testware")
sys.path.append(os.path.dirname(curr)+"\..\..\Modules")
sys.path.append(os.path.dirname(curr)+"\..\..")
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"\..\..\..\Modules\Common")
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"\..\..\..\Solution")
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"\..\..\..\Solution\MFG\Hybrid")

from configure import *
#from Solution.MFG.Hybrid.SnowdevilAFT.configure import *
#from Solution.MFG.Hybrid.SnowdevilESS.configure import *
from PlatypusScripting import *
from Modules.Backend import *
import Modules
import Modules.Common
import Modules.Backend
import Modules.Platform
import Modules.Slic
#from Modules.Backend import cable_check
#from Modules.Backend import backend
from Modules.Backend import drive
from Modules.Backend import eses_dae
from Modules.Backend import eses_expander
from Modules.Backend import sata_ssd
from Modules.Common import common_cdi
from Modules.Common import common
from Modules.Common import common_firmware
from Modules.Common import common_sp_codeload
from Modules.Common import common_device_discovery
from Modules.Common.common import *
from Modules.Platform import pcie
from Modules.Platform import bmc
from Modules.Platform import error
from Modules.Platform import rtc
from Modules.Platform import system
from Modules.Slic import slic_common
from Modules.Slic import slic_cmd
from Modules.Slic import slic_resume
from Modules.Slic import common_slic_traffic
from Modules.Common import resume
from Modules.Platform import onboard_sas_controller
from Modules.Platform import i2c
from Modules.Platform import spi
from Modules.Platform import sp_cmd
from Modules.Platform import cpu
from Modules.Platform import led
from Modules.Platform import interposer_board_cmc_car
from Modules.Platform import front_panel
from Modules.Platform import cooling
from Modules.Platform import memory
from Modules.Platform import sel_moon
from Modules.Platform import sel_transformer
from Modules.Platform import sp_powersupply
from Modules.Platform import mcelog
from Modules.Slic.HBA import lox_hba
from Modules.Slic.HBA import hba_common
from Modules.Slic.HBA import lsi_sas_hba
from Modules.Slic.HBA import mellanox_infiniband_hba
from Modules.Slic.HBA import pmc_sas_hba
from Modules.Slic.HBA import broadcom_ethernet_hba
from Modules.Slic import common_slic_traffic