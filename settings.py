settings = {
    'mega_verbose':False,    
    'remote_folder':'megup',
    'summary_file':'.summary_megup'
}

#Local settings
try:
    import local_settings
    local_settings_var = local_settings.local_settings
except:
    local_settings_var = dict()

settings.update(local_settings_var)