"""
Permissions: container for the normal and dangerous base Android system permissions.
"""


class PermissionsAPI31:
    """System permissions object with permissions and groups."""

    def __init__(self):
        self.dangerous_permissions = dict({
            "calendar": ['READ_CALENDAR',
                         'WRITE_CALENDAR'],
            "camera": ['CAMERA'],
            "contacts": ['READ_CONTACTS',
                         'WRITE_CONTACTS',
                         'GET_ACCOUNTS'],
            "location": ['ACCESS_FINE_LOCATION',
                         'ACCESS_COARSE_LOCATION',
                         'ACCESS_BACKGROUND_LOCATION'],
            "microphone": ['RECORD_AUDIO'],
            "phone": ['READ_PHONE_STATE',
                      'CALL_PHONE',
                      'READ_CALL_LOG',
                      'WRITE_CALL_LOG',
                      'ADD_VOICEMAIL',
                      'USE_SIP',
                      'ACCEPT_HANDOVER',
                      'ANSWER_PHONE_CALLS',
                      'READ_PHONE_NUMBERS',
                      'USE_SIP'],
            "sensors": ['BODY_SENSORS',
                        'ACTIVITY_RECOGNITION',
                        'UWB_RANGING'],
            "sms": ['SEND_SMS',
                    'RECEIVE_SMS',
                    'READ_SMS',
                    'RECEIVE_WAP_PUSH',
                    'RECEIVE_MMS',
                    'RECEIVE_WAP_PUSH'],
            "storage": ['READ_EXTERNAL_STORAGE',
                        'WRITE_EXTERNAL_STORAGE',
                        'ACCESS_MEDIA_LOCATION'],
            "bluetooth": ['BLUETOOTH_ADVERTISE',
                          'BLUETOOTH_CONNECT',
                          'BLUETOOTH_SCAN'],
            "privileged": ['BIND_QUICK_ACCESS_WALLET_SERVICE',
                          'LOADER_USAGE_STATS',
                          'MANAGE_EXTERNAL_STORAGE',
                          'MANAGE_MEDIA',
                          'MANAGE_ONGOING_CALLS',
                          'USE_ICC_AUTH_WITH_DEVICE_IDENTIFIER']
        })

        self.normal_permissions = [
            'ACCEPT_HANDOVER',
            'ACCESS_BLOBS_ACROSS_USERS',
            'ACCESS_LOCATION_EXTRA_COMMANDS',
            'ACCESS_NETWORK_STATE',
            'ACCESS_NOTIFICATION_POLICY',
            'ACCESS_WIFI_STATE',
            'BIND_AUTOFILL_SERVICE',
            'BIND_CALL_REDIRECTION_SERVICE',
            'BIND_CARRIER_MESSAGING_CLIENT_SERVICE',
            'BIND_COMPANION_DEVICE_SERVICE',
            'BIND_VISUAL_VOICEMAIL_SERVICE',
            'BLUETOOTH'
            'BLUETOOTH_ADMIN',
            'BROADCAST_STICKY',
            'CALL_COMPANION_APP',
            'CHANGE_NETWORK_STATE',
            'CHANGE_WIFI_MULTICAST_STATE',
            'CHANGE_WIFI_STATE',
            'DISABLE_KEYGUARD',
            'EXPAND_STATUS_BAR',
            'FOREGROUND_SERVICE',
            'GET_PACKAGE_SIZE',
            'HIDE_OVERLAY_WINDOWS',
            'HIGH_SAMPLING_RATE_SENSORS',
            'INSTALL_SHORTCUT',
            'INSTANT_APP_FOREGROUND_SERVICE',
            'INTERNET',
            'INTERACT_ACROSS_PROFILES',
            'KILL_BACKGROUND_PROCESSES',
            'MANAGE_OWN_CALLS',
            'MODIFY_AUDIO_SETTINGS',
            'NFC',
            'NFC_PREFERRED_PAYMENT_INFO',
            'NFC_TRANSACTION_EVENT',
            'QUERY_ALL_PACKAGES',
            'READ_PRECISE_PHONE_STATE',
            'READ_SYNC_SETTINGS',
            'READ_SYNC_STATS',
            'RECEIVE_BOOT_COMPLETED',
            'REORDER_TASKS',
            'REQUEST_COMPANION_RUN_IN_BACKGROUND',
            'REQUEST_COMPANION_USE_DATA_IN_BACKGROUND',
            'REQUEST_COMPANION_PROFILE_WATCH',
            'REQUEST_COMPANION_START_FOREGROUND_SERVICES_FROM_BACKGROUND',
            'REQUEST_DELETE_PACKAGES',
            'REQUEST_IGNORE_BATTERY_OPTIMIZATIONS',
            'REQUEST_INSTALL_PACKAGES',
            'REQUEST_OBSERVE_COMPANION_DEVICE_PRESENCE',
            'REQUEST_PASSWORD_COMPLEXITY',
            'SCHEDULE_EXACT_ALARM',
            'START_FOREGROUND_SERVICES_FROM_BACKGROUND',
            'START_VIEW_PERMISSION_USAGE',
            'SET_ALARM',
            'SET_TIME_ZONE',
            'SET_WALLPAPER',
            'SET_WALLPAPER_HINTS',
            'TRANSMIT_IR',
            'UNINSTALL_SHORTCUT',
            'UPDATE_PACKAGES_WITHOUT_USER_ACTION',
            'USE_BIOMETRIC',
            'USE_FULL_SCREEN_INTENT',
            'VIBRATE',
            'WAKE_LOCK',
            'WRITE_SYNC_SETTINGS'
        ]

    def get_dangerous_permission_group(self, permissions):
        """Given a permission return the remaining permissions from the group."""
        requested_permission_groups = dict()

        for key, value in self.dangerous_permissions.items():
            for permission in permissions:
                if permission in value:
                    requested_permission_groups[key] = self.dangerous_permissions[key]

        return requested_permission_groups
