import qalib
import copy, os

def smsip_supported():
    '''
    This API verifies smsip IMS registration.
    :lastModified: 
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
    :lastModified: 
    :return: True if CID supports video call
    :parameter: none
    ''' 
    CID = dev.shell('getprop ro.csc.sales_code')
    CID = str(CID)
    CID = CID.replace("\n","")
    return re.match("(AAA|BBB|CCC|DDD|EEE)", CID)

#Google Map -----------------------------------------------------------
def grant_permssion_for_map():
    dev.shell("pm grant com.google.android.apps.maps android.permission.ACCESS_FINE_LOCATION")


def start_map_navigation(destination=None,satellite=False):
    '''
    This API that start navigation in PIP mode.
    :lastModified: 
    :return: True if Map PIP is started
    :parameter: destination of the navigation and satellite view on/off (true/false)
    ''' 
    Map_PIP = [{"resourceId":".*maps:id/custom_slider_container"}, {"resourceId":".*maps:id/mainmap_container"}]
    launch_maps_clear_popups()
    maps_ready = quick_start_navigation( destination, satellite )
    if node_exists(text = ".*(?i)Upgrade Google Maps", timeout = 3000):
        click_node(talkback = "(?i)Ignore")
    press("KEYCODE_HOME")
    pause(3000)
    if get_any_node(Map_PIP, timeout = 10000):
        print "Map PIP Started"
        return True
    else:
        FailReason("Map Navgiation PIP not started")

def clean_up_map_navigation():
    '''
    This API that stops navigation in PIP mode.
    :lastModified: 
    :return: True if Map PIP is not found
    :parameter: none
    ''' 
    Map_PIP = [{"resourceId":".*maps:id/custom_slider_container"}, {"resourceId":".*maps:id/mainmap_container"}]
    launch_app("Maps")
    disable_all_handlers()
    #print "Here!!!!!"
    back_out_to_home_screen()
    enable_all_handlers()

    if get_any_node(Map_PIP, timeout = 10000):
        return False
    else:
        return True
