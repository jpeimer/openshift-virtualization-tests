ALL_OPTIONS_VM_PREFERENCE_SPEC = {
    "clock_timezone": "America/New_York",
    "clock_utc_seconds_offset": 600,
    "clock_preferred_timer": {
        "hpet": {"present": True, "tickPolicy": "demi-tick-policy"},
        "hyperv": {"present": False},
        "kvm": {"present": True},
        "pit": {"present": True, "tickPolicy": "demi-tick-policy"},
        "rtc": {
            "present": False,
            "tickPolicy": "demi-tick-policy",
            "track": "demi-track",
        },
    },
    "cpu_topology": "any",
    "devices": {
        "preferredAutoattachGraphicsDevice": True,
        "preferredAutoattachInputDevice": True,
        "preferredAutoattachMemBalloon": False,
        "preferredAutoattachPodInterface": False,
        "preferredAutoattachSerialConsole": True,
        "preferredBlockMultiQueue": True,
        "preferredCdromBus": "demi-cd-from-bus",
        "preferredDisableHotplug": False,
        "preferredDiskBlockSize": {
            "custom": {"logical": 2, "physical": 5},
            "matchVolume": {"enabled": True},
        },
        "preferredDiskBus": "demi-disk-bus",
        "preferredDiskCache": "demi-disk-cache",
        "preferredDiskDedicatedIoThread": False,
        "preferredInputBus": "demi-input-bus",
        "preferredInputType": "demi-input-type",
        "preferredInterfaceModel": "demi-interface-model",
        "preferredLunBus": "demi-lun-bus",
        "preferredNetworkInterfaceMultiQueue": False,
        "preferredRng": {},
        "preferredSoundModel": "demi-sound-model",
        "preferredTPM": {},
        "preferredUseVirtioTransitional": True,
        "preferredVirtualGPUOptions": {"display": {"enabled": True, "ramFB": {"enabled": True}}},
    },
    "features": {
        "preferredAcpi": {"enabled": True},
        "preferredApic": {"enabled": True, "endOfInterrupt": True},
        "preferredHyperv": {
            "evmcs": {"enabled": True},
            "frequencies": {"enabled": True},
            "ipi": {"enabled": True},
            "reenlightenment": {"enabled": True},
            "relaxed": {"enabled": True},
            "reset": {"enabled": True},
            "runtime": {"enabled": True},
            "spinlocks": {"enabled": True, "spinlocks": 5000},
            "synic": {"enabled": False},
            "synictimer": {
                "enabled": True,
                "direct": {"enabled": True},
            },
            "tlbflush": {"enabled": False},
            "vapic": {"enabled": True},
            "vendorid": {"enabled": True, "vendorid": "demiVendorid"},
            "vpindex": {"enabled": True},
        },
        "preferredKvm": {"hidden": True},
        "preferredPvspinlock": {"enabled": False},
        "preferredSmm": {"enabled": True},
    },
    "firmware": {
        "preferredUseBios": True,
        "preferredUseBiosSerial": False,
        "preferredEfi": {"persistent": True, "secureBoot": True},
    },
    "machine": {"preferredMachineType": "demi-machine-type"},
}

UPDATED_MEMORY_2Gi = "2Gi"
UPDATED_MEMORY_3Gi = "3Gi"