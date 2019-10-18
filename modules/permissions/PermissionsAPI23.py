"""
Permissions: container for the normal and dangerous base Android system permissions.
"""


class PermissionsAPI23:
    """System permissions object with permissions and groups."""

    def __init__(self):
        self.dangerous_permissions = dict({
            "calendar": ['READ_CALENDAR',
                         'WRITE_CALENDAR'],
            "camera": ['CAMERA'],
            "contacts": ['READ_CONTACTS', 'WRITE_CONTACTS', 'GET_ACCOUNTS'],
            "location": ['ACCESS_FINE_LOCATION', 'ACCESS_COARSE_LOCATION'],
            "microphone": ['RECORD_AUDIO'],
            "phone": ['READ_PHONE_STATE', 'CALL_PHONE',
                      'READ_CALL_LOG', 'WRITE_CALL_LOG', 'ADD_VOICEMAIL',
                      'USE_SIP', 'PROCESS_OUTGOING_CALLS'],
            "sensors": ['BODY_SENSORS'],
            "sms": ['SEND_SMS', 'RECEIVE_SMS', 'READ_SMS',
                    'RECEIVE_WAP_PUSH', 'RECEIVE_MMS'],
            "storage": ['READ_EXTERNAL_STORAGE', 'WRITE_EXTERNAL_STORAGE']
        })

        self.normal_permissions = [
            'ACCESS_LOCATION_EXTRA_COMMANDS',
            'ACCESS_NETWORK_STATE',
            'ACCESS_NOTIFICATION_POLICY',
            'ACCESS_WIFI_STATE',
            'BLUETOOTH'
            'BLUETOOTH_ADMIN',
            'BROADCAST_STICKY',
            'CHANGE_NETWORK_STATE',
            'CHANGE_WIFI_MULTICAST_STATE',
            'CHANGE_WIFI_STATE',
            'DISABLE_KEYGUARD',
            'EXPAND_STATUS_BAR',
            'GET_PACKAGE_SIZE',
            'INSTALL_SHORTCUT',
            'INTERNET',
            'KILL_BACKGROUND_PROCESSES',
            'MODIFY_AUDIO_SETTINGS',
            'NFC',
            'READ_SYNC_SETTINGS',
            'READ_SYNC_STATS',
            'RECEIVE_BOOT_COMPLETED',
            'REORDER_TASKS',
            'REQUEST_IGNORE_BATTERY_OPTIMIZATIONS',
            'REQUEST_INSTALL_PACKAGES',
            'SET_ALARM',
            'SET_TIME_ZONE',
            'SET_WALLPAPER',
            'SET_WALLPAPER_HINTS',
            'TRANSMIT_IR',
            'UNINSTALL_SHORTCUT',
            'USE_FINGERPRINT',
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
