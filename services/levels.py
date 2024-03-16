from ..schemas.levels import Level


class LevelService:

    @staticmethod
    def get_level(levels: list[Level], level_name: str):
        for level in levels:
            if level.name == level_name:
                return level
        return None
    
level_service = LevelService()