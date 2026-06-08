class AppConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.settings = {
                "theme": "Dark",
                "volume": 80,
            }
        return cls._instance

    def get_setting(self, key):
        return self.settings.get(key)

    def update_setting(self, key, value):
        self.settings[key] = value


config1 = AppConfig()
config2 = AppConfig()

config1.update_setting("theme", "Light")

print(f"Тема: {config1.get_setting('theme')}")
print(f"Тема: {config2.get_setting('theme')}")