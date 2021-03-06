DEFAULT_SETTINGS = {
    "update_interval": 0.01,
    "debug": False,
    "hardware": {
        "device_id": 0  # only change if use more than one corsair device, and it's interfering with the program
    },
    "renders": {
        "active": ["BackgroundRender", "HpRender", "WeaponRender", "BombRender", "SmokeRender", "FireRender", "FlashbangRender", "ChatRender"],
        "settings": {
            "BackgroundRender": {
                "ct_color": "#5C7793",
                "t_color": "#C16734"
            },
            "BombRender": {
                "explode_time": 40
            },
            "FlashbangRender": {
                "gradient": True
            },
            "SmokeRender": {
                "gradient": True
            },
            "FireRender": {
                "gradient": True
            },
            "ChatRender": {
                "color": "#C1C100"
            }
        }
    }
}
