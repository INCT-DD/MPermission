"""
Permissions: container for the normal and dangerous base Android system permissions.
"""


class PermissionsAPI29:
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
                         'ACCESS_COARSE_LOCATION'],
            "microphone": ['RECORD_AUDIO'],
            "phone": ['READ_PHONE_STATE',
                      'CALL_PHONE',
                      'READ_CALL_LOG',
                      'WRITE_CALL_LOG',
                      'ADD_VOICEMAIL',
                      'USE_SIP',
                      'PROCESS_OUTGOING_CALLS'],
            "sensors": ['BODY_SENSORS'],
            "sms": ['SEND_SMS',
                    'RECEIVE_SMS',
                    'READ_SMS',
                    'RECEIVE_WAP_PUSH',
                    'RECEIVE_MMS'],
            "storage": ['READ_EXTERNAL_STORAGE',
                        'WRITE_EXTERNAL_STORAGE']
        })

        self.normal_permissions = [
            'ACCESS_BACKGROUND_LOCATION',
            'ACCEPT_HANDOVER',
            'ACCESS_LOCATION_EXTRA_COMMANDS',
            'ACCESS_MEDIA_LOCATION',
            'ACCESS_NETWORK_STATE',
            'ACCESS_NOTIFICATION_POLICY',
            'ACCESS_WIFI_STATE',
            'ACTIVITY_RECOGNITION',
            'ANSWER_PHONE_CALLS',
            'BIND_AUTOFILL_SERVICE',
            'BIND_CALL_REDIRECTION_SERVICE',
            'BIND_CARRIER_MESSAGING_CLIENT_SERVICE',
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
            'INSTALL_SHORTCUT',
            'INSTANT_APP_FOREGROUND_SERVICE',
            'INTERNET',
            'KILL_BACKGROUND_PROCESSES',
            'MANAGE_OWN_CALLS',
            'MODIFY_AUDIO_SETTINGS',
            'NFC',
            'NFC_TRANSACTION_EVENT',
            'READ_PHONE_NUMBERS',
            'READ_SYNC_SETTINGS',
            'READ_SYNC_STATS',
            'RECEIVE_BOOT_COMPLETED',
            'REORDER_TASKS',
            'REQUEST_COMPANION_RUN_IN_BACKGROUND',
            'REQUEST_COMPANION_USE_DATA_IN_BACKGROUND',
            'REQUEST_DELETE_PACKAGES',
            'REQUEST_IGNORE_BATTERY_OPTIMIZATIONS',
            'REQUEST_INSTALL_PACKAGES',
            'REQUEST_PASSWORD_COMPLEXITY',
            'SMS_FINANCIAL_TRANSACTIONS',
            'START_VIEW_PERMISSION_USAGE',
            'SET_ALARM',
            'SET_TIME_ZONE',
            'SET_WALLPAPER',
            'SET_WALLPAPER_HINTS',
            'TRANSMIT_IR',
            'UNINSTALL_SHORTCUT',
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
