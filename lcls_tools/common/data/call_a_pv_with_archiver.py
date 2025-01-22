from datetime import datetime
from typing import Dict
from lcls_tools.common.data.archiver import get_values_over_time_range, ArchiveDataHandler

start_date_time = datetime(
    year=2024, month=11, day=7, hour=12, minute=00, second=0, microsecond=0
)
end_date_time = datetime(
    year=2024, month=11, day=7, hour=13, minute=15, second=0, microsecond=0
)

pv1 = "DOOR:LI10:1:Closed"          # Legitimate PV
pv2 = "NotReal"                     # Fake pv not in Archive Appliance
pv3 = "ACCL:L1B:0210:ASETSUB.VALQ"  # Added to Archive Appliance in December
pv_list = [pv1, pv2, pv3]

result_dict: Dict[str, ArchiveDataHandler] = get_values_over_time_range(pv_list, start_date_time, end_date_time)
