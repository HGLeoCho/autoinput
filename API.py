import qalib
import copy, os

def smsip_supported():
    '''
    This API verifies smsip IMS registration.
    :lastModified: 20/03/19
    :return: True if smsip IMS registered
    :parameter: none
    ''' 
    volte_support_found = False
    single_dev_info = get_global("single_device_info")
    if single_dev_info and dev.getDeviceId() in single_dev_info:
        return single_dev_info.get(dev.getDeviceId(),{}).get("volte")
    if calling_supported():
        for ims in get_ims_system_service_list():
            ims_dump = dev.shell('dumpsys %s|grep -i "smsip\ *=\ *"|tail -n 1' % ims).strip()
            volte_support_found = bool(re.match("(?i)^[\s\t]*smsip[\s\t]*=[\s\t]*true",ims_dump))
            if volte_support_found:
                break
        if not volte_support_found:
            ims_dump = dev.shell('dumpsys activity provider com.sec.internal.ims.imsservice.SettingsProvider|grep -i -E "smsip *= (true|false)"')
            volte_support_found = bool(re.search("(?i)[\s\t]*smsip[\s\t]*=[\s\t]*true",ims_dump))
    return volte_support_found

def video_call_supported_carrier():
    '''
    This API verifies video call support.
    :lastModified: 20/03/19
    :return: True if CID supports video call
    :parameter: none
    ''' 
    CID = dev.shell('getprop ro.csc.sales_code')
    CID = str(CID)
    CID = CID.replace("\n","")
    return re.match("(AAA|BBB|CCC|DDD|EEE)", CID)
